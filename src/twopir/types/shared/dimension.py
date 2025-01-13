# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Dimension"]


class Dimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    sub_dimensions: List["SubDimension"]
    """The sub dimensions of the dimension"""

    action_dimension: Optional["SubDimension"] = None
    """If `action_dimension` is set, this node is a part of short-circuit subtree.

    If the score of the action_dimension is > 0.5, then evaluate the node and return
    the actual score. If it is <= 0.5 return -1. The higher level node will ignore
    the -1 scores and thus we achieve the short-circuit behavior.
    """

    action_on_low_score: Optional[bool] = None
    """
    If `action_on_low_score = True`, the node emits the real value if action
    dimension score is <= 0.5 and it returns -1 otherwise.
    """

    weight: Optional[float] = None
    """
    The weight of the dimension The sum of dimension weights will be normalized to
    one internally. A higher weight counts for more when aggregating this dimension
    is aggregated into the final score.
    """


from .sub_dimension import SubDimension

if PYDANTIC_V2:
    Dimension.model_rebuild()
else:
    Dimension.update_forward_refs()  # type: ignore
