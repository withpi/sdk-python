# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperimentStatus"]


class ExperimentStatus(BaseModel):
    job_id: int
    """The job id"""

    state: Literal["running", "done", "error"]
    """Current state of the job"""
