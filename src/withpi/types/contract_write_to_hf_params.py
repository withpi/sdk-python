# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.contract import Contract

__all__ = ["ContractWriteToHfParams"]


class ContractWriteToHfParams(TypedDict, total=False):
    contract: Required[Contract]
    """The contract to write to Huggingface"""

    hf_contract_name: Required[str]
    """Huggingface contract name e.g.

    withpi/my_contract. By default we export to the withpi organization. If you want
    to use your own organization, we provide the hf_token.
    """

    hf_token: Optional[str]
    """Huggingface token to use if you want to write to your own HF organization"""
