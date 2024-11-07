# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DimensionScoreParams", "Dimension", "DimensionSubDimension"]


class DimensionScoreParams(TypedDict, total=False):
    dimension: Required[Dimension]
    """The dimension to score"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""


class DimensionSubDimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""


class Dimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    sub_dimensions: Required[Iterable[DimensionSubDimension]]
    """The sub dimensions of the dimension"""
