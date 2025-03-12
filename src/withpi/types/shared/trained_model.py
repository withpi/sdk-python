# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TrainedModel"]


class TrainedModel(BaseModel):
    epoch: float
    """The training epoch"""

    eval_loss: float
    """The evaluation loss"""

    serving_id: int
    """The serving id of the trained model within this Job"""

    serving_state: Literal["UNLOADED", "LOADING", "SERVING"]
    """State of the model in the serving system"""

    step: int
    """The training step"""

    pi_score: Optional[float] = None
    """The PI score of the eval set what isn't used in training"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
