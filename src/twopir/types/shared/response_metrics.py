# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ResponseMetrics"]


class ResponseMetrics(BaseModel):
    cost: float
    """Cost in USD of this operation"""

    latency: float
    """Latency in milliseconds of this scoring"""

    scores: Dict[str, float]
    """Scores associated with this operation"""
