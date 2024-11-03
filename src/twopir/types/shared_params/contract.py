# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .dimension import Dimension

__all__ = ["Contract"]


class Contract(TypedDict, total=False):
    description: Required[str]
    """The full description of the contract, which may be the system prompt."""

    dimensions: Required[Iterable[Dimension]]
    """The dimensions associated with this contract"""

    name: Required[str]
    """The human-readable name for the contract"""
