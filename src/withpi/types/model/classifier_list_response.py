# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .classification_status import ClassificationStatus

__all__ = ["ClassifierListResponse"]

ClassifierListResponse: TypeAlias = List[ClassificationStatus]
