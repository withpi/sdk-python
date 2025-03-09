# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .synthetic_data_status import SyntheticDataStatus

__all__ = ["GenerateSyntheticDataListResponse"]

GenerateSyntheticDataListResponse: TypeAlias = List[SyntheticDataStatus]
