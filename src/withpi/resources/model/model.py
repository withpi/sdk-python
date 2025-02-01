# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sft.sft import (
    SftResource,
    AsyncSftResource,
    SftResourceWithRawResponse,
    AsyncSftResourceWithRawResponse,
    SftResourceWithStreamingResponse,
    AsyncSftResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ModelResource", "AsyncModelResource"]


class ModelResource(SyncAPIResource):
    @cached_property
    def sft(self) -> SftResource:
        return SftResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return ModelResourceWithStreamingResponse(self)


class AsyncModelResource(AsyncAPIResource):
    @cached_property
    def sft(self) -> AsyncSftResource:
        return AsyncSftResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncModelResourceWithStreamingResponse(self)


class ModelResourceWithRawResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

    @cached_property
    def sft(self) -> SftResourceWithRawResponse:
        return SftResourceWithRawResponse(self._model.sft)


class AsyncModelResourceWithRawResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

    @cached_property
    def sft(self) -> AsyncSftResourceWithRawResponse:
        return AsyncSftResourceWithRawResponse(self._model.sft)


class ModelResourceWithStreamingResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

    @cached_property
    def sft(self) -> SftResourceWithStreamingResponse:
        return SftResourceWithStreamingResponse(self._model.sft)


class AsyncModelResourceWithStreamingResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

    @cached_property
    def sft(self) -> AsyncSftResourceWithStreamingResponse:
        return AsyncSftResourceWithStreamingResponse(self._model.sft)
