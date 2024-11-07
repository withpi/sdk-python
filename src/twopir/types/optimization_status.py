# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OptimizationStatus", "Contract"]


class Contract(BaseModel):
    description: str
    """The description of the contract"""

    name: str
    """The name of the contract"""


class OptimizationStatus(BaseModel):
    contract: Optional[Contract] = None
    """The optimized contract. Absent unless state is done"""

    job_id: int
    """The job id"""

    state: Literal["running", "done", "error"]
    """Current state of the job"""
