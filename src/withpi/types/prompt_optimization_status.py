# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromptOptimizationStatus"]


class PromptOptimizationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    optimized_prompt_messages: List[Dict[str, str]]
    """
    The optimized prompt messages in the OpenAI message format with the jinja
    {{ input }} variable for the next user prompt
    """

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR"]
    """Current state of the job"""
