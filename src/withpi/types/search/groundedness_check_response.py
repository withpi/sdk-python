# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["GroundednessCheckResponse", "Hallucination"]


class Hallucination(BaseModel):
    explanation: str

    output_text: str


class GroundednessCheckResponse(BaseModel):
    hallucinations: List[Hallucination]

    score: float
