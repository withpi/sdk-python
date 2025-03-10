# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sft import (
    SftResource,
    AsyncSftResource,
    SftResourceWithRawResponse,
    AsyncSftResourceWithRawResponse,
    SftResourceWithStreamingResponse,
    AsyncSftResourceWithStreamingResponse,
)
from .grpo import (
    GrpoResource,
    AsyncGrpoResource,
    GrpoResourceWithRawResponse,
    AsyncGrpoResourceWithRawResponse,
    GrpoResourceWithStreamingResponse,
    AsyncGrpoResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TrainingResource", "AsyncTrainingResource"]


class TrainingResource(SyncAPIResource):
    @cached_property
    def sft(self) -> SftResource:
        return SftResource(self._client)

    @cached_property
    def grpo(self) -> GrpoResource:
        return GrpoResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return TrainingResourceWithStreamingResponse(self)


class AsyncTrainingResource(AsyncAPIResource):
    @cached_property
    def sft(self) -> AsyncSftResource:
        return AsyncSftResource(self._client)

    @cached_property
    def grpo(self) -> AsyncGrpoResource:
        return AsyncGrpoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncTrainingResourceWithStreamingResponse(self)


class TrainingResourceWithRawResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

    @cached_property
    def sft(self) -> SftResourceWithRawResponse:
        return SftResourceWithRawResponse(self._training.sft)

    @cached_property
    def grpo(self) -> GrpoResourceWithRawResponse:
        return GrpoResourceWithRawResponse(self._training.grpo)


class AsyncTrainingResourceWithRawResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

    @cached_property
    def sft(self) -> AsyncSftResourceWithRawResponse:
        return AsyncSftResourceWithRawResponse(self._training.sft)

    @cached_property
    def grpo(self) -> AsyncGrpoResourceWithRawResponse:
        return AsyncGrpoResourceWithRawResponse(self._training.grpo)


class TrainingResourceWithStreamingResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

    @cached_property
    def sft(self) -> SftResourceWithStreamingResponse:
        return SftResourceWithStreamingResponse(self._training.sft)

    @cached_property
    def grpo(self) -> GrpoResourceWithStreamingResponse:
        return GrpoResourceWithStreamingResponse(self._training.grpo)


class AsyncTrainingResourceWithStreamingResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

    @cached_property
    def sft(self) -> AsyncSftResourceWithStreamingResponse:
        return AsyncSftResourceWithStreamingResponse(self._training.sft)

    @cached_property
    def grpo(self) -> AsyncGrpoResourceWithStreamingResponse:
        return AsyncGrpoResourceWithStreamingResponse(self._training.grpo)
