# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .state import State
from .contract import Contract
from ..._models import BaseModel

__all__ = ["ContractCalibrationStatus"]


class ContractCalibrationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    calibrated_contract: Optional[Contract] = None
    """The calibrated contract"""
