# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataGenerationStatus"]


class DataGenerationStatus(BaseModel):
    data: Optional[List[str]] = None
    """The generated data. Absent unless state is done"""

    job_id: int
    """The job id"""

    state: Literal["running", "done", "error"]
    """Current state of the job"""
