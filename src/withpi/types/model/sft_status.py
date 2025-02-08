# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SftStatus", "TrainedModel"]


class TrainedModel(BaseModel):
    contract_score: float
    """The PI contract score of the eval set what isn't used in training"""

    epoch: float
    """The training epoch"""

    eval_loss: float
    """The evaluation loss"""

    firework_hosted_model_id: str
    """Firework's hosted model id"""

    step: int
    """The training step"""

    hf_model_name: Optional[str] = None
    """The SFT model weights in Huggingface"""


class SftStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""

    trained_models: Optional[List[TrainedModel]] = None
    """A list of trained models selected based on the PI Contract score."""
