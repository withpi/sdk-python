# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["InputEvaluationMetrics"]


class InputEvaluationMetrics(BaseModel):
    filter_score: float
    """The 0-1 score with 1 meaning filter"""

    scores: Dict[str, float]
    """The score components for each dimension"""

    weights: Dict[str, float]
    """Map of score names to their weights in the overall score"""
