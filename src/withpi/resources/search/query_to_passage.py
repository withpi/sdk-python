# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.search import query_to_passage_rank_documents_params
from ...types.search.query_to_passage_rank_documents_response import QueryToPassageRankDocumentsResponse

__all__ = ["QueryToPassageResource", "AsyncQueryToPassageResource"]


class QueryToPassageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryToPassageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return QueryToPassageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryToPassageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return QueryToPassageResourceWithStreamingResponse(self)

    def rank_documents(
        self,
        *,
        passages: List[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryToPassageRankDocumentsResponse:
        """Ranks documents based on their relevance to the query.

        This will return a score
        for each passage indicating its relevance to the query. Scores are returned in
        the same order as the input passages.

        Args:
          passages: The passages to rank

          query: The query to compare against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/query_to_passage/score",
            body=maybe_transform(
                {
                    "passages": passages,
                    "query": query,
                },
                query_to_passage_rank_documents_params.QueryToPassageRankDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryToPassageRankDocumentsResponse,
        )


class AsyncQueryToPassageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryToPassageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryToPassageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryToPassageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncQueryToPassageResourceWithStreamingResponse(self)

    async def rank_documents(
        self,
        *,
        passages: List[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryToPassageRankDocumentsResponse:
        """Ranks documents based on their relevance to the query.

        This will return a score
        for each passage indicating its relevance to the query. Scores are returned in
        the same order as the input passages.

        Args:
          passages: The passages to rank

          query: The query to compare against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/query_to_passage/score",
            body=await async_maybe_transform(
                {
                    "passages": passages,
                    "query": query,
                },
                query_to_passage_rank_documents_params.QueryToPassageRankDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryToPassageRankDocumentsResponse,
        )


class QueryToPassageResourceWithRawResponse:
    def __init__(self, query_to_passage: QueryToPassageResource) -> None:
        self._query_to_passage = query_to_passage

        self.rank_documents = to_raw_response_wrapper(
            query_to_passage.rank_documents,
        )


class AsyncQueryToPassageResourceWithRawResponse:
    def __init__(self, query_to_passage: AsyncQueryToPassageResource) -> None:
        self._query_to_passage = query_to_passage

        self.rank_documents = async_to_raw_response_wrapper(
            query_to_passage.rank_documents,
        )


class QueryToPassageResourceWithStreamingResponse:
    def __init__(self, query_to_passage: QueryToPassageResource) -> None:
        self._query_to_passage = query_to_passage

        self.rank_documents = to_streamed_response_wrapper(
            query_to_passage.rank_documents,
        )


class AsyncQueryToPassageResourceWithStreamingResponse:
    def __init__(self, query_to_passage: AsyncQueryToPassageResource) -> None:
        self._query_to_passage = query_to_passage

        self.rank_documents = async_to_streamed_response_wrapper(
            query_to_passage.rank_documents,
        )
