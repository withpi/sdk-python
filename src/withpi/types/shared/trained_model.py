# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["TrainedModel"]


class TrainedModel(BaseModel):
    contract_score: float
    """The PI contract score of the eval set what isn't used in training"""

    epoch: float
    """The training epoch"""

    eval_loss: float
    """The evaluation loss"""

    is_loaded: bool
    """Whether the model is loaded in the serving system"""

    serving_id: int
    """The serving id of the trained model within this Job"""

    step: int
    """The training step"""
