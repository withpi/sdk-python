# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract

__all__ = ["ContractCalibrateParams", "Feedback"]


class ContractCalibrateParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to calibrate"""

    feedbacks: Required[Iterable[Feedback]]
    """The feedbacks to use for calibration"""


class Feedback(TypedDict, total=False):
    labels: Required[Dict[str, str]]
    """The labels for each dimension"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""

    scores: Required[Dict[str, float]]
    """The scores for each dimension"""
