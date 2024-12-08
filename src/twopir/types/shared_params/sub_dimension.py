# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubDimension"]


class SubDimension(TypedDict, total=False):
    id: Required[str]
    """The label of the dimension"""

    description: Required[str]
    """The description of the dimension"""

    parameters: Required[Optional[Iterable[float]]]
    """The learned parameters for the scoring method.

    For llm_as_a_judge type, this corresponds to the values assigned to each Likert
    point from 1-5, normalized to a 0-1 range.
    """

    scoring_type: Required[Literal["llm_as_a_judge", "glean_structured_detector", "python_code"]]
    """The type of scoring performed for this dimension"""

    weight: Required[float]
    """The weight of the subdimension.

    The sum of subdimension weights will be normalized to one internally.  A higher weight counts
            for more when aggregating this subdimension into the parent dimension.
    """
