# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataGenerationStatus"]


class DataGenerationStatus(BaseModel):
    job_id: int
    """The unique identifier of this job"""

    state: Literal["running", "done", "error"]
    """Current status of the job"""

    data: Optional[List[str]] = None
    """The generated data. Absent unless state is 'done'"""
