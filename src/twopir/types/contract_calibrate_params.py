# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .response_param import ResponseParam
from .shared_params.contract import Contract

__all__ = ["ContractCalibrateParams", "Feedback"]


class ContractCalibrateParams(TypedDict, total=False):
    contract: Required[Contract]
    """A collection of dimensions an LLM response must adhere to"""

    feedbacks: Required[Iterable[Feedback]]
    """The list of Feedbacks to use for calibration"""


class Feedback(TypedDict, total=False):
    labels: Required[Dict[str, float]]
    """The human-applied labels associated with the example"""

    llm_input: Required[Dict[str, Union[str, float]]]
    """Key/Value pairs constituting the input.

    If the input is just text, use the key "query"
    """

    llm_response: Required[ResponseParam]
    """The response from the LLM"""

    scores: Required[Dict[str, float]]
    """Previous scores associated with the example"""
