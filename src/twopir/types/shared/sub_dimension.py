# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    id: str
    """The label of the dimension"""

    description: str
    """The description of the dimension"""

    scoring_type: Literal["llm_as_a_judge"]
    """The type of scoring performed for this dimension"""
