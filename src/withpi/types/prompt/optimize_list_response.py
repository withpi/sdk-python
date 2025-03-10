# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.prompt_optimization_status import PromptOptimizationStatus

__all__ = ["OptimizeListResponse"]

OptimizeListResponse: TypeAlias = List[PromptOptimizationStatus]
