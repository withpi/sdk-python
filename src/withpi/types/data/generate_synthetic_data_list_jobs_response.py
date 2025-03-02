# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.synthetic_data_status import SyntheticDataStatus

__all__ = ["GenerateSyntheticDataListJobsResponse"]

GenerateSyntheticDataListJobsResponse: TypeAlias = List[SyntheticDataStatus]
