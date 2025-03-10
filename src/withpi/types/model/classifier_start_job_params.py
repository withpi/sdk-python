# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClassifierStartJobParams", "Example"]


class ClassifierStartJobParams(TypedDict, total=False):
    base_model: Required[Literal["MODERNBERT_BASE", "MODERNBERT_LARGE"]]
    """The base model to start the classification tuning process"""

    examples: Required[Iterable[Example]]
    """Examples to use in the classification tuning process"""

    learning_rate: float
    """Classification learning rate"""

    num_train_epochs: int
    """Classification number of train epochs"""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""
