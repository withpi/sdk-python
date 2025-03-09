# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .rl_grpo_status import RlGrpoStatus

__all__ = ["GrpoListResponse"]

GrpoListResponse: TypeAlias = List[RlGrpoStatus]
