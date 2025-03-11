# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScoringSystemGenerateParams"]


class ScoringSystemGenerateParams(TypedDict, total=False):
    application_description: Required[str]
    """The application description to generate a scoring spec for."""

    try_auto_generating_python_code: bool
    """If true, try to generate python code for sub-dimensions in the scoring spec."""
