# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .generate_input_response_pairs import (
    GenerateInputResponsePairsResource,
    AsyncGenerateInputResponsePairsResource,
    GenerateInputResponsePairsResourceWithRawResponse,
    AsyncGenerateInputResponsePairsResourceWithRawResponse,
    GenerateInputResponsePairsResourceWithStreamingResponse,
    AsyncGenerateInputResponsePairsResourceWithStreamingResponse,
)

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def generate(self) -> GenerateResource:
        return GenerateResource(self._client)

    @cached_property
    def generate_input_response_pairs(self) -> GenerateInputResponsePairsResource:
        return GenerateInputResponsePairsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def generate(self) -> AsyncGenerateResource:
        return AsyncGenerateResource(self._client)

    @cached_property
    def generate_input_response_pairs(self) -> AsyncGenerateInputResponsePairsResource:
        return AsyncGenerateInputResponsePairsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> GenerateInputResponsePairsResourceWithRawResponse:
        return GenerateInputResponsePairsResourceWithRawResponse(self._data.generate_input_response_pairs)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> AsyncGenerateInputResponsePairsResourceWithRawResponse:
        return AsyncGenerateInputResponsePairsResourceWithRawResponse(self._data.generate_input_response_pairs)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> GenerateInputResponsePairsResourceWithStreamingResponse:
        return GenerateInputResponsePairsResourceWithStreamingResponse(self._data.generate_input_response_pairs)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> AsyncGenerateInputResponsePairsResourceWithStreamingResponse:
        return AsyncGenerateInputResponsePairsResourceWithStreamingResponse(self._data.generate_input_response_pairs)
