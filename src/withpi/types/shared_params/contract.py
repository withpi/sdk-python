# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .dimension import Dimension

__all__ = ["Contract"]


class ContractTyped(TypedDict, total=False):
    description: Required[str]
    """The description of the contract"""

    name: Required[str]
    """The name of the contract"""

    dimensions: Iterable[Dimension]
    """The dimensions of the contract"""


Contract: TypeAlias = Union[ContractTyped, Dict[str, object]]
