# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import data_create_cluster_inputs_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .generate_inputs import (
    GenerateInputsResource,
    AsyncGenerateInputsResource,
    GenerateInputsResourceWithRawResponse,
    AsyncGenerateInputsResourceWithRawResponse,
    GenerateInputsResourceWithStreamingResponse,
    AsyncGenerateInputsResourceWithStreamingResponse,
)
from .generate_examples import (
    GenerateExamplesResource,
    AsyncGenerateExamplesResource,
    GenerateExamplesResourceWithRawResponse,
    AsyncGenerateExamplesResourceWithRawResponse,
    GenerateExamplesResourceWithStreamingResponse,
    AsyncGenerateExamplesResourceWithStreamingResponse,
)
from ...types.data_create_cluster_inputs_response import DataCreateClusterInputsResponse

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def generate_examples(self) -> GenerateExamplesResource:
        return GenerateExamplesResource(self._client)

    @cached_property
    def generate_inputs(self) -> GenerateInputsResource:
        return GenerateInputsResource(self._client)

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

    def create_cluster_inputs(
        self,
        *,
        inputs: Iterable[data_create_cluster_inputs_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataCreateClusterInputsResponse:
        """
        Clusters inputs into groups with counts

        Args:
          inputs: The data to create clusters from.

          num_clusters: The number of clusters to form. If none, the api chooses a number automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/cluster_inputs",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "num_clusters": num_clusters,
                },
                data_create_cluster_inputs_params.DataCreateClusterInputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataCreateClusterInputsResponse,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def generate_examples(self) -> AsyncGenerateExamplesResource:
        return AsyncGenerateExamplesResource(self._client)

    @cached_property
    def generate_inputs(self) -> AsyncGenerateInputsResource:
        return AsyncGenerateInputsResource(self._client)

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

    async def create_cluster_inputs(
        self,
        *,
        inputs: Iterable[data_create_cluster_inputs_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataCreateClusterInputsResponse:
        """
        Clusters inputs into groups with counts

        Args:
          inputs: The data to create clusters from.

          num_clusters: The number of clusters to form. If none, the api chooses a number automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/cluster_inputs",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "num_clusters": num_clusters,
                },
                data_create_cluster_inputs_params.DataCreateClusterInputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataCreateClusterInputsResponse,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.create_cluster_inputs = to_raw_response_wrapper(
            data.create_cluster_inputs,
        )

    @cached_property
    def generate_examples(self) -> GenerateExamplesResourceWithRawResponse:
        return GenerateExamplesResourceWithRawResponse(self._data.generate_examples)

    @cached_property
    def generate_inputs(self) -> GenerateInputsResourceWithRawResponse:
        return GenerateInputsResourceWithRawResponse(self._data.generate_inputs)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.create_cluster_inputs = async_to_raw_response_wrapper(
            data.create_cluster_inputs,
        )

    @cached_property
    def generate_examples(self) -> AsyncGenerateExamplesResourceWithRawResponse:
        return AsyncGenerateExamplesResourceWithRawResponse(self._data.generate_examples)

    @cached_property
    def generate_inputs(self) -> AsyncGenerateInputsResourceWithRawResponse:
        return AsyncGenerateInputsResourceWithRawResponse(self._data.generate_inputs)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.create_cluster_inputs = to_streamed_response_wrapper(
            data.create_cluster_inputs,
        )

    @cached_property
    def generate_examples(self) -> GenerateExamplesResourceWithStreamingResponse:
        return GenerateExamplesResourceWithStreamingResponse(self._data.generate_examples)

    @cached_property
    def generate_inputs(self) -> GenerateInputsResourceWithStreamingResponse:
        return GenerateInputsResourceWithStreamingResponse(self._data.generate_inputs)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.create_cluster_inputs = async_to_streamed_response_wrapper(
            data.create_cluster_inputs,
        )

    @cached_property
    def generate_examples(self) -> AsyncGenerateExamplesResourceWithStreamingResponse:
        return AsyncGenerateExamplesResourceWithStreamingResponse(self._data.generate_examples)

    @cached_property
    def generate_inputs(self) -> AsyncGenerateInputsResourceWithStreamingResponse:
        return AsyncGenerateInputsResourceWithStreamingResponse(self._data.generate_inputs)
