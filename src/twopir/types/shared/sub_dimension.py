# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    scoring_type: Literal["PI_SCORER", "HUGGINGFACE_SCORER", "PYTHON_CODE"]
    """The type of scoring performed for this dimension"""

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

    huggingface_url: Optional[str] = None
    """
    The URL of the HuggingFace model to use for scoring. Only relevant for
    scoring_type of HUGGINGFACE_SCORER
    """

    parameters: Optional[List[float]] = None
    """The learned parameters for the scoring method.

    For PI_SCORER type, this corresponds to the values assigned to each Likert point
    from 1-5, normalized to a 0-1 range.
    """

    python_code: Optional[str] = None
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""

    weight: Optional[float] = None
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """


if PYDANTIC_V2:
    SubDimension.model_rebuild()
else:
    SubDimension.update_forward_refs()  # type: ignore
