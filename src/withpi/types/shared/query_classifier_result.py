# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["QueryClassifierResult", "Probability"]


class Probability(BaseModel):
    label: str

    score: float


class QueryClassifierResult(BaseModel):
    prediction: str

    probabilities: List[Probability]

    query: str
