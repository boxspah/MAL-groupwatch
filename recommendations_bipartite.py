"""
MAL-groupwatch

Module Description:
Implementation of a bipartite weighted recommendations graph based on a paper by Song (2019).
"""
from __future__ import annotations
from typing import Any, Union

from recommendations import WeightedGraph

""" Constants for recommendations system."""
INFLUENCE = 0.5
SIM_THRESHOLD = 0.01
# TODO: calibrate values


class _WeightedBipartiteVertex:
    """A vertex in a bipartite weighted recommendation graph, used to represent a user or an anime.

    Each vertex item is either a user id or anime title.

    Instance Attributes:
        - item: The data stored in this vertex, representing a user or anime.
        - kind: The type of this vertex: 'user' or 'anime'.
        - neighbours: The vertices that are adjacent to this vertex, and their corresponding
            edge weights.
        - energy: TODO

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
        - self.kind in {'user', 'anime'}
        - self.energy >= 0
    """
    item: Any
    kind: str
    energy: float
    neighbours: dict[_WeightedBipartiteVertex, Union[int, float]]

    def __init__(self, item: Any, kind: str) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        Preconditions:
            - kind in {'user', 'anime'}
        """
        self.item = item
        self.kind = kind
        self.energy = ...
        self.neighbours = {}

    def degree(self) -> int:
        """Return the degree of this vertex."""
        return len(self.neighbours)

    def similarity_score(self, other: _WeightedBipartiteVertex) -> float:
        """Return the similarity score between this vertex and other based on a sigmoid function.
        """
        ...


class WeightedBipartiteGraph(WeightedGraph):
    """A bipartite weighted graph used to represent a anime recommendation network.

    TODO: finish documentation
    """
    min_rating: int
    max_rating: int
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _WeightedBipartiteVertex object.
    _vertices: dict[Any, _WeightedBipartiteVertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}
        self.min_rating = 1
        self.max_rating = 10

        WeightedGraph.__init__(self)

    def add_vertex(self, item: Any, kind: str) -> None:
        """Add a vertex with the given item and kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {'user', 'anime'}
        """
        if item not in self._vertices:
            self._vertices[item] = _WeightedBipartiteVertex(item, kind)

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float] = 1) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
            - self._vertices[item1].kind != self._vertices[item2].kind
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            if v1.kind == v2.kind:
                return v2 in v1.neighbours
            else:
                return False
        else:
            return False

    def get_similarity_score(self, item1: Any, item2: Any, score_type: str = 'sigmoid') -> float:
        """Return the similarity score between the two given items in this graph.

        TODO: finish documentation

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - self._vertices[item1].kind == self._vertices[item2].kind == 'user'
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            return v1.similarity_score(v2)

        else:
            raise ValueError

    def similarity_coefficient(self, user1: int, user2: int, target: str) -> float:
        """Returns the similarity coefficient of user1 and user1 with respect to
        target.

        Calculation based on formula given in paper.

        Preconditions:
            - {user1, user2, target}.issubset(set(self._vertices))
            - self._vertices[user1].kind == self._vertices[user2].kind == 'user'
            - self._vertices[target].kind == 'anime'
        """
        return 1 - abs(self.get_weight(user1, target) - self.get_weight(user2, target)) / \
            (self.max_rating - self.min_rating)

    def recommend_anime(self, anime: str, limit: int,
                        score_type: str = 'unweighted') -> list[tuple[str, float]]:
        ...


def create_weighted_bipartite_graph(weighted_graph: WeightedGraph) -> WeightedBipartiteGraph:
    """Transforms a weighted graph into a weighted bipartite recomemndations graph
    according to the specifications in Song (2019)."""
    ...
