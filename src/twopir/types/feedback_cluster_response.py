# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .feedback_topic_cluster import FeedbackTopicCluster

__all__ = ["FeedbackClusterResponse"]

FeedbackClusterResponse: TypeAlias = List[FeedbackTopicCluster]
