# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .sdk_dimension_param import SDKDimensionParam

__all__ = ["SDKContractParam"]


class SDKContractParamTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""

    dimensions: Iterable[SDKDimensionParam]
    """The dimensions of the contract"""


SDKContractParam: TypeAlias = Union[SDKContractParamTyped, Dict[str, object]]
