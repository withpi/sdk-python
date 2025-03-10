# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import data_cluster_inputs_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .generate_input_response_pairs import (
    GenerateInputResponsePairsResource,
    AsyncGenerateInputResponsePairsResource,
    GenerateInputResponsePairsResourceWithRawResponse,
    AsyncGenerateInputResponsePairsResourceWithRawResponse,
    GenerateInputResponsePairsResourceWithStreamingResponse,
    AsyncGenerateInputResponsePairsResourceWithStreamingResponse,
)
from ...types.data_cluster_inputs_response import DataClusterInputsResponse

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

    def cluster_inputs(
        self,
        *,
        inputs: Iterable[data_cluster_inputs_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataClusterInputsResponse:
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
                data_cluster_inputs_params.DataClusterInputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataClusterInputsResponse,
        )


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

    async def cluster_inputs(
        self,
        *,
        inputs: Iterable[data_cluster_inputs_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataClusterInputsResponse:
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
                data_cluster_inputs_params.DataClusterInputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataClusterInputsResponse,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.cluster_inputs = to_raw_response_wrapper(
            data.cluster_inputs,
        )

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> GenerateInputResponsePairsResourceWithRawResponse:
        return GenerateInputResponsePairsResourceWithRawResponse(self._data.generate_input_response_pairs)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.cluster_inputs = async_to_raw_response_wrapper(
            data.cluster_inputs,
        )

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> AsyncGenerateInputResponsePairsResourceWithRawResponse:
        return AsyncGenerateInputResponsePairsResourceWithRawResponse(self._data.generate_input_response_pairs)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.cluster_inputs = to_streamed_response_wrapper(
            data.cluster_inputs,
        )

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> GenerateInputResponsePairsResourceWithStreamingResponse:
        return GenerateInputResponsePairsResourceWithStreamingResponse(self._data.generate_input_response_pairs)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.cluster_inputs = async_to_streamed_response_wrapper(
            data.cluster_inputs,
        )

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._data.generate)

    @cached_property
    def generate_input_response_pairs(self) -> AsyncGenerateInputResponsePairsResourceWithStreamingResponse:
        return AsyncGenerateInputResponsePairsResourceWithStreamingResponse(self._data.generate_input_response_pairs)
