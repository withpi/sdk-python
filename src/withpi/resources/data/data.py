# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .input.input import (
    InputResource,
    AsyncInputResource,
    InputResourceWithRawResponse,
    AsyncInputResourceWithRawResponse,
    InputResourceWithStreamingResponse,
    AsyncInputResourceWithStreamingResponse,
)
from .generate_synthetic_data import (
    GenerateSyntheticDataResource,
    AsyncGenerateSyntheticDataResource,
    GenerateSyntheticDataResourceWithRawResponse,
    AsyncGenerateSyntheticDataResourceWithRawResponse,
    GenerateSyntheticDataResourceWithStreamingResponse,
    AsyncGenerateSyntheticDataResourceWithStreamingResponse,
)

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def generate_synthetic_data(self) -> GenerateSyntheticDataResource:
        return GenerateSyntheticDataResource(self._client)

    @cached_property
    def input(self) -> InputResource:
        return InputResource(self._client)

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
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResource:
        return AsyncGenerateSyntheticDataResource(self._client)

    @cached_property
    def input(self) -> AsyncInputResource:
        return AsyncInputResource(self._client)

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
    def generate_synthetic_data(self) -> GenerateSyntheticDataResourceWithRawResponse:
        return GenerateSyntheticDataResourceWithRawResponse(self._data.generate_synthetic_data)

    @cached_property
    def input(self) -> InputResourceWithRawResponse:
        return InputResourceWithRawResponse(self._data.input)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResourceWithRawResponse:
        return AsyncGenerateSyntheticDataResourceWithRawResponse(self._data.generate_synthetic_data)

    @cached_property
    def input(self) -> AsyncInputResourceWithRawResponse:
        return AsyncInputResourceWithRawResponse(self._data.input)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def generate_synthetic_data(self) -> GenerateSyntheticDataResourceWithStreamingResponse:
        return GenerateSyntheticDataResourceWithStreamingResponse(self._data.generate_synthetic_data)

    @cached_property
    def input(self) -> InputResourceWithStreamingResponse:
        return InputResourceWithStreamingResponse(self._data.input)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResourceWithStreamingResponse:
        return AsyncGenerateSyntheticDataResourceWithStreamingResponse(self._data.generate_synthetic_data)

    @cached_property
    def input(self) -> AsyncInputResourceWithStreamingResponse:
        return AsyncInputResourceWithStreamingResponse(self._data.input)
