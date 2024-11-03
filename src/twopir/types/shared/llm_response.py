# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["LlmResponse"]


class LlmResponse(BaseModel):
    text: str
    """The literal text returned from the LLM."""
