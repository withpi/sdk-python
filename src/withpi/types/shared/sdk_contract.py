# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel
from .sdk_dimension import SDKDimension

__all__ = ["SDKContract"]


class SDKContract(BaseModel):
    description: str
    """The description of the contract"""

    name: str
    """The name of the contract"""

    dimensions: Optional[List[SDKDimension]] = None
    """The dimensions of the contract"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
