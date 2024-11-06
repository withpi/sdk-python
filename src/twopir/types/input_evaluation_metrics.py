# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["InputEvaluationMetrics"]


class InputEvaluationMetrics(BaseModel):
    filter_score: float
    """The 0-1 score, with 1 meaning 'filter'"""

    scores: Dict[str, float]
    """Scores associated with this operation"""

    weights: Dict[str, float]
    """Map of filter_score name to its weight in the overall score"""
