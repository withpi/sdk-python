# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LoraConfig"]


class LoraConfig(BaseModel):
    lora_rank: Optional[Literal["R_16", "R_32", "R_64"]] = None
    """The number of dimensions in the low-rank decomposition of the weight updates."""
