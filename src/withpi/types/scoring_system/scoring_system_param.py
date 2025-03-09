# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..sdk_dimension_param import SDKDimensionParam

__all__ = ["ScoringSystemParam"]


class ScoringSystemParamTyped(TypedDict, total=False):
    description: Required[str]
    """The application description"""

    name: Required[str]
    """The name of the scoring system"""

    dimensions: Iterable[SDKDimensionParam]
    """The dimensions of the scoring system"""


ScoringSystemParam: TypeAlias = Union[ScoringSystemParamTyped, Dict[str, object]]
