# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["SubDimension"]


class SubDimension(BaseModel):
    description: str
    """The description of the dimension"""

    label: str
    """The label of the dimension"""
