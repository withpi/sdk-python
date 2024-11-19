# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["InferenceRunResponse"]


class InferenceRunResponse(BaseModel):
    structured: Optional[Dict[str, object]] = None
    """The structured output, if the model returns structure"""

    text: Optional[str] = None
    """The generated text, if the model returns text"""
