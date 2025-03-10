# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.scorer import Scorer

__all__ = ["ScorerScoreParams"]


class ScorerScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scorer: Required[Scorer]
    """The scoring system to score"""
