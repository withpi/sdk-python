# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .optimize import (
    OptimizeResource,
    AsyncOptimizeResource,
    OptimizeResourceWithRawResponse,
    AsyncOptimizeResourceWithRawResponse,
    OptimizeResourceWithStreamingResponse,
    AsyncOptimizeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def optimize(self) -> OptimizeResource:
        return OptimizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def optimize(self) -> AsyncOptimizeResource:
        return AsyncOptimizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

    @cached_property
    def optimize(self) -> OptimizeResourceWithRawResponse:
        return OptimizeResourceWithRawResponse(self._prompt.optimize)


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

    @cached_property
    def optimize(self) -> AsyncOptimizeResourceWithRawResponse:
        return AsyncOptimizeResourceWithRawResponse(self._prompt.optimize)


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

    @cached_property
    def optimize(self) -> OptimizeResourceWithStreamingResponse:
        return OptimizeResourceWithStreamingResponse(self._prompt.optimize)


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

    @cached_property
    def optimize(self) -> AsyncOptimizeResourceWithStreamingResponse:
        return AsyncOptimizeResourceWithStreamingResponse(self._prompt.optimize)
