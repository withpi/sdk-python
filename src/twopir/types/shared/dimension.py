# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Dimension"]


class Dimension(BaseModel):
    description: str
    """Human readable description of what the dimension is testing"""

    label: str
    """Human readable label for the dimension"""

    sub_dimension: Optional[List[Dimension]] = None
    """Nested dimensions to be tested as part of this one"""


if PYDANTIC_V2:
    Dimension.model_rebuild()
else:
    Dimension.update_forward_refs()  # type: ignore
