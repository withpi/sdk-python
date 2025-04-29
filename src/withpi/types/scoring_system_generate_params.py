# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScoringSystemGenerateParams"]


class ScoringSystemGenerateParams(TypedDict, total=False):
    application_description: Required[str]
    """The application description to generate a scoring spec for."""

    num_questions: int
    """The number of questions that the generated scoring system should contain.

    If <= 0, then the number is auto selected.
    """

    try_auto_generating_python_code: bool
    """If true, try to generate python code for the generated questions."""
