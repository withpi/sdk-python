# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.sdk_example import SDKExample

__all__ = ["SftStartJobParams", "ScoringSpec", "ScoringSpecDimension", "ScoringSpecDimensionSubDimension", "LoraConfig"]


class SftStartJobParams(TypedDict, total=False):
    examples: Required[Iterable[SDKExample]]
    """Examples to use in the SFT tuning process.

    We split this data into train/eval 90/10.
    """

    scoring_spec: Required[ScoringSpec]
    """The scoring spec to use in the SFT tuning process"""

    base_sft_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"]
    """The base model to start the SFT tuning process."""

    learning_rate: float
    """SFT learning rate"""

    lora_config: LoraConfig
    """The LoRA configuration."""

    num_train_epochs: int
    """SFT number of train epochs: <= 10."""

    system_prompt: Optional[str]
    """A custom system prompt to use during the RL tuning process"""


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


class LoraConfig(TypedDict, total=False):
    lora_rank: Literal["R_16", "R_32", "R_64"]
    """The number of dimensions in the low-rank decomposition of the weight updates."""
