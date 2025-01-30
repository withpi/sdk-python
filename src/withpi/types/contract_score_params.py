# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract

__all__ = ["ContractScoreParams"]


class ContractScoreParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to score"""

    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""
