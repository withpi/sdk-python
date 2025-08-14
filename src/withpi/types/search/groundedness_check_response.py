# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GroundednessCheckResponse", "Hallucination"]


class Hallucination(BaseModel):
    claim: str
    """What claim is being made in the text that is incorrect"""

    hallucination_type: Literal[
        "Evident conflict",
        "Subtle conflict",
        "Evident introduction of baseless information",
        "Subtle introduction of baseless information",
    ]

    reasoning: str
    """The reasoning for the hallucination"""

    text: str
    """
    A quote of the text that is not supported by the context (select the minimal
    text that is hallucinated)
    """

    why_incorrect: str
    """Why is the claim incorrect?"""


class GroundednessCheckResponse(BaseModel):
    hallucinations: List[Hallucination]

    score: float
