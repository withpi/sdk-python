# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract
from .shared_params.llm_response import LlmResponse

__all__ = ["ExperimentCreateParams", "Example"]


class ExperimentCreateParams(TypedDict, total=False):
    contract: Required[Contract]
    """A collection of dimensions an LLM response must adhere to"""

    examples: Required[Iterable[Example]]
    """List of examples that should be scored"""

    scorer_id: Required[int]
    """The ID of the scorer to apply"""


class Example(TypedDict, total=False):
    llm_input: Required[Dict[str, Union[str, float]]]
    """Key/Value pairs constituting the input.

    If the input is just text, use the key "query"
    """

    llm_response: Required[LlmResponse]
    """The response from the LLM"""
