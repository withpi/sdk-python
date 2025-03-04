# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .state import State
from ..._models import BaseModel
from .trained_model import TrainedModel

__all__ = ["SftStatus"]


class SftStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    trained_models: Optional[List[TrainedModel]] = None
    """A list of trained models selected based on the PI Contract score."""
