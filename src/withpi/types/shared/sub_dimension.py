# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .dimension_scoring_type import DimensionScoringType

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    scoring_type: DimensionScoringType
    """The type of scoring performed for this dimension"""

    custom_model_id: Optional[str] = None
    """
    The ID of the custom model to use for scoring. Only relevant for scoring_type of
    CUSTOM_MODEL_SCORER
    """

    parameters: Optional[List[float]] = None
    """The learned parameters for the scoring method.

    This represents piecewise linear interpolation between [0, 1].
    """

    python_code: Optional[str] = None
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""

    weight: Optional[float] = None
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """
