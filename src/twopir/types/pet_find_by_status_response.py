# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .pet import Pet

__all__ = ["PetFindByStatusResponse"]

PetFindByStatusResponse: TypeAlias = List[Pet]
