# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.question import Question

__all__ = ["GenerateRetrieveResponse"]


class GenerateRetrieveResponse(BaseModel):
    detailed_status: List[str]
    """Detailed status of the job"""

    job_id: str
    """The job id"""

    state: Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
    """Current state of the job"""

    balanced_accuracy: Optional[float] = None
    """
    Weighted combination fo average accuracy per class for the labeled data and
    overall accuracy for preference data.
    """

    f1: Optional[float] = None
    """F1 for the labeled data."""

    num_labeled_examples_used: Optional[int] = None
    """Number of labeled examples used for spec generation."""

    num_preference_examples_used: Optional[int] = None
    """Number of preference examples used for spec generation."""

    precision: Optional[float] = None
    """Precision for the labeled data."""

    recall: Optional[float] = None
    """Recall for the labeled data."""

    scoring_spec: Optional[List[Question]] = None
    """The generated scoring spec"""

    threshold: Optional[float] = None
    """Threshold to use to separate 0 and 1 labels in the case of classification."""
