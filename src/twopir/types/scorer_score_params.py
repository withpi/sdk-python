# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

from .contract_param import ContractParam
from .llm_response_param import LlmResponseParam

__all__ = ["ScorerScoreParams"]


class ScorerScoreParams(TypedDict, total=False):
    contract: Required[ContractParam]
    """A collection of dimensions an LLM response must adhere to"""

    llm_input: Required[Dict[str, Union[str, float]]]
    """Key/Value pairs constituting the input.

    If the input is just text, use the key "query"
    """

    llm_response: Required[LlmResponseParam]
    """The response from the LLM"""
