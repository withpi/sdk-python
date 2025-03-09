# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .scoring_system_calibration_status import ScoringSystemCalibrationStatus

__all__ = ["CalibrateListResponse"]

CalibrateListResponse: TypeAlias = List[ScoringSystemCalibrationStatus]
