# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.search import consistency_check_params
from ...types.search.consistency_check_response import ConsistencyCheckResponse

__all__ = ["ConsistencyResource", "AsyncConsistencyResource"]


class ConsistencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsistencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConsistencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsistencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return ConsistencyResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        output1: str,
        output2: str,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsistencyCheckResponse:
        """
        Checks how two query outputs or passages compare with each other.

        Args:
          output1: The first output or passage to check for consistency.

          output2: The second output or passage to check for consistency.

          query: The optional query that generated the outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/consistency/check",
            body=maybe_transform(
                {
                    "output1": output1,
                    "output2": output2,
                    "query": query,
                },
                consistency_check_params.ConsistencyCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsistencyCheckResponse,
        )


class AsyncConsistencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsistencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsistencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsistencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncConsistencyResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        output1: str,
        output2: str,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsistencyCheckResponse:
        """
        Checks how two query outputs or passages compare with each other.

        Args:
          output1: The first output or passage to check for consistency.

          output2: The second output or passage to check for consistency.

          query: The optional query that generated the outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/consistency/check",
            body=await async_maybe_transform(
                {
                    "output1": output1,
                    "output2": output2,
                    "query": query,
                },
                consistency_check_params.ConsistencyCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsistencyCheckResponse,
        )


class ConsistencyResourceWithRawResponse:
    def __init__(self, consistency: ConsistencyResource) -> None:
        self._consistency = consistency

        self.check = to_raw_response_wrapper(
            consistency.check,
        )


class AsyncConsistencyResourceWithRawResponse:
    def __init__(self, consistency: AsyncConsistencyResource) -> None:
        self._consistency = consistency

        self.check = async_to_raw_response_wrapper(
            consistency.check,
        )


class ConsistencyResourceWithStreamingResponse:
    def __init__(self, consistency: ConsistencyResource) -> None:
        self._consistency = consistency

        self.check = to_streamed_response_wrapper(
            consistency.check,
        )


class AsyncConsistencyResourceWithStreamingResponse:
    def __init__(self, consistency: AsyncConsistencyResource) -> None:
        self._consistency = consistency

        self.check = async_to_streamed_response_wrapper(
            consistency.check,
        )
