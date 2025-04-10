# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ScoringSystemScoreResponse"]


class ScoringSystemScoreResponse(BaseModel):
    dimension_scores: Dict[str, float]
    """The score components for each dimension"""

    total_score: float
    """The total score of the scoring spec"""
