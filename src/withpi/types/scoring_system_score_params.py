# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.scoring_spec import ScoringSpec

__all__ = ["ScoringSystemScoreParams"]


class ScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_spec: Required[ScoringSpec]
    """The scoring spec to score"""
