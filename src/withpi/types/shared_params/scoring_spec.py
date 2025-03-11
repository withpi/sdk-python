# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .scoring_dimension import ScoringDimension

__all__ = ["ScoringSpec"]


class ScoringSpecTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[ScoringDimension]
    """The dimensions of the scoring system"""


ScoringSpec: TypeAlias = Union[ScoringSpecTyped, Dict[str, object]]
