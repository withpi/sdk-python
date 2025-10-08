# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConsistencyCheckParams"]


class ConsistencyCheckParams(TypedDict, total=False):
    output1: Required[str]
    """The first output or passage to check for consistency."""

    output2: Required[str]
    """The second output or passage to check for consistency."""

    query: str
    """The optional query that generated the outputs."""
