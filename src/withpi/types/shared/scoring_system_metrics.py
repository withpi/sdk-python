# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ScoringSystemMetrics"]


class ScoringSystemMetrics(BaseModel):
    question_scores: Dict[str, float]
    """The score components for each question"""

    total_score: float
    """The total score of the scoring spec"""
