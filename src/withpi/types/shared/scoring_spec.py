# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List

from ..._models import BaseModel
from .scoring_dimension import ScoringDimension

__all__ = ["ScoringSpec"]


class ScoringSpec(BaseModel):
    description: str
    """The application description"""

    dimensions: List[ScoringDimension]
    """The dimensions of the scoring spec"""

    name: str
    """The name of the scoring spec"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
