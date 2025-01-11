# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Contract"]


class Contract(BaseModel):
    description: str
    """The description of the contract"""

    name: str
    """The name of the contract"""

    dimensions: Optional[List["Dimension"]] = None
    """The dimensions of the contract"""


from .dimension import Dimension

if PYDANTIC_V2:
    Contract.model_rebuild()
else:
    Contract.update_forward_refs()  # type: ignore
