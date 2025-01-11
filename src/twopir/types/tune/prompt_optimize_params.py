# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptOptimizeParams", "Example"]


class PromptOptimizeParams(TypedDict, total=False):
    contract: Required["Contract"]
    """The contract to optimize"""

    examples: Required[Iterable[Example]]
    """The examples to train and validate on"""

    initial_system_instruction: Required[str]
    """The initial system instruction"""

    model_id: Required[Literal["gpt-4o-mini", "mock-llm"]]
    """The model to use for generating responses"""

    tuning_algorithm: Required[Literal["PI", "DSPY"]]
    """The tuning algorithm to use"""


class Example(TypedDict, total=False):
    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Optional[Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]
    """The rating of the llm_output given the llm_input"""


from ..shared_params.contract import Contract
