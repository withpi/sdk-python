# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["InputEvaluateParams", "Contract"]


class InputEvaluateParams(TypedDict, total=False):
    contract: Required[Contract]

    llm_input: Required[Union[str, Dict[str, str]]]


class Contract(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""
