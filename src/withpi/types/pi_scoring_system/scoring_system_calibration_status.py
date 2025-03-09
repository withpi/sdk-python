# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..scoring_system import ScoringSystem
from ..contracts.state import State

__all__ = ["ScoringSystemCalibrationStatus"]


class ScoringSystemCalibrationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    calibrated_scoring_system: Optional[ScoringSystem] = None
    """The calibrated scoring system"""
