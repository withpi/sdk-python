# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.state import State
from ..shared.trained_model import TrainedModel

__all__ = ["ClassifierListResponse", "ClassifierListResponseItem"]


class ClassifierListResponseItem(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    trained_models: Optional[List[TrainedModel]] = None
    """A list of trained classification models."""


ClassifierListResponse: TypeAlias = List[ClassifierListResponseItem]
