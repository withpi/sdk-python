# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.data import input_cluster_params
from ...._base_client import make_request_options
from .generate_from_seeds import (
    GenerateFromSeedsResource,
    AsyncGenerateFromSeedsResource,
    GenerateFromSeedsResourceWithRawResponse,
    AsyncGenerateFromSeedsResourceWithRawResponse,
    GenerateFromSeedsResourceWithStreamingResponse,
    AsyncGenerateFromSeedsResourceWithStreamingResponse,
)
from ....types.data.input_cluster_response import InputClusterResponse

__all__ = ["InputResource", "AsyncInputResource"]


class InputResource(SyncAPIResource):
    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResource:
        return GenerateFromSeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InputResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return InputResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return InputResourceWithStreamingResponse(self)

    def cluster(
        self,
        *,
        inputs: Iterable[input_cluster_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputClusterResponse:
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
            "/data/input/cluster",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "num_clusters": num_clusters,
                },
                input_cluster_params.InputClusterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputClusterResponse,
        )


class AsyncInputResource(AsyncAPIResource):
    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResource:
        return AsyncGenerateFromSeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInputResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInputResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncInputResourceWithStreamingResponse(self)

    async def cluster(
        self,
        *,
        inputs: Iterable[input_cluster_params.Input],
        num_clusters: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputClusterResponse:
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
            "/data/input/cluster",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "num_clusters": num_clusters,
                },
                input_cluster_params.InputClusterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputClusterResponse,
        )


class InputResourceWithRawResponse:
    def __init__(self, input: InputResource) -> None:
        self._input = input

        self.cluster = to_raw_response_wrapper(
            input.cluster,
        )

    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResourceWithRawResponse:
        return GenerateFromSeedsResourceWithRawResponse(self._input.generate_from_seeds)


class AsyncInputResourceWithRawResponse:
    def __init__(self, input: AsyncInputResource) -> None:
        self._input = input

        self.cluster = async_to_raw_response_wrapper(
            input.cluster,
        )

    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResourceWithRawResponse:
        return AsyncGenerateFromSeedsResourceWithRawResponse(self._input.generate_from_seeds)


class InputResourceWithStreamingResponse:
    def __init__(self, input: InputResource) -> None:
        self._input = input

        self.cluster = to_streamed_response_wrapper(
            input.cluster,
        )

    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResourceWithStreamingResponse:
        return GenerateFromSeedsResourceWithStreamingResponse(self._input.generate_from_seeds)


class AsyncInputResourceWithStreamingResponse:
    def __init__(self, input: AsyncInputResource) -> None:
        self._input = input

        self.cluster = async_to_streamed_response_wrapper(
            input.cluster,
        )

    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResourceWithStreamingResponse:
        return AsyncGenerateFromSeedsResourceWithStreamingResponse(self._input.generate_from_seeds)
