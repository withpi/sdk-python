# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["QueryGenerateFanoutsParams"]


class QueryGenerateFanoutsParams(TypedDict, total=False):
    num_fanout_queries: Required[int]
    """The number of fanout queries to generate for each input query"""

    queries: Required[List[str]]
    """The list of queries to generate fanouts for"""
