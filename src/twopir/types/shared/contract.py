# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel
from .dimension import Dimension

__all__ = ["Contract"]


class Contract(BaseModel):
    description: str
    """The description of the contract"""

    name: str
    """The name of the contract"""

    dimensions: Optional[List[Dimension]] = None
    """The dimensions of the contract"""

    scorer_ast: Union[str, Dict[str, object], None] = None
    """The scorer AST of the contract"""
