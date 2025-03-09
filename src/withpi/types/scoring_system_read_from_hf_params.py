# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScoringSystemReadFromHfParams"]


class ScoringSystemReadFromHfParams(TypedDict, total=False):
    hf_scoring_system_name: Required[str]
    """Huggingface scoring system name e.g.

    withpi/my_scoring_system. You need to provide the hf_token if the scoring system
    dataset is not public or not own by the withpi organization.
    """

    hf_token: Optional[str]
    """Huggingface token to use if you want to read to your own HF organization"""
