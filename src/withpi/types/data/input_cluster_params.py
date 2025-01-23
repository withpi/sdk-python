# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InputClusterParams", "Input"]


class InputClusterParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]


class Input(TypedDict, total=False):
    identifier: Required[str]
    """The identifier of the input"""

    llm_input: Required[str]
    """The input to LLM"""
