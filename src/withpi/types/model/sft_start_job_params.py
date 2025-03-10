# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .rl.lora_config_param import LoraConfigParam
from ..data.sdk_example_param import SDKExampleParam
from ..shared_params.sdk_contract import SDKContract
from .rl.text_generation_base_model import TextGenerationBaseModel

__all__ = ["SftStartJobParams"]


class SftStartJobParams(TypedDict, total=False):
    examples: Required[Iterable[SDKExampleParam]]
    """Examples to use in the SFT tuning process.

    We split this data into train/eval 90/10.
    """

    scoring_system: Required[SDKContract]
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
