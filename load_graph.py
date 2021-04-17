""""
Module Description:

"""
from recommendations import WeightedGraph
import html
import csv


def load_graph(reviews_file: str, animes_file: str) -> WeightedGraph:
    """
    Returns a bipartite graph corresponding to the datasets.

    TODO: write documentation

    Adapted from Assignment 3.
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
        'disable': ['E1136', 'W0221'],
        'extra-imports': ['csv'],
        'max-nested-blocks': 4
    })
