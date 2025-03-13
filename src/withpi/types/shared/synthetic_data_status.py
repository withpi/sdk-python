# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .example import Example
from ..._models import BaseModel

__all__ = ["SyntheticDataStatus"]


class SyntheticDataStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    data: Optional[List[Example]] = None
    """The generated synthetic data.

    Can be present even if the state is not done/error as it is streamed.
    """
