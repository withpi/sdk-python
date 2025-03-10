# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.scoring_system import ScoringSystem

__all__ = ["PiScoringSystemScoreParams"]


class PiScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_system: Required[ScoringSystem]
    """The scoring system to score"""
