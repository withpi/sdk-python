# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..contracts.state import State
from ..shared.scoring_system import ScoringSystem

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
