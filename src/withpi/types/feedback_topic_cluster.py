# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FeedbackTopicCluster"]


class FeedbackTopicCluster(BaseModel):
    feedback: List[str]
    """The feedback IDs assigned to this topic"""

    per_source_counts: Dict[str, int]
    """The counts of feedback per source"""

    rating: Literal["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
    """The rating of the feedback in this cluster"""

    topic: str
    """The topic of the feedback in this cluster"""
