# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["OptimizationStatus"]


class OptimizationStatus(BaseModel):
    contract: Optional["Contract"] = None
    """The optimized contract. Absent unless state is done"""

    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["queued", "running", "done", "error"]
    """Current state of the job"""


from .shared.contract import Contract

if PYDANTIC_V2:
    OptimizationStatus.model_rebuild()
else:
    OptimizationStatus.update_forward_refs()  # type: ignore
