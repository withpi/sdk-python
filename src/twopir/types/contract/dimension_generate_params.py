# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared_params.dimension import Dimension

__all__ = ["DimensionGenerateParams"]


class DimensionGenerateParams(TypedDict, total=False):
    dimension: Required[Dimension]
