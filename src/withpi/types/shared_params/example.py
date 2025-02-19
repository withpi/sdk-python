# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Example"]


class Example(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""
