# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InputClusterParams", "Body"]


class InputClusterParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    identifier: Required[str]
    """The identifier of the input"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""
