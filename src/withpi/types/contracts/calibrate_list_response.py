# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.contract_calibration_status import ContractCalibrationStatus

__all__ = ["CalibrateListResponse"]

CalibrateListResponse: TypeAlias = List[ContractCalibrationStatus]
