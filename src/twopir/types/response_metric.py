# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ResponseMetric", "Score"]


class Score(BaseModel):
    name: str
    """Name of the score in this object"""

    score: float
    """The score"""


class ResponseMetric(BaseModel):
    cost: float
    """Cost in USD of this operation"""

    latency: float
    """Latency in milliseconds of this scoring"""

    scores: List[Score]
    """List of scores associated with this operation"""
