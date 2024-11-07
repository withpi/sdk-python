# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["Dimension", "SubDimension"]


class SubDimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""


class Dimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    sub_dimensions: Required[Iterable[SubDimension]]
    """The sub dimensions of the dimension"""
