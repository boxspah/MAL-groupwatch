"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Recommendations
Module Description:
====================
The module contains classes to represent predictions of what a given user would rate a
show.
"""

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
        - self._score_type in {'unweighted', 'strict'}
    """
    # Private Instance Attributes:
    #   - _score_type: the type of similarity score to use when computing similarity score
    _score_type: str

    def __init__(self, graph: recommendations.WeightedGraph,
                 score_type: str = 'unweighted') -> None:
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
