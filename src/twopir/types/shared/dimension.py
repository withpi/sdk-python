# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .sub_dimension import SubDimension

__all__ = ["Dimension"]


class Dimension(BaseModel):
    id: str
    """The label of the dimension"""

    description: str
    """The description of the dimension"""

    scoring_type: Literal["llm_as_a_judge"]
    """The type of scoring performed for this dimension"""

    sub_dimensions: List[SubDimension]
    """The sub dimensions of the dimension"""
