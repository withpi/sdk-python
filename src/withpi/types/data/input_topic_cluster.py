# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["InputTopicCluster"]


class InputTopicCluster(BaseModel):
    inputs: List[str]
    """The input IDs assigned to this topic"""

    topic: str
    """The topic of the input in this cluster"""
