# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...shared_params.contract import Contract

__all__ = ["GrpoStartJobParams", "Example", "LoraConfig"]


class GrpoStartJobParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to use in the GRPO tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    base_rl_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"]
    """The base model to start the RL tunning process"""

    learning_rate: float
    """SFT learning rate"""

    lora_config: LoraConfig
    """The LoRA configuration."""

    num_train_epochs: int
    """SFT number of train epochs"""

    system_prompt: Optional[str]
    """A custom system prompt to use during the RL tuning process"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input prompt to LLM for the RL training process"""


class LoraConfig(TypedDict, total=False):
    lora_rank: Literal["R_16", "R_32", "R_64"]
    """The number of dimensions in the low-rank decomposition of the weight updates."""
