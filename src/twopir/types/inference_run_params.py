# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InferenceRunParams", "LlmInput"]


class InferenceRunParams(TypedDict, total=False):
    llm_input: Required[LlmInput]


class LlmInput(TypedDict, total=False):
    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to run inference on"""

    model_id: Required[Literal["gpt_4o_mini_agent", "mock_agent"]]
    """The model to use for generating responses"""
