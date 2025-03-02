# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.example import Example
from .contracts.state import State

__all__ = ["DataListQuestionAnswerJobsResponse", "DataListQuestionAnswerJobsResponseItem"]


class DataListQuestionAnswerJobsResponseItem(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: State
    """Current state of the job"""

    data: Optional[List[Example]] = None
    """The generated synthetic data.

    Can be present even if the state is not done/error as it is streamed.
    """


DataListQuestionAnswerJobsResponse: TypeAlias = List[DataListQuestionAnswerJobsResponseItem]
