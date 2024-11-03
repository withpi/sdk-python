# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .dimension_param import DimensionParam

__all__ = ["ContractParam"]


class ContractParam(TypedDict, total=False):
    description: Required[str]
    """The full description of the contract, which may be the system prompt."""

    dimensions: Required[Iterable[DimensionParam]]
    """The dimensions associated with this contract"""

    name: Required[str]
    """The human-readable name for the contract"""
