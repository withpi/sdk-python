# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.scorer import Scorer

__all__ = ["CalibrateListResponse", "CalibrateListResponseItem"]


class CalibrateListResponseItem(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    calibrated_scoring_system: Optional[Scorer] = None
    """The calibrated scoring system"""


CalibrateListResponse: TypeAlias = List[CalibrateListResponseItem]
