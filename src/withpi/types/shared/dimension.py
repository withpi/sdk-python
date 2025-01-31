# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sub_dimension import SubDimension

__all__ = ["Dimension", "ActionDimension"]


class ActionDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    scoring_type: Literal["PI_SCORER", "HUGGINGFACE_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]
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

    huggingface_url: Optional[str] = None
    """
    The URL of the HuggingFace model to use for scoring. Only relevant for
    scoring_type of HUGGINGFACE_SCORER
    """

    python_code: Optional[str] = None
    """The PYTHON code associated the PYTHON_CODE DimensionScoringType."""


class Dimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    sub_dimensions: List[SubDimension]
    """The sub dimensions of the dimension"""

    action_dimension: Optional[ActionDimension] = None
    """If `action_dimension` is set, this node is a part of short-circuit subtree.

    If the score of the action_dimension is > 0.5, then evaluate the node and return
    the actual score. If it is <= 0.5 return -1. The higher level node will ignore
    the -1 scores and thus we achieve the short-circuit behavior.
    """

    parameters: Optional[List[float]] = None
    """The learned parameters for the scoring method.

    This represents piecewise linear interpolation between [0, 1].
    """

    weight: Optional[float] = None
    """
    The weight of the dimension The sum of dimension weights will be normalized to
    one internally. A higher weight counts for more when aggregating this dimension
    is aggregated into the final score.
    """
