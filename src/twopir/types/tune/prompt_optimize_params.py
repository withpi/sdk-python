# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared_params.contract import Contract

__all__ = ["PromptOptimizeParams"]


class PromptOptimizeParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to optimize"""

    experiment_id: Required[int]
    """The experiment id"""
