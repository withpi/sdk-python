# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.question import Question

__all__ = ["ScoringSystemListJobsResponse", "ScoringSystemListJobsResponseItem"]


class ScoringSystemListJobsResponseItem(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    scoring_spec: Optional[List[Question]] = None
    """The generated scoring spec"""


ScoringSystemListJobsResponse: TypeAlias = List[ScoringSystemListJobsResponseItem]
