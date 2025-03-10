# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .lora_config_param import LoraConfigParam
from .text_generation_base_model import TextGenerationBaseModel
from ...shared_params.sdk_contract import SDKContract

__all__ = ["GrpoStartJobParams", "Example"]


class GrpoStartJobParams(TypedDict, total=False):
    base_rl_model: Required[TextGenerationBaseModel]
    """The base model to start the RL tunning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    learning_rate: Required[float]
    """GRPO learning rate"""

    lora_config: Required[LoraConfigParam]
    """The LoRA configuration."""

    num_train_epochs: Required[int]
    """GRPO number of train epochs"""

    scoring_system: Required[SDKContract]
    """The scoring system to use in the GRPO tuning process"""

    system_prompt: Required[Optional[str]]
    """A custom system prompt to use during the RL tuning process"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input prompt to LLM for the RL training process"""
