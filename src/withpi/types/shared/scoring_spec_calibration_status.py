# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .question import Question
from ..._models import BaseModel

__all__ = ["ScoringSpecCalibrationStatus"]


class ScoringSpecCalibrationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    calibrated_scoring_spec: Optional[List[Question]] = None
    """The calibrated scoring spec"""
