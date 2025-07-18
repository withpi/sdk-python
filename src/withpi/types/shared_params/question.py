# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["Question"]


class Question(TypedDict, total=False):
    question: Required[str]
    """The yes/no question to ask Pi Scoring System."""

    custom_model_id: Optional[str]
    """
    The ID of the custom model associated with the CUSTOM_MODEL_SCORER scoring_type.
    """

    is_lower_score_desirable: Optional[bool]
    """
    Indicates whether a lower score represents a better outcome (e.g., fewer errors,
    less toxicity)
    """

    label: Optional[str]
    """The label of the question."""

    parameters: Optional[Iterable[float]]
    """
    The learned parameters for the scoring question define a piecewise linear
    interpolation over the range [0, 1]. This transformation adjusts the score
    distribution to better match your preferences—for example, by pulling scores
    below 0.5 closer to 0, and scores above 0.5 closer to 1.
    """

    python_code: Optional[str]
    """The PYTHON code associated with the PYTHON_CODE scoring_type."""

    remap_spec: Union[Literal["NEUTRAL", "STRICT", "LENIENT"], Dict[str, float], None]
    """Remapping spec to modulate the scores returned by Pi Scorer"""

    scoring_type: Optional[Literal["PI_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]]
    """The type of scoring performed for this question. Default: PI_SCORER."""

    tag: Optional[str]
    """The tag or the group to which this question belongs."""

    weight: Optional[float]
    """
    The weight of the question which reflects its relative importance. The sum of
    question weights will be normalized to one internally. A higher weight counts
    for more when aggregating this subdimension into the parent dimension.
    """
