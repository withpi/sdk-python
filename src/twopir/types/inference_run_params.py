# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["InferenceRunParams"]


class InferenceRunParams(TypedDict, total=False):
    llm_input: Required[Union[str, Dict[str, str]]]
