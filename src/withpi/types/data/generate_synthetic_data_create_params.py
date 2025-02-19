# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.example import Example

__all__ = ["GenerateSyntheticDataCreateParams"]


class GenerateSyntheticDataCreateParams(TypedDict, total=False):
    num_examples_to_generate: Required[int]
    """The number of new LLM examples to generate"""

    seeds: Required[Iterable[Example]]
    """The list of LLM examples (inputs + outputs) to be used as seeds"""

    application_description: Optional[str]
    """The application description for which the synthetic data would be applicable."""

    batch_size: int
    """Number of examples to generate in one LLM call.

    Must be <=10. Generally it could be same as `num_shots`.
    """

    exploration_mode: Literal["CONSERVATIVE", "BALANCED", "CREATIVE", "ADVENTUROUS"]
    """The exploration mode for examples generation. Defaults to `BALANCED`"""

    num_shots: int
    """Number of examples to be included in the prompt for generation"""

    system_prompt: Optional[str]
    """The system prompt to generate the responses for the application's inputs"""
