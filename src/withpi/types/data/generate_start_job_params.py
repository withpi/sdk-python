# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..shared.exploration_mode import ExplorationMode

__all__ = ["GenerateStartJobParams"]


class GenerateStartJobParams(TypedDict, total=False):
    application_description: Required[str]
    """The application description for which the inputs would be applicable."""

    num_inputs_to_generate: Required[int]
    """The number of new LLM inputs to generate"""

    seeds: Required[SequenceNotStr[str]]
    """The list of LLM inputs to be used as seeds"""

    batch_size: int
    """Number of inputs to generate in one LLM call.

    Must be <= 125. Generally it could be same as `num_shots`.
    """

    exploration_mode: ExplorationMode
    """The exloration mode for input generation. Defaults to `BALANCED`"""

    num_shots: int
    """Number of inputs to be included in the prompt for generation.

    Must be <= 50. Generally it could be same as `batch_size`.
    """

    run_parallel_batches: bool
    """If true, multiple batches of generation and critique run concurrently."""
