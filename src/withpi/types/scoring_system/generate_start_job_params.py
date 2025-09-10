# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.question import Question

__all__ = ["GenerateStartJobParams", "Example", "PreferenceExample"]


class GenerateStartJobParams(TypedDict, total=False):
    application_description: Required[str]
    """The application description to generate a scoring spec for."""

    examples: Required[Iterable[Example]]
    """Rated examples to use for generating the discriminating questions.

    The scores can be class labels or actual scores (but must be between 0 and 1)
    """

    preference_examples: Required[Iterable[PreferenceExample]]
    """Preference examples to use for generating the discriminating questions.

    Must specify either the examples or preference examples
    """

    batch_size: int
    """Number of examples to use in one batch to generate the questions."""

    existing_questions: Iterable[Question]
    """
    Existing questions for the applications, these may or may not be retained in the
    output depending on their performance
    """

    num_questions: int
    """The number of questions that the generated scoring system should contain.

    If <= 0, then the number is auto selected.
    """

    retain_existing_questions: bool
    """If true, only generate new questions that improve the accuracy."""

    try_auto_generating_python_code: bool
    """If true, try to generate python code for the generated questions."""


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Optional[Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]
    """DEPRECATED: Instead fill the desired score to the 'score' field."""

    score: float
    """The target score of the example, between 0 and 1."""


class PreferenceExample(TypedDict, total=False):
    chosen: Required[str]
    """The chosen output in corresponding to the llm_input."""

    llm_input: Required[str]
    """The input to LLM"""

    rejected: Required[str]
    """The rejected output in corresponding to the llm_input."""
