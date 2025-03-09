# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..contracts.state import State

__all__ = ["SftListParams"]


class SftListParams(TypedDict, total=False):
    state: Optional[State]
    """Filter jobs by state"""
