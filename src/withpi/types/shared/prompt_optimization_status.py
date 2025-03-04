# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .state import State
from ..._models import BaseModel

__all__ = ["PromptOptimizationStatus"]


class PromptOptimizationStatus(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    optimized_prompt_messages: Optional[List[Dict[str, str]]] = None
    """
    The optimized prompt messages in the OpenAI message format with the jinja
    {{ input }} variable for the next user prompt
    """
