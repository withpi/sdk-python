# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ContractCalibrateParams", "Contract", "Feedback"]


class ContractCalibrateParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to calibrate"""

    feedbacks: Required[Iterable[Feedback]]
    """The feedbacks to use for calibration"""


class Contract(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""


class Feedback(TypedDict, total=False):
    labels: Required[Dict[str, str]]
    """The labels for each dimension"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""

    scores: Required[Dict[str, float]]
    """The scores for each dimension"""
