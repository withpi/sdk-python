# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetSampleParams"]


class DatasetSampleParams(TypedDict, total=False):
    name: Required[str]
    """The name of a dataset hosted on Hugging Face."""

    split: Required[str]
    """The split to sample from."""

    subset: Optional[str]
    """The subset to sample from."""
