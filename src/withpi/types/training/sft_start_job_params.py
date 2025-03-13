# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.example import Example
from ..shared_params.scoring_spec import ScoringSpec

__all__ = ["SftStartJobParams", "LoraConfig"]


class SftStartJobParams(TypedDict, total=False):
    examples: Required[Iterable[Example]]
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


class LoraConfig(TypedDict, total=False):
    lora_rank: Literal["R_16", "R_32", "R_64"]
    """The number of dimensions in the low-rank decomposition of the weight updates."""
