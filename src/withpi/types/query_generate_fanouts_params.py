# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["QueryGenerateFanoutsParams", "ExampleFanoutQuery"]


class QueryGenerateFanoutsParams(TypedDict, total=False):
    queries: Required[List[str]]
    """The list of queries to generate fanouts for"""

    example_fanout_queries: Iterable[ExampleFanoutQuery]
    """The list of queries to use as few-shot examples for the fanout generation"""

    num_fanout_queries: int
    """The number of fanout queries to generate for each input query"""


class ExampleFanoutQuery(TypedDict, total=False):
    fanout_queries: Required[List[str]]
    """The list of fanout queries associated with the input"""

    query: Required[str]
    """The input query that the fanout queries are based on."""
