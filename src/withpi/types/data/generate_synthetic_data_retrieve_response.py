# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.example import Example

__all__ = ["GenerateSyntheticDataRetrieveResponse"]


class GenerateSyntheticDataRetrieveResponse(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""

    data: Optional[List[Example]] = None
    """The generated synthetic data.

    Can be present even if the state is not done/error as it is streamed.
    """
