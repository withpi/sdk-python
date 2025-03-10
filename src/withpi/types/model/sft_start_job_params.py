# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .rl.lora_config_param import LoraConfigParam
from ..shared_params.sdk_example import SDKExample
from .rl.text_generation_base_model import TextGenerationBaseModel

__all__ = ["SftStartJobParams", "Scorer", "ScorerDimension", "ScorerDimensionSubDimension"]


class SftStartJobParams(TypedDict, total=False):
    examples: Required[Iterable[SDKExample]]
    """Examples to use in the SFT tuning process.

    We split this data into train/eval 90/10.
    """

    scorer: Required[Scorer]
    """The scoring system to use in the SFT tuning process"""

    base_sft_model: TextGenerationBaseModel
    """The base model to start the SFT tuning process."""

    learning_rate: float
    """SFT learning rate"""

    lora_config: LoraConfigParam
    """The LoRA configuration."""

    num_train_epochs: int
    """SFT number of train epochs: <= 10."""

    system_prompt: Optional[str]
    """A custom system prompt to use during the RL tuning process"""


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
