# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["QueryGenerateFanoutsResponse", "QueryGenerateFanoutsResponseItem"]


class QueryGenerateFanoutsResponseItem(BaseModel):
    fanout_queries: List[str]
    """The list of fanout queries generated from the input"""

    query: str
    """The input query to generate fanouts from."""


QueryGenerateFanoutsResponse: TypeAlias = List[QueryGenerateFanoutsResponseItem]
