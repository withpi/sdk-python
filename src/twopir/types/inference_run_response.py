# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["InferenceRunResponse"]


class InferenceRunResponse(BaseModel):
    text: str
    """The generated text"""
