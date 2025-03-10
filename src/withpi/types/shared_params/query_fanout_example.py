# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["QueryFanoutExample"]


class QueryFanoutExample(TypedDict, total=False):
    fanout_queries: Required[List[str]]
    """The list of fanout queries associated with the input"""

    query: Required[str]
    """The input query that the fanout queries are based on."""
