# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["QueryGenerateFanoutsParams"]


class QueryGenerateFanoutsParams(TypedDict, total=False):
    queries: Required[List[str]]
    """The list of queries to generate fanouts for"""
