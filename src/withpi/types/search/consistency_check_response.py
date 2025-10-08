# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ConsistencyCheckResponse", "Inconsistency"]


class Inconsistency(BaseModel):
    contradicts_text: str

    explanation: str

    output_id: str

    output_text: str


class ConsistencyCheckResponse(BaseModel):
    inconsistencies: List[Inconsistency]

    score: float
