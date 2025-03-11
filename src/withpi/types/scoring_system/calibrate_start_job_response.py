# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.scoring_spec import ScoringSpec

__all__ = ["CalibrateStartJobResponse"]


class CalibrateStartJobResponse(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    calibrated_scoring_spec: Optional[ScoringSpec] = None
    """The calibrated scoring spec"""
