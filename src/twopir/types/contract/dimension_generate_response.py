# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["DimensionGenerateResponse", "SubDimension"]


class SubDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""


class DimensionGenerateResponse(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    sub_dimensions: List[SubDimension]
    """The sub dimensions of the dimension"""
