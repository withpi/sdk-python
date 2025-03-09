# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .calibration_status import CalibrationStatus

__all__ = ["CalibrateListResponse"]

CalibrateListResponse: TypeAlias = List[CalibrationStatus]
