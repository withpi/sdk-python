# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.query_fanout_example import QueryFanoutExample

__all__ = ["QueryGenerateFanoutsParams"]


class QueryGenerateFanoutsParams(TypedDict, total=False):
    queries: Required[List[str]]
    """The list of queries to generate fanouts for"""

    example_fanout_queries: Iterable[QueryFanoutExample]
    """The list of queries to use as few-shot examples for the fanout generation"""

    num_fanout_queries: int
    """The number of fanout queries to generate for each input query"""
