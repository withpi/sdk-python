# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ...shared.state import State

__all__ = ["GrpoListParams"]


class GrpoListParams(TypedDict, total=False):
    state: Optional[State]
    """Filter jobs by state"""
