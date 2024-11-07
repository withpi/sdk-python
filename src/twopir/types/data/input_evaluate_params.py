# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

from ..shared_params.contract import Contract

__all__ = ["InputEvaluateParams"]


class InputEvaluateParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract the input is intended to drive"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""
