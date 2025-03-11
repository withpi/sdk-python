# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.scoring_spec import ScoringSpec

__all__ = ["CalibrateStartJobParams", "Example", "PreferenceExample"]


class CalibrateStartJobParams(TypedDict, total=False):
    scoring_spec: Required[ScoringSpec]
    """The scoring spec to calibrate"""

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
