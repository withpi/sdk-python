# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["DataListResponse", "DataListResponseItem"]


class DataListResponseItem(BaseModel):
    llm_input: str

    llm_output: str


DataListResponse: TypeAlias = List[DataListResponseItem]
