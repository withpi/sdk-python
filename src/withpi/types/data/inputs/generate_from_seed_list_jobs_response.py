# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...shared.data_generation_status import DataGenerationStatus

__all__ = ["GenerateFromSeedListJobsResponse"]

GenerateFromSeedListJobsResponse: TypeAlias = List[DataGenerationStatus]
