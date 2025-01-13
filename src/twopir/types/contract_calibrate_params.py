# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContractCalibrateParams", "Example"]


class ContractCalibrateParams(TypedDict, total=False):
    contract: Required["Contract"]
    """The contract to calibrate"""

    examples: Required[Iterable[Example]]
    """Rated examples to use when calibrating the contract"""


class Example(TypedDict, total=False):
    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Required[Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]]
    """The rating of the llm_output given the llm_input"""


from .shared_params.contract import Contract
