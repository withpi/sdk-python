# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubDimension"]


class SubDimension(TypedDict, total=False):
    description: Required[str]
    """The description of the dimension"""

    label: Required[str]
    """The label of the dimension"""

    scoring_type: Required[Literal["LLM_AS_A_JUDGE", "HUGGINGFACE_SCORER", "PYTHON_CODE"]]
    """The type of scoring performed for this dimension"""

    huggingface_url: Optional[str]
    """
    The URL of the HuggingFace model to use for scoring. Only relevant for
    scoring_type of hugingface_scorer
    """

    parameters: Optional[Iterable[float]]
    """The learned parameters for the scoring method.

    For llm_as_a_judge type, this corresponds to the values assigned to each Likert
    point from 1-5, normalized to a 0-1 range.
    """

    python_code: Optional[str]
    """The PYTHON code associated the python_code DimensionScoringType."""

    weight: float
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """
