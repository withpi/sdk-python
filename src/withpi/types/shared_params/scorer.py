# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .scorer_dimension import ScorerDimension

__all__ = ["Scorer"]


class ScorerTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[ScorerDimension]
    """The dimensions of the scoring system"""


Scorer: TypeAlias = Union[ScorerTyped, Dict[str, object]]
