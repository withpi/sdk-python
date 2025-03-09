# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .scoring_system.scoring_system_param import ScoringSystemParam

__all__ = ["ScoringSystemScoreParams"]


class ScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_system: Required[ScoringSystemParam]
    """The scoring system to score"""
