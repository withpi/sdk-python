# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .dimension_scoring_type import DimensionScoringType

__all__ = ["SDKActionDimension"]


class SDKActionDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    scoring_type: DimensionScoringType
    """The type of scoring performed for this dimension"""

    action_on_low_score: Optional[bool] = None
    """
    If `action_on_low_score = True`, the node emits the real value if action
    dimension score is <= 0.5 and it returns -1 otherwise.
    """

    custom_model_id: Optional[str] = None
    """
    The ID of the custom model to use for scoring. Only relevant for scoring_type of
    CUSTOM_MODEL_SCORER
    """

    python_code: Optional[str] = None
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""
