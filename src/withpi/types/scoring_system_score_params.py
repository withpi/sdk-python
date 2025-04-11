# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.scoring_spec import ScoringSpec

__all__ = ["ScoringSystemScoreParams", "ScoringInput", "ScoringInputUnionMember1"]


class ScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_input: Required[ScoringInput]
    """Either a scoring spec or a list of questions to score"""


class ScoringInputUnionMember1(TypedDict, total=False):
    question: Required[str]
    """The description of the dimension"""

    tag: Required[Optional[str]]
    """The tag or the group to which"""

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


ScoringInput: TypeAlias = Union[ScoringSpec, Iterable[ScoringInputUnionMember1]]
