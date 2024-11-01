# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .example_param import ExampleParam

__all__ = ["ScorerScoreParams"]


class ScorerScoreParams(TypedDict, total=False):
    example: Required[Annotated[ExampleParam, PropertyInfo(alias="Example")]]
