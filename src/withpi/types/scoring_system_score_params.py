# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

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

    kwargs: object
    """Optional additional parameters (keyword arguments)"""


ScoringSpec: TypeAlias = Union[Iterable[Question], _scoring_spec.ScoringSpec]
