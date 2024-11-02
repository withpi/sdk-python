# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .example_param import ExampleParam

__all__ = ["ScorerScoreParams", "Contract", "ContractDimension"]


class ScorerScoreParams(TypedDict, total=False):
    contract: Required[Contract]

    example: Required[ExampleParam]


class ContractDimension(TypedDict, total=False):
    description: Required[str]

    label: Required[str]


class Contract(TypedDict, total=False):
    description: Required[str]

    dimensions: Required[Iterable[ContractDimension]]

    name: Required[str]
