# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GroundednessCheckResponse", "Hallucination"]


class Hallucination(BaseModel):
    claim: str
    """What claim is being made in the text that is incorrect"""

    explanation: str
    """Explanation regarding why the claim is incorrect"""

    hallucination_type: Literal[
        "Evident conflict",
        "Subtle conflict",
        "Evident introduction of baseless information",
        "Subtle introduction of baseless information",
    ]

    output_text: str
    """
    A quote of the answer or output text that is not supported by the context
    (select the minimal text that is hallucinated)
    """

    reasoning: str
    """The reasoning for the hallucination"""


class GroundednessCheckResponse(BaseModel):
    hallucinations: List[Hallucination]

    score: float
