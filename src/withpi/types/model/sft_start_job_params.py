# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.contract import Contract

__all__ = ["SftStartJobParams", "Example"]


class SftStartJobParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to use in the SFT tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the SFT tuning process"""

    base_sft_model: Literal["LLAMA_3.1_8B"]
    """The base model to start the SFT tuning process."""

    learning_rate: float
    """SFT learning rate"""

    num_train_epochs: int
    """SFT number of train epochs"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""
