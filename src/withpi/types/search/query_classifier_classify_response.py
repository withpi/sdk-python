# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.query_classifier_result import QueryClassifierResult

__all__ = ["QueryClassifierClassifyResponse"]


class QueryClassifierClassifyResponse(BaseModel):
    results: List[QueryClassifierResult]
