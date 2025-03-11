# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScoringSystemImportSpecParams"]


class ScoringSystemImportSpecParams(TypedDict, total=False):
    hf_scoring_spec_name: Required[str]
    """Huggingface dataset e.g.

    withpi/my_scoring_system containing the Scoring spec. This is only needed for
    the source=HUGGINGFACE.
    """

    hf_token: Optional[str]
    """Huggingface token to use if you want to read to your own HF organization.

    This is only needed for the source=HUGGINGFACE.
    """

    source: Literal["HUGGINGFACE"]
    """Source of where to get the Scoring spec"""
