# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.contract import Contract

__all__ = ["OptimizationStatus"]


class OptimizationStatus(BaseModel):
    contract: Optional[Contract] = None
    """The optimized contract. Absent unless state is done"""

    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["running", "done", "error"]
    """Current state of the job"""
