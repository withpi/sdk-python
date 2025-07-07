# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.question import Question

__all__ = ["ScoringSystemImportSpecResponse"]

ScoringSystemImportSpecResponse: TypeAlias = List[Question]
