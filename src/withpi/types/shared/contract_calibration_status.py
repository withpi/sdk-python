# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .contract import Contract
from ..._models import BaseModel
from ..contracts.state import State

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
