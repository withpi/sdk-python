# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContractReadFromHfParams"]


class ContractReadFromHfParams(TypedDict, total=False):
    hf_contract_name: Required[str]
    """Huggingface contract name e.g.

    withpi/my_contract. You need to provide the hf_token if the contract dataset is
    not public or not own by the withpi organization.
    """

    hf_token: Optional[str]
    """Huggingface token to read the contract dataset"""
