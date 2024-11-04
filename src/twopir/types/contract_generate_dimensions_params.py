# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract

__all__ = ["ContractGenerateDimensionsParams"]


class ContractGenerateDimensionsParams(TypedDict, total=False):
    contract: Required[Contract]
    """A collection of dimensions an LLM response must adhere to"""
