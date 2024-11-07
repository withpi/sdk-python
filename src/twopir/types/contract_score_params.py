# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["ContractScoreParams", "Contract"]


class ContractScoreParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to score"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""


class Contract(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""
