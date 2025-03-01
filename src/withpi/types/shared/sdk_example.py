# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["SDKExample"]


class SDKExample(BaseModel):
    llm_input: str
    """The input to LLM"""

    llm_output: str
    """The output to evaluate"""
