# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.question import Question

__all__ = ["GenerateRetrieveResponse"]


class GenerateRetrieveResponse(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    scoring_spec: Optional[List[Question]] = None
    """The generated scoring spec"""

    threshold: Optional[float] = None
    """Threshold to use to separate 0 and 1 labels in the case of classification."""
