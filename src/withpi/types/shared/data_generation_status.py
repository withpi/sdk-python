# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .state import State
from ..._models import BaseModel

__all__ = ["DataGenerationStatus"]


class DataGenerationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    data: Optional[List[str]] = None
    """The generated data.

    Can be present even if the state is not done/error as it is streamed.
    """
