# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroundednessCheckParams"]


class GroundednessCheckParams(TypedDict, total=False):
    context: Required[str]
    """The context to check groundedness against."""

    output: Required[str]
    """The generated output to check for groundedness."""

    processing_strategy: Literal["speed_optimized", "balanced", "quality_optimized"]
    """The processing strategy to use for the groundedness check."""

    query: str
    """The optional query that generated the output."""
