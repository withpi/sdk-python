# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ContractCalibrateResponse"]


class ContractCalibrateResponse(BaseModel):
    description: str
    """The description of the contract"""

    name: str
    """The name of the contract"""
