# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["QueryClassifierClassifyParams", "Class", "Example"]


class QueryClassifierClassifyParams(TypedDict, total=False):
    classes: Required[Iterable[Class]]
    """The list of class definitions to classify the queries into. Must be <= 20."""

    queries: Required[SequenceNotStr[str]]
    """The list of queries to classify. Must be <= 10."""

    batch_size: int
    """Number of inputs to generate in one LLM call. Must be <=10."""

    examples: Optional[Iterable[Example]]
    """Optional list of examples to provide as few-shot examples for the classifier.

    Must be <= 20.
    """

    mode: Literal["generative", "probabilistic"]
    """The mode to use for the classification.

    The probabilistic mode returns probabilities for each class.
    """


class Class(TypedDict, total=False):
    description: Required[str]

    label: Required[str]


class Example(TypedDict, total=False):
    label: Required[str]

    text: Required[str]
