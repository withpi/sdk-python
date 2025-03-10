# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["QueryFanoutExample"]


class QueryFanoutExample(BaseModel):
    fanout_queries: List[str]
    """The list of fanout queries associated with the input"""

    query: str
    """The input query that the fanout queries are based on."""
