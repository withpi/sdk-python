# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import query_generate_fanouts_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.query_generate_fanouts_response import QueryGenerateFanoutsResponse

__all__ = ["QueriesResource", "AsyncQueriesResource"]


class QueriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return QueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return QueriesResourceWithStreamingResponse(self)

    def generate_fanouts(
        self,
        *,
        queries: List[str],
        example_fanout_queries: Iterable[query_generate_fanouts_params.ExampleFanoutQuery] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryGenerateFanoutsResponse:
        """
        Generates query fanouts for an input query.

        Args:
          queries: The list of queries to generate fanouts for

          example_fanout_queries: The list of queries to use as few-shot examples for the fanout generation

          num_fanout_queries: The number of fanout queries to generate for each input query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/queries/generate_fanouts",
            body=maybe_transform(
                {
                    "queries": queries,
                    "example_fanout_queries": example_fanout_queries,
                    "num_fanout_queries": num_fanout_queries,
                },
                query_generate_fanouts_params.QueryGenerateFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryGenerateFanoutsResponse,
        )


class AsyncQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncQueriesResourceWithStreamingResponse(self)

    async def generate_fanouts(
        self,
        *,
        queries: List[str],
        example_fanout_queries: Iterable[query_generate_fanouts_params.ExampleFanoutQuery] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryGenerateFanoutsResponse:
        """
        Generates query fanouts for an input query.

        Args:
          queries: The list of queries to generate fanouts for

          example_fanout_queries: The list of queries to use as few-shot examples for the fanout generation

          num_fanout_queries: The number of fanout queries to generate for each input query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/queries/generate_fanouts",
            body=await async_maybe_transform(
                {
                    "queries": queries,
                    "example_fanout_queries": example_fanout_queries,
                    "num_fanout_queries": num_fanout_queries,
                },
                query_generate_fanouts_params.QueryGenerateFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryGenerateFanoutsResponse,
        )


class QueriesResourceWithRawResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.generate_fanouts = to_raw_response_wrapper(
            queries.generate_fanouts,
        )


class AsyncQueriesResourceWithRawResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.generate_fanouts = async_to_raw_response_wrapper(
            queries.generate_fanouts,
        )


class QueriesResourceWithStreamingResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.generate_fanouts = to_streamed_response_wrapper(
            queries.generate_fanouts,
        )


class AsyncQueriesResourceWithStreamingResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.generate_fanouts = async_to_streamed_response_wrapper(
            queries.generate_fanouts,
        )
