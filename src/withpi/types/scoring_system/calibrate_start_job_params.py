# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params import scoring_spec as _scoring_spec
from ..shared_params.question import Question

__all__ = ["CalibrateStartJobParams", "ScoringSpec", "Example", "PreferenceExample"]


class CalibrateStartJobParams(TypedDict, total=False):
    scoring_spec: Required[ScoringSpec]
    """Either a scoring spec or a list of questions to score"""

    examples: Optional[Iterable[Example]]
    """Rated examples to use when calibrating the scoring spec.

    Must specify either the examples or the preference examples
    """

    preference_examples: Optional[Iterable[PreferenceExample]]
    """Preference examples to use when calibrating the scoring spec.

    Must specify either the examples or preference examples
    """

    strategy: Literal["LITE", "FULL"]
    """The strategy to use to calibrate the scoring spec.

    FULL would take longer than LITE but may result in better result.
    """


ScoringSpec: TypeAlias = Union[Iterable[Question], _scoring_spec.ScoringSpec]


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Required[Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]
    """The rating of the llm_output given the llm_input"""


class PreferenceExample(TypedDict, total=False):
    chosen: Required[str]
    """The chosen output in corresponding to the llm_input."""

    llm_input: Required[str]
    """The input to LLM"""

    rejected: Required[str]
    """The rejected output in corresponding to the llm_input."""
