# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["InferenceRunParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    body: Required[str]


class Variant1(TypedDict, total=False):
    body: Required[Dict[str, str]]


InferenceRunParams: TypeAlias = Union[Variant0, Variant1]
