# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ContractScoreResponse"]


class ContractScoreResponse(BaseModel):
    scores: Dict[str, float]
    """The score components for each dimension"""

    total_score: float
    """The total score of the contract"""

    weights: Dict[str, float]
    """Map of score names to their weights in the overall score"""
