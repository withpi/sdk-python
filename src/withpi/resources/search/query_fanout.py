# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ...types.search import query_fanout_generate_params
from ...types.shared_params.query_fanout_example import QueryFanoutExample
from ...types.search.query_fanout_generate_response import QueryFanoutGenerateResponse

__all__ = ["QueryFanoutResource", "AsyncQueryFanoutResource"]


class QueryFanoutResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryFanoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return QueryFanoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryFanoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return QueryFanoutResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        query: str,
        few_shot_examples: Iterable[QueryFanoutExample] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryFanoutGenerateResponse:
        """
        Generates query fanout for an input query.

        Args:
          query: The query to generate fanouts for

          few_shot_examples: The list of few-shot examples for the fanout generation. Only needed if the
              default fanouts are not working well.

          num_fanout_queries: The number of fanout queries to generate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/query_fanout/generate",
            body=maybe_transform(
                {
                    "query": query,
                    "few_shot_examples": few_shot_examples,
                    "num_fanout_queries": num_fanout_queries,
                },
                query_fanout_generate_params.QueryFanoutGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryFanoutGenerateResponse,
        )


class AsyncQueryFanoutResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryFanoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryFanoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryFanoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncQueryFanoutResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        query: str,
        few_shot_examples: Iterable[QueryFanoutExample] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryFanoutGenerateResponse:
        """
        Generates query fanout for an input query.

        Args:
          query: The query to generate fanouts for

          few_shot_examples: The list of few-shot examples for the fanout generation. Only needed if the
              default fanouts are not working well.

          num_fanout_queries: The number of fanout queries to generate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/query_fanout/generate",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "few_shot_examples": few_shot_examples,
                    "num_fanout_queries": num_fanout_queries,
                },
                query_fanout_generate_params.QueryFanoutGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryFanoutGenerateResponse,
        )


class QueryFanoutResourceWithRawResponse:
    def __init__(self, query_fanout: QueryFanoutResource) -> None:
        self._query_fanout = query_fanout

        self.generate = to_raw_response_wrapper(
            query_fanout.generate,
        )


class AsyncQueryFanoutResourceWithRawResponse:
    def __init__(self, query_fanout: AsyncQueryFanoutResource) -> None:
        self._query_fanout = query_fanout

        self.generate = async_to_raw_response_wrapper(
            query_fanout.generate,
        )


class QueryFanoutResourceWithStreamingResponse:
    def __init__(self, query_fanout: QueryFanoutResource) -> None:
        self._query_fanout = query_fanout

        self.generate = to_streamed_response_wrapper(
            query_fanout.generate,
        )


class AsyncQueryFanoutResourceWithStreamingResponse:
    def __init__(self, query_fanout: AsyncQueryFanoutResource) -> None:
        self._query_fanout = query_fanout

        self.generate = async_to_streamed_response_wrapper(
            query_fanout.generate,
        )
