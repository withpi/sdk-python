# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...shared_params.contract import Contract
from ...shared_params.lora_config import LoraConfig
from ...shared.finetuning_base_model import FinetuningBaseModel

__all__ = ["GrpoStartJobParams", "Example"]


class GrpoStartJobParams(TypedDict, total=False):
    base_rl_model: Required[FinetuningBaseModel]
    """The base model to start the RL tunning process"""

    contract: Required[Contract]
    """The contract to use in the GRPO tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    learning_rate: Required[float]
    """GRPO learning rate"""

    lora_config: Required[LoraConfig]
    """The LoRA configuration."""

    num_train_epochs: Required[int]
    """GRPO number of train epochs"""

    system_prompt: Required[Optional[str]]
    """A custom system prompt to use during the RL tuning process"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input prompt to LLM for the RL training process"""
