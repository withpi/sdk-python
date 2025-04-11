# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ScoringSystemMetrics", "DimensionScores"]


class DimensionScores(BaseModel):
    subdimension_scores: Dict[str, float]
    """The score components for each subdimension"""

    total_score: float
    """The total score of the dimension"""


class ScoringSystemMetrics(BaseModel):
    dimension_scores: Dict[str, DimensionScores]
    """The score components for each dimension"""

    question_scores: Dict[str, float]
    """The score components for each question"""

    total_score: float
    """The total score of the scoring spec"""
