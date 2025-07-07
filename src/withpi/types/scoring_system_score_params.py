# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.question import Question

__all__ = ["ScoringSystemScoreParams"]


class ScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_spec: Required[Iterable[Question]]
    """Either a scoring spec or a list of questions to score"""

    aggregation_method: Literal["ARITHMETIC_MEAN", "GEOMETRIC_MEAN", "HARMONIC_MEAN"]
    """The strategy to combine the individual question scores to get the total score.

    Defaults to HARMONIC_MEAN.
    """

    kwargs: object
    """Optional additional parameters (keyword arguments)"""
