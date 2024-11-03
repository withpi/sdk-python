# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperimentStatus"]


class ExperimentStatus(BaseModel):
    job_id: int
    """The unique identifier of this job"""

    state: Literal["running", "done", "error"]
    """Current statue of the prompt optimization job"""
