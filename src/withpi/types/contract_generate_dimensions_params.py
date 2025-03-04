# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContractGenerateDimensionsParams"]


class ContractGenerateDimensionsParams(TypedDict, total=False):
    contract_description: Required[str]
    """The application description to generate contract for."""

    try_auto_generating_python_code: bool
    """
    If true, try to generate python code for sub-dimensions with structured
    evaluation
    """
