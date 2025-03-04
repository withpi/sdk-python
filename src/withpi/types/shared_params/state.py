# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["State"]

State: TypeAlias = Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]
