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

            if anime_id not in catalogue:
                continue
            else:
                graph.add_vertex(user_id, 'user')
                graph.add_vertex(catalogue[anime_id], 'anime')

            if rating != -1:
                graph.add_edge(user_id, catalogue[anime_id], rating)

    return graph
