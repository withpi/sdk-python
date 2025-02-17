# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateSyntheticDataCreateParams", "Seed"]


class GenerateSyntheticDataCreateParams(TypedDict, total=False):
    application_description: Required[str]
    """The application description for which the synthetic data would be applicable."""

    num_examples_to_generate: Required[int]
    """The number of new LLM examples to generate"""

    seeds: Required[Iterable[Seed]]
    """The list of LLM examples (inputs + outputs) to be used as seeds"""

    batch_size: int
    """Number of examples to generate in one LLM call.

    Must be <=10. Generally it could be same as `num_shots`.
    """

    exploration_mode: Literal["CONSERVATIVE", "BALANCED", "CREATIVE", "ADVENTUROUS"]
    """The exloration mode for examples generation. Defaults to `BALANCED`"""

    num_shots: int
    """Number of examples to be included in the prompt for generation.

    Generally it could be same as `batch_size`.
    """


class Seed(TypedDict, total=False):
    llm_input: Required[str]
    """The input to LLM"""

    llm_output: Required[str]
    """The output to evaluate"""
