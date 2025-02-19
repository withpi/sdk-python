# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.example import Example
from .shared_params.contract import Contract

__all__ = ["PromptOptimizeParams"]


class PromptOptimizeParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to optimize"""

    examples: Required[Iterable[Example]]
    """The examples to train and validate on"""

    initial_system_instruction: Required[str]
    """The initial system instruction"""

    model_id: Required[Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"]]
    """The model to use for generating responses"""

    tuning_algorithm: Required[Literal["PI", "DSPY"]]
    """The tuning algorithm to use"""

    dspy_optimization_type: Optional[Literal["BOOTSTRAP_FEW_SHOT", "COPRO", "MIPROv2"]]
    """The DSPY teleprompter/optimizer to use.

    This only applies for the DSPY. Leave it as None if tuning_algorithm != DSPY.
    """

    use_chain_of_thought: bool
    """Decides if to use chain of thought or not.

    This only applies for the DSPY. Leave it as None if tuning_algorithm != DSPY.
    """
