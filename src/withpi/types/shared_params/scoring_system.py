# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .sdk_dimension import SDKDimension

__all__ = ["ScoringSystem"]


class ScoringSystemTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[SDKDimension]
    """The dimensions of the scoring system"""


ScoringSystem: TypeAlias = Union[ScoringSystemTyped, Dict[str, object]]
