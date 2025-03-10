# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel
from .scorer_dimension import ScorerDimension

__all__ = ["Scorer"]


class Scorer(BaseModel):
    description: str
    """The application description"""

    name: str
    """The name of the scoring system"""

    dimensions: Optional[List[ScorerDimension]] = None
    """The dimensions of the scoring system"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
