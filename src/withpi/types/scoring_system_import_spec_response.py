# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .shared.question import Question
from .shared.scoring_spec import ScoringSpec

__all__ = ["ScoringSystemImportSpecResponse"]

ScoringSystemImportSpecResponse: TypeAlias = Union[List[Question], ScoringSpec]
