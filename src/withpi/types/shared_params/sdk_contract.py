# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .sdk_dimension import SDKDimension

__all__ = ["SDKContract"]


class SDKContractTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""

    dimensions: Iterable[SDKDimension]
    """The dimensions of the contract"""


SDKContract: TypeAlias = Union[SDKContractTyped, Dict[str, object]]
