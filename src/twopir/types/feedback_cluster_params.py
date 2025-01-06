# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedbackClusterParams", "Feedback"]


class FeedbackClusterParams(TypedDict, total=False):
    feedbacks: Required[Iterable[Feedback]]


class Feedback(TypedDict, total=False):
    comment: Required[str]
    """The comment on the feedback"""

    identifier: Required[str]
    """The identifier of the feedback used to align responses"""

    llm_input: Required[Union[str, Dict[str, str]]]
    """The input to evaluate"""

    llm_output: Required[str]
    """The output to evaluate"""

    rating: Required[Literal["positive", "negative"]]
    """Structured text rating of this feedback."""

    sources: Optional[List[str]]
    """
    The source labels of the feedback. When computing cluster statistics, per-source
    statistics will be maintained.
    """
