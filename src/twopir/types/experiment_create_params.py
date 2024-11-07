# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract

__all__ = ["ExperimentCreateParams", "Example"]


class ExperimentCreateParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to evaluate against"""

    examples: Required[Iterable[Example]]
    """The examples to evaluate"""

    scorer_id: Required[int]
    """The scorer id to use"""


class Example(TypedDict, total=False):
    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""
