# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.contract import Contract

__all__ = ["CalibrateStartJobParams", "Example", "PreferenceExample"]


class CalibrateStartJobParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to calibrate"""

    examples: Required[Iterable[Example]]
    """Rated examples to use when calibrating the contract"""

    preference_examples: Iterable[PreferenceExample]
    """Preference examples to use when calibrating the contract"""

    strategy: Literal["LITE", "FULL"]
    """The strategy to use to calibrate the contract.

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
