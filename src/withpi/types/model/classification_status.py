# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .trained_model import TrainedModel
from ..contracts.state import State

__all__ = ["ClassificationStatus"]


class ClassificationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    trained_models: Optional[List[TrainedModel]] = None
    """A list of trained classification models."""
