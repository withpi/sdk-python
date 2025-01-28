# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.contract import Contract

__all__ = ["ContractCalibrationStatus"]


class ContractCalibrationStatus(BaseModel):
    calibrated_contract: Optional[Contract] = None
    """The calibrated contract"""

    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""
