# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GenerateFromSeedGenerateParams"]


class GenerateFromSeedGenerateParams(TypedDict, total=False):
    contract_description: Required[str]
    """The application description to generate contract for."""

    num_inputs: Required[int]
    """The number of LLM inputs to generate"""

    seeds: Required[List[str]]
    """The list of LLM inputs to be used as seeds"""
