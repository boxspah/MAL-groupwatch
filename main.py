"""
Main module for MAL-groupwatch
"""

from load_graph import load_graph

if __name__ == '__main__':
    graph = load_graph("data/rating.csv", "data/anime.csv")

    ...
