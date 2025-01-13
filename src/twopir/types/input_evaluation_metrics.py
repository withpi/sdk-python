# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["InputEvaluationMetrics"]


class InputEvaluationMetrics(BaseModel):
    filter_scores: List[float]
    """The 0-1 scores mean the probability of being filtered"""
