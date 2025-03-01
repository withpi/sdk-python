# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.query_fanout_example import QueryFanoutExample

__all__ = ["QueryGenerateFanoutsResponse"]

QueryGenerateFanoutsResponse: TypeAlias = List[QueryFanoutExample]
