# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .state import State

__all__ = ["CalibrateListParams"]


class CalibrateListParams(TypedDict, total=False):
    state: Optional[State]
    """Filter jobs by state"""
