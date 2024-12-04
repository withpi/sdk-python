# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GenerateFromSeedGenerateParams"]


class GenerateFromSeedGenerateParams(TypedDict, total=False):
    num_inputs: Required[int]

    seeds: Required[List[str]]
