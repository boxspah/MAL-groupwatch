""""
MAL Groupwatch: load_graph
=================================================

Module Description:
The sole function in this module reads two CSV files corresponding to the Kaggle dataset and
returns a weighted bipartite graph for further processing.
"""
import html
import csv

from recommendations import WeightedGraph


def load_graph(reviews_file: str, animes_file: str) -> WeightedGraph:
    """
    Returns a weighted bipartite graph corresponding to the datasets.

    The graph stores one vertex for each user and for each anime. A user vertex stores the
    corresponding user ID; an anime vertex stores the title of the anime (not the MAL ID).
    Edges denote a review between the user and the anime. The weight of the edge is the review
    score.

    NOTE: A user who has watched, but has not REVIEWED an anime, will not be adjacent to the anime.

    Adapted from CSC111, Assignment 3.
    """
    graph = WeightedGraph()
    catalogue = {}

    with open(animes_file, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            anime_id = int(row[0])
            title = html.unescape(row[1])

            catalogue[anime_id] = title

    with open(reviews_file, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            user_id = int(row[0])
            anime_id = int(row[1])
            rating = int(row[2])

            if anime_id in catalogue and rating != -1:
                graph.add_vertex(user_id, 'user')
                graph.add_vertex(catalogue[anime_id], 'anime')

                graph.add_edge(user_id, catalogue[anime_id], rating)

    return graph


if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136'],
        'extra-imports': ['html', 'csv', 'recommendations'],
        'allowed-io': ['load_graph']
    })
