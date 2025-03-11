# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.scoring_spec import ScoringSpec

__all__ = ["GrpoStartJobParams", "Example", "LoraConfig"]


class GrpoStartJobParams(TypedDict, total=False):
    base_rl_model: Required[Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"]]
    """The base model to start the RL tunning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    learning_rate: Required[float]
    """GRPO learning rate"""

    lora_config: Required[LoraConfig]
    """The LoRA configuration."""

    num_train_epochs: Required[int]
    """GRPO number of train epochs"""

    scoring_spec: Required[ScoringSpec]
    """The scoring spec to use in the GRPO tuning process"""

    system_prompt: Required[Optional[str]]
    """A custom system prompt to use during the RL tuning process"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input prompt to LLM for the RL training process"""


class LoraConfig(TypedDict, total=False):
    lora_rank: Literal["R_16", "R_32", "R_64"]
    """The number of dimensions in the low-rank decomposition of the weight updates."""
