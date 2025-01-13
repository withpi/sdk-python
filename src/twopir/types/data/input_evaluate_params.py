# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Required, TypedDict

__all__ = ["InputEvaluateParams"]


class InputEvaluateParams(TypedDict, total=False):
    contract: Required["Contract"]
    """The contract the input is intended to drive"""

    llm_inputs: Required[List[Union[str, Dict[str, str]]]]
    """The inputs to evaluate"""


from ..shared_params.contract import Contract
