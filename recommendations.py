"""
MAL Groupwatch: recommendations
=================================================

Module Description:
The module contains classes to represent weighted graphs and vertices, which represent an anime
recommendation network with ratings.
"""
from __future__ import annotations
import math
from typing import Any, Union


class _WeightedVertex:
    """A vertex in a weighted rating graph, used to represent a user or an anime.

    Each vertex item is either a user id or an anime title.

    Adapted from CSC111, Assignment 3.

    Instance Attributes:
        - item: The data stored in this vertex, representing a user or anime.
        - kind: The type of this vertex: 'user' or 'anime'.
        - neighbours: The vertices that are adjacent to this vertex, and their corresponding
            edge weights.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
        - self.kind in {'user', 'anime'}
    """
    item: Any
    kind: str
    neighbours: dict[_WeightedVertex, Union[int, float]]

    def __init__(self, item: Any, kind: str) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        Preconditions:
            - kind in {'user', 'anime'}
        """
        self.item = item
        self.kind = kind
        self.neighbours = {}

    def degree(self) -> int:
        """Return the degree of this vertex."""
        return len(self.neighbours)

    def similarity_score_unweighted(self, other: _WeightedVertex) -> float:
        """Return the unweighted similarity score between this vertex and other.

        The unweighted similarity score is zero if either of the two vertices have no
        neighbors. Otherwise, it is the number of vertices adjacent to both self and other,
        divided by the number of vertices adjacent to either self or other. It does not take
        into account the weight of the edges.
        """
        if self.degree() == 0 or other.degree() == 0:
            return 0
        else:
            self_neighbours = set(self.neighbours.keys())
            other_neighbours = set(other.neighbours.keys())
            len_and = len(self_neighbours.intersection(other_neighbours))
            len_or = len(self_neighbours.union(other_neighbours))
            return len_and / len_or

    def similarity_score_strict(self, other: _WeightedVertex) -> float:
        """Return the strict weighted similarity score between this vertex and other.

        The weighted similarity score is zero if either of the two vertices have no
        neighbors. Otherwise, it is the number of vertices adjacent to both self and other that
        have the same weight on the corresponding edges to self and other, divided by the number of
        vertices adjacent to either self or other.
        """
        if self.degree() == 0 or other.degree() == 0:
            return 0
        else:
            self_neighbours = set(self.neighbours.keys())
            other_neighbours = set(other.neighbours.keys())
            self_other_intersect = self_neighbours.intersection(other_neighbours)
            self_other = {s for s in self_other_intersect
                          if self.neighbours[s] == other.neighbours[s]}
            len_and = len(self_other)
            len_or = len(self_neighbours.union(other_neighbours))
            return len_and / len_or

    def similarity_score_pearson(self, other: _WeightedVertex) -> float:
        """Return the Pearson correlation (centered cosine similarity) score between this vertex
        and other.

        The score is zero if either of the two vertices have no neighbours.
        If self's neighbours all have the same weight, or other's neighbours all have the same
        weight, return the strict weighted similarity score between self and other.
        Otherwise, it is the cosine similarity of the weights of each vertex's edges centered
        at 0. This is otherwise known as the Pearson correlation.
        """
        if self.degree() == 0 or other.degree() == 0:
            return 0
        else:
            self_vector = self._normalize_weights()
            other_vector = other._normalize_weights()
            mag_self = math.sqrt(sum(w ** 2 for w in self_vector.values()))
            mag_other = math.sqrt(sum(w ** 2 for w in other_vector.values()))

            if mag_other == 0:
                return self.similarity_score_strict(other)
            else:
                dot_p_so_far = 0

                for v in self_vector:
                    if v in other_vector:
                        dot_p_so_far += self_vector[v] * other_vector[v]

                return dot_p_so_far / (mag_self * mag_other)

    def _normalize_weights(self) -> dict[_WeightedVertex, Union[float, int]]:
        """Return a dictionary mapping each neighbour of self to its associated edge weight after
        being centered at 0.

        Note that the sum of all edges connected to a vertex becomes 0.

        This is a non-mutating method.
        """
        norm_dict = {}
        mean_rating = sum(self.neighbours.values()) / self.degree()

        for v, w in self.neighbours.items():
            norm_dict[v] = w - mean_rating

        return norm_dict


class WeightedGraph:
    """A weighted graph used to represent a recommendation network that keeps track of
    ratings.

    Adapted from CSC111, Assignment 3.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _WeightedVertex object.
    _vertices: dict[Any, _WeightedVertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any, kind: str) -> None:
        """Add a vertex with the given item and kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {'user', 'anime'}
        """
        if item not in self._vertices:
            self._vertices[item] = _WeightedVertex(item, kind)

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float] = 1) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Note that the *items* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return {neighbour.item for neighbour in v.neighbours}
        else:
            raise ValueError

    def get_all_vertices(self, kind: str = '') -> set:
        """Return a set of all vertex items in this graph.

        If kind != '', only return the items of the given vertex kind.

        Preconditions:
            - kind in {'', 'user', 'anime'}
        """
        if kind != '':
            return {v.item for v in self._vertices.values() if v.kind == kind}
        else:
            return set(self._vertices.keys())

    def get_weight(self, item1: Any, item2: Any) -> Union[int, float]:
        """Return the weight of the edge between the given items.

        Return 0 if item1 and item2 are not adjacent.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        return v1.neighbours.get(v2, 0)

    def average_weight(self, item: Any) -> float:
        """Return the average weight of the edges adjacent to the vertex corresponding to item.

        Raise ValueError if item does not corresponding to a vertex in the graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return sum(v.neighbours.values()) / len(v.neighbours)
        else:
            raise ValueError

    def get_similarity_score(self, item1: Any, item2: Any,
                             score_type: str) -> float:
        """Return the similarity score between the two given items in this graph.

        score_type is one of 'unweighted', 'strict', or 'pearson', corresponding to the
        different ways of calculating weighted graph vertex similarity.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - score_type in {'unweighted', 'strict', 'pearson'}
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            if score_type == 'unweighted':
                return v1.similarity_score_unweighted(v2)
            elif score_type == 'strict':
                return v1.similarity_score_strict(v2)
            elif score_type == 'pearson':
                return v1.similarity_score_pearson(v2)
            else:
                # This should never run!
                raise ValueError
        else:
            raise ValueError

    def recommend_anime(self, anime: str, limit: int,
                        score_type: str = 'unweighted') -> list[tuple[str, float]]:
        """Return a list of up to <limit> tuples, where the first element is the titles of the
        recommended anime based on similarity to the given anime and the second element is
        their corresponding similarity scores.

        Fewer than <limit> books are returned if and only if there aren't enough anime that
        have a similarity score with <anime> that is greater than 0.

        score_type is one of 'unweighted', 'strict', or 'pearson', corresponding to the
        different ways of calculating weighted graph vertex similarity.

        The corresponding similarity score formula is used
        in this method (whenever the phrase "similarity score" appears below).

        The tuples are sorted in descending order of similarity score and ties are broken in
        descending order of anime title. That is, if v1 and v2 have the same similarity score, then
        v1 comes before v2 if and only if v1.item > v2.item.

        Preconditions:
            - anime in self._vertices
            - self._vertices[anime].kind == 'anime'
            - limit >= 1
            - score_type in {'unweighted', 'strict', 'pearson'}
        """
        anime_vertices = self.get_all_vertices('anime')
        anime_vertices.remove(anime)
        anime_vertices = list(anime_vertices)

        similarity_scores = {}
        for anime_v1 in anime_vertices:
            similarity_scores[anime_v1] = self.get_similarity_score(anime, anime_v1, score_type)
        anime_vertices.sort(key=(lambda x: (similarity_scores[x], x)), reverse=True)
        animes = [(anime_v2, similarity_scores[anime_v2])
                  for anime_v2 in anime_vertices[0: limit] if similarity_scores[anime_v2] != 0]
        return animes


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136'],
        'extra-imports': ['math'],
    })
