# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["PromptOptimizationStatus"]


class PromptOptimizationStatus(BaseModel):
    job_id: int
    """The unique identifier of this job"""

    state: Literal["running", "done", "error"]
    """Current statue of the prompt optimization job"""

    contract: Optional["Contract"] = None
    """The optimized contract. Absent unless state is 'done'"""


from .shared.contract import Contract

if PYDANTIC_V2:
    PromptOptimizationStatus.model_rebuild()
else:
    PromptOptimizationStatus.update_forward_refs()  # type: ignore
