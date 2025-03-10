# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.sdk_example import SDKExample

__all__ = ["OptimizeStartJobParams", "Scorer", "ScorerDimension", "ScorerDimensionSubDimension"]


class OptimizeStartJobParams(TypedDict, total=False):
    examples: Required[Iterable[SDKExample]]
    """The examples to train and validate on"""

    initial_system_instruction: Required[str]
    """The initial system instruction"""

    model_id: Required[Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"]]
    """The model to use for generating responses"""

    scorer: Required[Scorer]
    """The contract to optimize"""

    tuning_algorithm: Required[Literal["PI", "DSPY"]]
    """The tuning algorithm to use"""

    dspy_optimization_type: Optional[Literal["BOOTSTRAP_FEW_SHOT", "COPRO", "MIPROv2"]]
    """The DSPY teleprompter/optimizer to use.

    This only applies for the DSPY. Leave it as None if tuning_algorithm != DSPY.
    """

    use_chain_of_thought: bool
    """Decides if to use chain of thought or not.

    This only applies for the DSPY. Leave it as None if tuning_algorithm != DSPY.
    """


class ScorerDimensionSubDimensionTyped(TypedDict, total=False):
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


ScorerDimensionSubDimension: TypeAlias = Union[ScorerDimensionSubDimensionTyped, Dict[str, object]]


class ScorerDimensionTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    sub_dimensions: Required[Iterable[ScorerDimensionSubDimension]]
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


ScorerDimension: TypeAlias = Union[ScorerDimensionTyped, Dict[str, object]]


class ScorerTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[ScorerDimension]
    """The dimensions of the scoring system"""


Scorer: TypeAlias = Union[ScorerTyped, Dict[str, object]]
