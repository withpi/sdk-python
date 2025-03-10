# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ScorerScoreResponse", "DimensionScores"]


class DimensionScores(BaseModel):
    subdimension_scores: Dict[str, float]
    """The score components for each subdimension"""

    total_score: float
    """The total score of the dimension"""


class ScorerScoreResponse(BaseModel):
    dimension_scores: Dict[str, DimensionScores]
    """The score components for each dimension"""

    total_score: float
    """The total score of the scoring system"""
