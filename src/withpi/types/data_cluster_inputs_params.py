# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataClusterInputsParams", "Input"]


class DataClusterInputsParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]
    """The data to create clusters from."""

    num_clusters: Optional[int]
    """The number of clusters to form.

    If none, the api chooses a number automatically.
    """


class Input(TypedDict, total=False):
    identifier: Required[str]
    """The identifier of the input"""

    llm_input: Required[str]
    """The input to LLM"""
