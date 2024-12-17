# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InputGenerateSeedsParams"]


class InputGenerateSeedsParams(TypedDict, total=False):
    contract: Required["Contract"]
    """The contract to generate input seeds for."""

    num_inputs: Required[int]
    """Number of input seeds to generate."""

    context_types: Optional[
        List[
            Literal[
                "none",
                "article",
                "conversation",
                "debate",
                "webpage",
                "passage",
                "chat history",
                "email thread",
                "text messages",
                "financial document",
                "scientific paper",
                "slide presentation description",
            ]
        ]
    ]
    """The types of context to generate for the input prompts if specified.

    Otherwise the context_types will be inferred.
    """


from ..shared_params.contract import Contract
