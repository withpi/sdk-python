# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DataCreateClusterInputsResponse", "DataCreateClusterInputsResponseItem"]


class DataCreateClusterInputsResponseItem(BaseModel):
    inputs: List[str]
    """The input IDs assigned to this topic"""

    topic: str
    """The topic of the input in this cluster"""


DataCreateClusterInputsResponse: TypeAlias = List[DataCreateClusterInputsResponseItem]
