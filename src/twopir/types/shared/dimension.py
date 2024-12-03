# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .sub_dimension import SubDimension

__all__ = ["Dimension"]


class Dimension(BaseModel):
    id: str
    """The label of the dimension"""

    description: str
    """The description of the dimension"""

    sub_dimensions: List[SubDimension]
    """The sub dimensions of the dimension"""

    weight: float
    """
    The weight of the dimension The sum of dimension weights will be normalized to
    one internally. A higher weight counts for more when aggregating this dimension
    is aggregated into the final score.
    """
