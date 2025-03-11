# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScoringSystemFromHuggingfaceParams"]


class ScoringSystemFromHuggingfaceParams(TypedDict, total=False):
    hf_scorer_name: Required[str]
    """Huggingface scorer name e.g.

    withpi/my_scoring_system. You need to provide the hf_token if the scorer dataset
    is not public or not own by the withpi organization.
    """

    hf_token: Optional[str]
    """Huggingface token to use if you want to read to your own HF organization"""
