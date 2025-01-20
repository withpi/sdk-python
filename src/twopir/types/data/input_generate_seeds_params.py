# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InputGenerateSeedsParams"]


class InputGenerateSeedsParams(TypedDict, total=False):
    contract_description: Required[str]
    """The application contract's description"""

    num_inputs: Required[int]
    """Number of input seeds to generate.

    Must be <= 50. If you want to generate more, please use the generate_from_seeds
    API.
    """

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
