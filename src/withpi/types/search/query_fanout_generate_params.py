# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.query_fanout_example import QueryFanoutExample

__all__ = ["QueryFanoutGenerateParams"]


class QueryFanoutGenerateParams(TypedDict, total=False):
    query: Required[str]
    """The query to generate fanouts for"""

    few_shot_examples: Iterable[QueryFanoutExample]
    """The list of few-shot examples for the fanout generation.

    Only needed if the default fanouts are not working well.
    """

    num_fanout_queries: int
    """The number of fanout queries to generate"""
