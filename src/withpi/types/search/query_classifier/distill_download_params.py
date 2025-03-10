# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DistillDownloadParams"]


class DistillDownloadParams(TypedDict, total=False):
    serving_id: Required[int]
