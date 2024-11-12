# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .sub_dimension import SubDimension

__all__ = ["Dimension"]


class Dimension(TypedDict, total=False):
    id: Required[str]
    """The label of the dimension"""

    description: Required[str]
    """The description of the dimension"""

    sub_dimensions: Required[Iterable[SubDimension]]
    """The sub dimensions of the dimension"""
