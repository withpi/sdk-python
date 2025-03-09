# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .data_generation_status import DataGenerationStatus

__all__ = ["GenerateFromSeedListResponse"]

GenerateFromSeedListResponse: TypeAlias = List[DataGenerationStatus]
