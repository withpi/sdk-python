# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...shared_params.contract import Contract

__all__ = ["GrpoStartJobParams", "Example"]


class GrpoStartJobParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to use in the GRPO tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    model: Required[Literal["LLAMA_3.2_1B"]]
    """The model to start the RL process"""

    learning_rate: float
    """SFT learning rate"""

    num_train_epochs: int
    """SFT number of train epochs"""

    system_prompt: Optional[str]
    """A custom system prompt to use during the RL tuning process"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input prompt to LLM for the RL training process"""
