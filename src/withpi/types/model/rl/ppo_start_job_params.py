# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...shared_params.contract import Contract

__all__ = ["PpoStartJobParams", "Example"]


class PpoStartJobParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to use in the SFT tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the RL tuning process"""

    model: Required[str]
    """The Huggingface model name to run RL on.

    Currently we only support the LLAMA model type and model size <= 8B parameters.
    """

    learning_rate: float
    """SFT learning rate"""

    num_train_epochs: int
    """SFT number of train epochs"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""
