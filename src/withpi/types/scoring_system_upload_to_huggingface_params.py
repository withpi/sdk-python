# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params import scoring_spec as _scoring_spec
from .shared_params.question import Question

__all__ = ["ScoringSystemUploadToHuggingfaceParams", "ScoringSpec"]


class ScoringSystemUploadToHuggingfaceParams(TypedDict, total=False):
    hf_scoring_spec_name: Required[str]
    """Huggingface scoring spec name e.g.

    withpi/my_scoring_system. By default we export to the withpi organization. If
    you want to use your own organization, we provide the hf_token.
    """

    scoring_spec: Required[ScoringSpec]
    """The list of questions or the scoring spec to write to Huggingface"""

    hf_token: Optional[str]
    """Huggingface token to use if you want to write to your own HF organization"""


ScoringSpec: TypeAlias = Union[Iterable[Question], _scoring_spec.ScoringSpec]
