# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    id: str
    """The label of the dimension"""

    description: str
    """The description of the dimension"""

    parameters: Optional[List[float]] = None
    """The learned parameters for the scoring method.

    For llm_as_a_judge type, this corresponds to the values assigned to each Likert
    point from 1-5, normalized to a 0-1 range.
    """

    scoring_method: Optional[Literal["twopir_judge"]] = None
    """The judge used for scoring this dimension (for llm_as_a_judge type)"""

    scoring_type: Literal["llm_as_a_judge"]
    """The type of scoring performed for this dimension"""

    weight: float
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """
