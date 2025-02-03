# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SftStatus", "HostedFireworkModel"]


class HostedFireworkModel(BaseModel):
    contract_score: float
    """The contract score of the evaluation set"""

    epoch: float
    """The training epoch"""

    eval_loss: float
    """The evaluation loss"""

    hosted_model_id: str
    """Firework's hosted model id"""

    step: int
    """The training step"""


class SftStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""

    hosted_firework_models: Optional[List[HostedFireworkModel]] = None
    """A list of hosted Firework models"""
