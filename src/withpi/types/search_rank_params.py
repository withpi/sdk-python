# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SearchRankParams"]


class SearchRankParams(TypedDict, total=False):
    passages: Required[List[str]]
    """The passages to rank"""

    query: Required[str]
    """The query to compare against"""
