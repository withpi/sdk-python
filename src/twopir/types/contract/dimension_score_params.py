# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

from ..shared_params.dimension import Dimension

__all__ = ["DimensionScoreParams"]


class DimensionScoreParams(TypedDict, total=False):
    dimension: Required[Dimension]
    """The dimension to score"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""
