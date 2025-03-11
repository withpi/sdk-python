# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CalibrateStartJobParams",
    "ScoringSpec",
    "ScoringSpecDimension",
    "ScoringSpecDimensionSubDimension",
    "Example",
    "PreferenceExample",
]


class CalibrateStartJobParams(TypedDict, total=False):
    scoring_spec: Required[ScoringSpec]
    """The scoring spec to calibrate"""

    examples: Optional[Iterable[Example]]
    """Rated examples to use when calibrating the scoring spec.

    Must specify either the examples or the preference examples
    """

    preference_examples: Optional[Iterable[PreferenceExample]]
    """Preference examples to use when calibrating the scoring spec.

    Must specify either the examples or preference examples
    """

    strategy: Literal["LITE", "FULL"]
    """The strategy to use to calibrate the scoring spec.

    FULL would take longer than LITE but may result in better result.
    """


class ScoringSpecDimensionSubDimensionTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    scoring_type: Required[Literal["PI_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]]
    """The type of scoring performed for this dimension"""

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

    weight: Optional[float]
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """


ScoringSpecDimensionSubDimension: TypeAlias = Union[ScoringSpecDimensionSubDimensionTyped, Dict[str, object]]


class ScoringSpecDimensionTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    sub_dimensions: Required[Iterable[ScoringSpecDimensionSubDimension]]
    """The sub dimensions of the dimension"""

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


ScoringSpecDimension: TypeAlias = Union[ScoringSpecDimensionTyped, Dict[str, object]]


class ScoringSpecTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[ScoringSpecDimension]
    """The dimensions of the scoring system"""


ScoringSpec: TypeAlias = Union[ScoringSpecTyped, Dict[str, object]]


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Required[Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]
    """The rating of the llm_output given the llm_input"""


class PreferenceExample(TypedDict, total=False):
    chosen: Required[str]
    """The chosen output in corresponding to the llm_input."""

    llm_input: Required[str]
    """The input to LLM"""

    rejected: Required[str]
    """The rejected output in corresponding to the llm_input."""
