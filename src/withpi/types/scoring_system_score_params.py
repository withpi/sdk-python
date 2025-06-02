# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params import scoring_spec as _scoring_spec
from .shared_params.question import Question

__all__ = ["ScoringSystemScoreParams", "ScoringSpec"]


class ScoringSystemScoreParams(TypedDict, total=False):
    llm_input: Required[str]
    """The input to score"""

    llm_output: Required[str]
    """The output to score"""

    scoring_spec: Required[ScoringSpec]
    """Either a scoring spec or a list of questions to score"""

    aggregtion_method: Literal["ARITHMETIC_MEAN", "GEOMETRIC_MEAN", "HARMONIC_MEAN"]
    """The strategy to use to calibrate the scoring spec.

    FULL would take longer than LITE but may result in better result.
    """

    kwargs: object
    """Optional additional parameters (keyword arguments)"""


ScoringSpec: TypeAlias = Union[Iterable[Question], _scoring_spec.ScoringSpec]
