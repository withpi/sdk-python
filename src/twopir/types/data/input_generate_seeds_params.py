# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InputGenerateSeedsParams"]


class InputGenerateSeedsParams(TypedDict, total=False):
    contract_description: Required[str]
    """The application contract's description"""

    num_inputs: Required[int]
    """Number of input seeds to generate.

    Must be <= 50. If you want to generate more, please use the generate_from_seeds
    API.
    """
