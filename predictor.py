"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Recommendations
Module Description:
====================
The module contains classes to represent predictions of what a given user would rate a
show.
"""
import math

import recommendations


class ReviewScorePredictor:
    """A graph-based entity that predicts a user's review for an anime.

    Instance Attributes:
        - graph: The anime review graph that this entity uses to make predictions.
    """
    graph: recommendations.WeightedGraph

    def __init__(self, graph: recommendations.WeightedGraph) -> None:
        """Initialize a new ReviewScorePredictor."""
        self.graph = graph

    def predict_review_score(self, user: str, anime: str) -> int:
        """Predict the score (1-5) that the given user would give the given show.

        If there is already an edge between the given user and anime in the graph,
        return that score. Otherwise, return a predicted score.

        Preconditions:
            - user in self.graph._vertices
            - anime in self.graph._vertices
        """
        raise NotImplementedError


class SimilarUserPredictor(ReviewScorePredictor):
    """An anime review predictor that makes a prediction based on how similar users rated the anime.

    Representation Invariants:
        - self._score_type in {'unweighted', 'strict', 'pearson'}
    """
    # Private Instance Attributes:
    #   - _score_type: the type of similarity score to use when computing similarity score
    _score_type: str

    def __init__(self, graph: recommendations.WeightedGraph,
                 score_type: str) -> None:
        """Initialize a new SimilarUserPredictor.
        """
        self._score_type = score_type
        ReviewScorePredictor.__init__(self, graph)

    def predict_review_score(self, user: str, anime: str) -> int:
        """ Predict the score

        Predictions are made in the following way:
        If there exists an edge between a user and an anime, return the weight of the edge (the user's score).
        Otherwise, return the anime's weighted score, where the weight of each review score is the similarity
        score of the given user and the reviewing user. If the total similarity score of all users for the book
        is 0, return the book's average review score.

        Preconditions:
            - user in self.graph._vertices
            - anime in self.graph._vertices
        """
        # use existing edge if it exists
        if self.graph.adjacent(user, anime):
            return self.graph.get_weight(user, anime)
        # get weighted review score
        else:
            anime_n = self.graph.get_neighbours(anime)
            total_scores = 0
            total_similarities = 0

            for n in anime_n:
                similarity = self.graph.get_similarity_score(n, user, self._score_type)
                review = self.graph.get_weight(n, anime)
                total_scores += similarity * review
                total_similarities += similarity

            if total_similarities == 0:
                return round(self.graph.average_weight(anime))
            else:
                return round(total_scores / total_similarities)


class NearestNeighbourPredictor(ReviewScorePredictor):
    """A graph-based entity that predicts a user's review score for an anime based on similar
    anime.

    Preconditions:
        - self._score_type in {'unweighted', 'strict', 'pearson'}
        - self._max_neighbours > 0
    """
    # Private Instance Attributes:
    #   - _score_type: the type of similarity score to use when computing similarity score
    #   - _max_neighbours: the maximum number of neighbours the prediction should factor into
    #   the weighted score
    _score_type: str
    _max_neighbours: int

    def __init__(self, graph: recommendations.WeightedGraph,
                 score_type: str, max_neighbours: int = 2) -> None:
        """Initialize a new NearestNeighbourPredictor."""
        self._score_type = score_type
        self._max_neighbours = max_neighbours
        ReviewScorePredictor.__init__(self, graph)

    def predict_review_score(self, user: str, anime: str) -> int:
        """Predict the user's review score for the target anime.

        If an edge exists between the user and the anime, return the weight of that edge.
        Otherwise, return the weighted score of the anime based on the top <self._max_neighbours>
        anime, where the weight is the similarity score of the target anime to the compared anime.
        If the total similarity score of all users for this anime equals 0, return the average
        review score of the anime.

        This predictor implementation is based on item-item collaborative filtering.
        """
        if self.graph.adjacent(user, anime):
            return self.graph.get_weight(user, anime)

        else:
            neighbourhood = self.graph.get_neighbours(user)

            ratings_list = sorted([(self.graph.get_similarity_score(n, anime, self._score_type), n)
                                   for n in neighbourhood])
            ratings_list = ratings_list[:self._max_neighbours]

            total_score, total_sim = 0, 0
            for sim, an in ratings_list:
                review = self.graph.get_weight(user, an)
                # adjusted_sim = 1 - math.acos(sim) / math.pi
                # print(sim, adjusted_sim)
                total_score += sim * review
                total_sim += sim

            if total_sim == 0:
                return round(self.graph.average_weight(anime))
            else:
                return round(total_score / total_sim)


if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136', 'W0221'],
        'extra-imports': ['csv'],
        'max-nested-blocks': 4
    })
