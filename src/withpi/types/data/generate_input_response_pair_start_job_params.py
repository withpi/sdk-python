# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..shared_params.example import Example
from ..shared.exploration_mode import ExplorationMode

__all__ = ["GenerateInputResponsePairStartJobParams"]


class GenerateInputResponsePairStartJobParams(TypedDict, total=False):
    num_pairs_to_generate: Required[int]
    """The number of new LLM input-response pairs to generate"""

    seeds: Required[Iterable[Example]]
    """The list of LLM input response-pairs to be used as seeds"""

    application_description: Optional[str]
    """The application description for which the synthetic data would be applicable."""

    batch_size: int
    """Number of input-response pairs to generate in one LLM call.

    Must be <=10. Generally it could be same as `num_shots`.
    """

    exploration_mode: ExplorationMode
    """The exploration mode for input-response pairs generation.

    Defaults to `BALANCED`
    """

    num_shots: int
    """Number of input-response pairs to be included in the prompt for generation"""

    run_parallel_batches: bool
    """If true, multiple batches of generation and critique run concurrently."""

    system_prompt: Optional[str]
    """The system prompt to generate the responses for the application's inputs"""
