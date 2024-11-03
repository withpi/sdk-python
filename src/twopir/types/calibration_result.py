# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["CalibrationResult"]


class CalibrationResult(BaseModel):
    contract: "Contract"
    """A collection of dimensions an LLM response must adhere to"""


from .shared.contract import Contract

if PYDANTIC_V2:
    CalibrationResult.model_rebuild()
else:
    CalibrationResult.update_forward_refs()  # type: ignore
