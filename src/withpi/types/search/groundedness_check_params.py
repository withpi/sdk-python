# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroundednessCheckParams"]


class GroundednessCheckParams(TypedDict, total=False):
    context: Required[str]
    """The context to check groundedness against. Must be < 15,000 characters."""

    output: Required[str]
    """The generated output to check for groundedness. Must be < 15,000 characters."""

    processing_strategy: Literal["speed_optimized", "balanced", "quality_optimized"]
    """The processing strategy to use for the groundedness check."""

    query: str
    """The optional query that generated the output. Must be < 2,000 characters."""
