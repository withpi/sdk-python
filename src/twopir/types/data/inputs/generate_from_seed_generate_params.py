# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GenerateFromSeedGenerateParams", "Seeds"]


class GenerateFromSeedGenerateParams(TypedDict, total=False):
    seeds: Required[Seeds]


class Seeds(TypedDict, total=False):
    num_inputs: Required[int]
    """Number of LLM inputs to generate."""

    seeds: Required[List[str]]
    """The LLM inputs to be used as seeds to generate the additional LLM inputs"""
