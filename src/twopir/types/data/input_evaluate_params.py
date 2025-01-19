# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["InputEvaluateParams"]


class InputEvaluateParams(TypedDict, total=False):
    contract_description: Required[str]
    """The application contract's description"""

    llm_inputs: Required[List[str]]
    """The inputs to evaluate"""
