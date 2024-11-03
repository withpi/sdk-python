# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Contract"]


class Contract(BaseModel):
    description: str
    """The full description of the contract, which may be the system prompt."""

    dimensions: List["Dimension"]
    """The dimensions associated with this contract"""

    name: str
    """The human-readable name for the contract"""


from .dimension import Dimension

if PYDANTIC_V2:
    Contract.model_rebuild()
else:
    Contract.update_forward_refs()  # type: ignore
