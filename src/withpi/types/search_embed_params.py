# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SearchEmbedParams"]


class SearchEmbedParams(TypedDict, total=False):
    batch: Required[bool]
    """Set to false for realtime usage, such as embedding queries.

    Set to true for batch usage, such as for embedding documents as part of
    indexing.
    """

    query: Required[List[str]]
    """List of queries or documents to embed"""
