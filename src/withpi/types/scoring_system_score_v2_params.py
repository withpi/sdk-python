# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScoringSystemScoreV2Params", "ScoringSpecV2", "ScoringSpecV2DimensionsV2"]


class ScoringSystemScoreV2Params(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_spec_v2: Required[ScoringSpecV2]
    """The scoring spec to score"""


class ScoringSpecV2DimensionsV2(TypedDict, total=False):
    question: Required[str]
    """The description of the dimension"""

    custom_model_id: Optional[str]
    """
    The ID of the custom model to use for scoring. Only relevant for scoring_type of
    CUSTOM_MODEL_SCORER
    """

    parameters: Optional[Iterable[float]]
    """The learned parameters for the scoring method.

    This represents piecewise linear interpolation between [0, 1].
    """

    python_code: Optional[str]
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""

    scoring_type: Optional[Literal["PI_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]]
    """The type of scoring performed for this dimension"""

    weight: Optional[float]
    """The weight of the dimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """


class ScoringSpecV2(TypedDict, total=False):
    dimensions_v2: Required[Iterable[ScoringSpecV2DimensionsV2]]
    """The dimensions of the scoring spec"""
