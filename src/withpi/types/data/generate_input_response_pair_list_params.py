# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["GenerateInputResponsePairListParams"]


class GenerateInputResponsePairListParams(TypedDict, total=False):
    state: Optional[Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]]
    """Filter jobs by state"""
