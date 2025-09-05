# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Question"]


class Question(BaseModel):
    question: str
    """The yes/no question to ask Pi Scoring System."""

    custom_model_id: Optional[str] = None
    """
    The ID of the custom model associated with the CUSTOM_MODEL_SCORER scoring_type.
    """

    label: Optional[str] = None
    """The label of the question."""

    parameters: Optional[List[float]] = None
    """
    The learned parameters for the scoring question define a piecewise linear
    interpolation over the range [0, 1]. This transformation adjusts the score
    distribution to better match your preferences—for example, by pulling scores
    below 0.5 closer to 0, and scores above 0.5 closer to 1.
    """

    python_code: Optional[str] = None
    """The PYTHON code associated with the PYTHON_CODE scoring_type."""

    scoring_type: Optional[Literal["PI_SCORER", "PYTHON_CODE", "CUSTOM_MODEL_SCORER"]] = None
    """The type of scoring performed for this question. Default: PI_SCORER."""

    tag: Optional[str] = None
    """The tag or the group to which this question belongs."""

    weight: Optional[float] = None
    """
    The weight of the question which reflects its relative importance. The sum of
    question weights will be normalized to one internally. A higher weight counts
    for more when aggregating this subdimension into the parent dimension.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
