# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.trained_model import TrainedModel

__all__ = ["SftListResponse", "SftListResponseItem"]


class SftListResponseItem(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    trained_models: Optional[List[TrainedModel]] = None
    """A list of trained models selected based on the PI Contract score."""


SftListResponse: TypeAlias = List[SftListResponseItem]
