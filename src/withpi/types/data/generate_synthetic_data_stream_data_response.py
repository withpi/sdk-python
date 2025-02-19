# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["GenerateSyntheticDataStreamDataResponse", "GenerateSyntheticDataStreamDataResponseItem"]


class GenerateSyntheticDataStreamDataResponseItem(BaseModel):
    llm_input: str

    llm_output: str


GenerateSyntheticDataStreamDataResponse: TypeAlias = List[GenerateSyntheticDataStreamDataResponseItem]
