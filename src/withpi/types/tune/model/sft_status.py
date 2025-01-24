# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SftStatus", "HostedFireworkModel"]


class HostedFireworkModel(BaseModel):
    api_model_id: str = FieldInfo(alias="model_id")
    """Firework's model id."""


class SftStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""

    hosted_firework_models: Optional[List[HostedFireworkModel]] = None
    """A list of hosted firework models"""
