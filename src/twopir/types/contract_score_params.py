# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract
from .shared_params.llm_response import LlmResponse

__all__ = ["ContractScoreParams"]


class ContractScoreParams(TypedDict, total=False):
    contract: Required[Contract]
    """A collection of dimensions an LLM response must adhere to"""

    llm_input: Required[Dict[str, Union[str, float]]]
    """Key/Value pairs constituting the input.

    If the input is just text, use the key "query"
    """

    llm_response: Required[LlmResponse]
    """The response from the LLM"""
