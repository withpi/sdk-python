# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["InputEvaluationMetrics"]


class InputEvaluationMetrics(BaseModel):
    filter_score: float
    """The 0-1 score with 1 meaning filter"""
