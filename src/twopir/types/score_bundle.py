# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ScoreBundle", "Score"]


class Score(BaseModel):
    dimension: Optional[str] = None

    score: Optional[float] = None


class ScoreBundle(BaseModel):
    scores: Optional[List[Score]] = None
