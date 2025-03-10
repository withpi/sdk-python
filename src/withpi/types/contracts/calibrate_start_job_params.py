# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .calibration_strategy import CalibrationStrategy
from .sdk_labeled_example_param import SDKLabeledExampleParam
from .sdk_preference_example_param import SDKPreferenceExampleParam
from ..shared_params.scoring_system import ScoringSystem

__all__ = ["CalibrateStartJobParams"]


class CalibrateStartJobParams(TypedDict, total=False):
    scoring_system: Required[ScoringSystem]
    """The scoring system to calibrate"""

    examples: Optional[Iterable[SDKLabeledExampleParam]]
    """Rated examples to use when calibrating the scoring system.

    Must specify either the examples or the preference examples
    """

    preference_examples: Optional[Iterable[SDKPreferenceExampleParam]]
    """Preference examples to use when calibrating the scoring system.

    Must specify either the examples or preference examples
    """

    strategy: CalibrationStrategy
    """The strategy to use to calibrate the scoring system.

    FULL would take longer than LITE but may result in better result.
    """
