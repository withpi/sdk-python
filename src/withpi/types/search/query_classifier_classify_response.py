# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["QueryClassifierClassifyResponse", "Result", "ResultProbability"]


class ResultProbability(BaseModel):
    label: str

    score: float


class Result(BaseModel):
    prediction: str

    probabilities: List[ResultProbability]

    query: str


class QueryClassifierClassifyResponse(BaseModel):
    results: List[Result]
