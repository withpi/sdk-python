# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .prompt import (
    PromptResource,
    AsyncPromptResource,
    PromptResourceWithRawResponse,
    AsyncPromptResourceWithRawResponse,
    PromptResourceWithStreamingResponse,
    AsyncPromptResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .model.model import (
    ModelResource,
    AsyncModelResource,
    ModelResourceWithRawResponse,
    AsyncModelResourceWithRawResponse,
    ModelResourceWithStreamingResponse,
    AsyncModelResourceWithStreamingResponse,
)

__all__ = ["TuneResource", "AsyncTuneResource"]


class TuneResource(SyncAPIResource):
    @cached_property
    def prompt(self) -> PromptResource:
        return PromptResource(self._client)

    @cached_property
    def model(self) -> ModelResource:
        return ModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> TuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return TuneResourceWithStreamingResponse(self)


class AsyncTuneResource(AsyncAPIResource):
    @cached_property
    def prompt(self) -> AsyncPromptResource:
        return AsyncPromptResource(self._client)

    @cached_property
    def model(self) -> AsyncModelResource:
        return AsyncModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncTuneResourceWithStreamingResponse(self)


class TuneResourceWithRawResponse:
    def __init__(self, tune: TuneResource) -> None:
        self._tune = tune

    @cached_property
    def prompt(self) -> PromptResourceWithRawResponse:
        return PromptResourceWithRawResponse(self._tune.prompt)

    @cached_property
    def model(self) -> ModelResourceWithRawResponse:
        return ModelResourceWithRawResponse(self._tune.model)


class AsyncTuneResourceWithRawResponse:
    def __init__(self, tune: AsyncTuneResource) -> None:
        self._tune = tune

    @cached_property
    def prompt(self) -> AsyncPromptResourceWithRawResponse:
        return AsyncPromptResourceWithRawResponse(self._tune.prompt)

    @cached_property
    def model(self) -> AsyncModelResourceWithRawResponse:
        return AsyncModelResourceWithRawResponse(self._tune.model)


class TuneResourceWithStreamingResponse:
    def __init__(self, tune: TuneResource) -> None:
        self._tune = tune

    @cached_property
    def prompt(self) -> PromptResourceWithStreamingResponse:
        return PromptResourceWithStreamingResponse(self._tune.prompt)

    @cached_property
    def model(self) -> ModelResourceWithStreamingResponse:
        return ModelResourceWithStreamingResponse(self._tune.model)


class AsyncTuneResourceWithStreamingResponse:
    def __init__(self, tune: AsyncTuneResource) -> None:
        self._tune = tune

    @cached_property
    def prompt(self) -> AsyncPromptResourceWithStreamingResponse:
        return AsyncPromptResourceWithStreamingResponse(self._tune.prompt)

    @cached_property
    def model(self) -> AsyncModelResourceWithStreamingResponse:
        return AsyncModelResourceWithStreamingResponse(self._tune.model)
