# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["Dimension"]


class Dimension(TypedDict, total=False):
    description: Required[str]
    """Human readable description of what the dimension is testing"""

    label: Required[str]
    """Human readable label for the dimension"""

    sub_dimension: Iterable[Dimension]
    """Nested dimensions to be tested as part of this one"""
