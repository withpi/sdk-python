# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchEmbedParams"]


class SearchEmbedParams(TypedDict, total=False):
    query: Required[SequenceNotStr[str]]
    """List of queries or documents to embed"""
