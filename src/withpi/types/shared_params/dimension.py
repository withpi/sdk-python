# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .sub_dimension import SubDimension

__all__ = ["Dimension", "ActionDimension"]


class ActionDimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    scoring_type: Required[Literal["PI_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]]
    """The type of scoring performed for this dimension"""

    action_on_low_score: Optional[bool]
    """
    If `action_on_low_score = True`, the node emits the real value if action
    dimension score is <= 0.5 and it returns -1 otherwise.
    """

    custom_model_id: Optional[str]
    """
    The ID of the custom model to use for scoring. Only relevant for scoring_type of
    CUSTOM_MODEL_SCORER
    """

    python_code: Optional[str]
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""


class Dimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    sub_dimensions: Required[Iterable[SubDimension]]
    """The sub dimensions of the dimension"""

    action_dimension: Optional[ActionDimension]
    """If `action_dimension` is set, this node is a part of short-circuit subtree.

    If the score of the action_dimension is > 0.5, then evaluate the node and return
    the actual score. If it is <= 0.5 return -1. The higher level node will ignore
    the -1 scores and thus we achieve the short-circuit behavior.
    """

    parameters: Optional[Iterable[float]]
    """The learned parameters for the scoring method.

    This represents piecewise linear interpolation between [0, 1].
    """

    weight: Optional[float]
    """
    The weight of the dimension The sum of dimension weights will be normalized to
    one internally. A higher weight counts for more when aggregating this dimension
    is aggregated into the final score.
    """
