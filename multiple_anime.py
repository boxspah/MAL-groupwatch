"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Multiple Anime

Module Description:
====================
The module contains a function to return recommendations when given multiple anime shows.
"""
from __future__ import annotations

from recommendations import WeightedGraph


def recommend_animes(animes: list[tuple[str, int]], limit: int, review_graph: WeightedGraph,
                     score_type: str = 'unweighted') -> list[str]:
    """Return a list of up to <limit> recommended animes based on similarity to the given list of
    animes in the first element of each tuple in the list <animes>, weighted by the second element
    of each tuple, review scores from 1 to 10, in the list <animes>. Fewer than <limit> books are
    returned if and only if there aren't enough animes that have a similarity score with any of the
    animes in inputted list that is greater than 0.

    score_type is one of 'unweighted' or 'strict', corresponding to the
    different ways of calculating weighted graph vertex similarity.

    The unweighted similarity score is zero if either of the two vertices have no
    neighbors. Otherwise, it is the number of vertices adjacent to both self and other,
    divided by the number of vertices adjacent to either self or other. It does not take
    into account the weight of the edges.

    The strict similarity score is zero if either of the two vertices have no
    neighbors. Otherwise, it is the number of vertices adjacent to both self and other that
    have the same weight on the corresponding edges to self and other, divided by the number of
    vertices adjacent to either self or other. This takes the weight of the edges into account.

    The corresponding similarity score formula is used
    in this method (whenever the phrase "similarity score" appears below).

    The return value is a list of the titles of recommended animes, sorted in
    descending order of similarity score, with ties broken in descending order
    of anime title. That is, if v1 and v2 have the same similarity score, then
    v1 comes before v2 if and only if v1.item > v2.item.

    Preconditions:
        - all(anime[0] in self._vertices for anime in animes)
        - self._vertices[anime].kind == 'anime'
        - limit >= 1
        - score_type in {'unweighted', 'strict'}
    """
    # Accumulator of recommended anime for each anime show in <animes>
    animes_so_far = []
    for anime, score in animes:
        recommendations = review_graph.recommend_anime(anime, limit, score_type)
        recommendations_weighted = [(show[0], score * show[1]) for show in recommendations]
        animes_so_far.extend(recommendations_weighted)
    animes_so_far.sort(key=(lambda x: x[0]), reverse=True)
    animes_so_far.sort(key=(lambda x: x[1]), reverse=True)
    recommendations_final = [anime_v1[0] for anime_v1 in animes_so_far[0: limit]
                             if anime_v1[1] != 0]
    return recommendations_final


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
