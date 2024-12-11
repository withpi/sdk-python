# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""

    scoring_type: Literal["LLM_AS_A_JUDGE", "HUGGINGFACE_SCORER", "PYTHON_CODE"]
    """The type of scoring performed for this dimension"""

    huggingface_url: Optional[str] = None
    """
    The URL of the HuggingFace model to use for scoring. Only relevant for
    scoring_type of hugingface_scorer
    """

    parameters: Optional[List[float]] = None
    """The learned parameters for the scoring method.

    For llm_as_a_judge type, this corresponds to the values assigned to each Likert
    point from 1-5, normalized to a 0-1 range.
    """

    python_code: Optional[str] = None
    """The PYTHON code associated the python_code DimensionScoringType."""

    weight: Optional[float] = None
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """
