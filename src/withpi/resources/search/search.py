# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import search_rank_params, search_embed_params
from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .consistency import (
    ConsistencyResource,
    AsyncConsistencyResource,
    ConsistencyResourceWithRawResponse,
    AsyncConsistencyResourceWithRawResponse,
    ConsistencyResourceWithStreamingResponse,
    AsyncConsistencyResourceWithStreamingResponse,
)
from .groundedness import (
    GroundednessResource,
    AsyncGroundednessResource,
    GroundednessResourceWithRawResponse,
    AsyncGroundednessResourceWithRawResponse,
    GroundednessResourceWithStreamingResponse,
    AsyncGroundednessResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.search_rank_response import SearchRankResponse
from ...types.search_embed_response import SearchEmbedResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def groundedness(self) -> GroundednessResource:
        return GroundednessResource(self._client)

    @cached_property
    def consistency(self) -> ConsistencyResource:
        return ConsistencyResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def embed(
        self,
        *,
        query: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchEmbedResponse:
        """Creates embeddings of provided text input for Search applications.

        Returns 256
        dimensional embeddings with the same length as the input query parameter.

        Args:
          query: List of queries or documents to embed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/embed",
            body=maybe_transform({"query": query}, search_embed_params.SearchEmbedParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchEmbedResponse,
        )

    def rank(
        self,
        *,
        passages: SequenceNotStr[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchRankResponse:
        """Rank passages based on their relevance to a query.

        This will return a score for
        each passage indicating its relevance to the query. Scores are returned in the
        same order as the input passages.

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
                search_rank_params.SearchRankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchRankResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def groundedness(self) -> AsyncGroundednessResource:
        return AsyncGroundednessResource(self._client)

    @cached_property
    def consistency(self) -> AsyncConsistencyResource:
        return AsyncConsistencyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def embed(
        self,
        *,
        query: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchEmbedResponse:
        """Creates embeddings of provided text input for Search applications.

        Returns 256
        dimensional embeddings with the same length as the input query parameter.

        Args:
          query: List of queries or documents to embed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/embed",
            body=await async_maybe_transform({"query": query}, search_embed_params.SearchEmbedParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchEmbedResponse,
        )

    async def rank(
        self,
        *,
        passages: SequenceNotStr[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchRankResponse:
        """Rank passages based on their relevance to a query.

        This will return a score for
        each passage indicating its relevance to the query. Scores are returned in the
        same order as the input passages.

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
                search_rank_params.SearchRankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchRankResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.embed = to_raw_response_wrapper(
            search.embed,
        )
        self.rank = to_raw_response_wrapper(
            search.rank,
        )

    @cached_property
    def groundedness(self) -> GroundednessResourceWithRawResponse:
        return GroundednessResourceWithRawResponse(self._search.groundedness)

    @cached_property
    def consistency(self) -> ConsistencyResourceWithRawResponse:
        return ConsistencyResourceWithRawResponse(self._search.consistency)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.embed = async_to_raw_response_wrapper(
            search.embed,
        )
        self.rank = async_to_raw_response_wrapper(
            search.rank,
        )

    @cached_property
    def groundedness(self) -> AsyncGroundednessResourceWithRawResponse:
        return AsyncGroundednessResourceWithRawResponse(self._search.groundedness)

    @cached_property
    def consistency(self) -> AsyncConsistencyResourceWithRawResponse:
        return AsyncConsistencyResourceWithRawResponse(self._search.consistency)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.embed = to_streamed_response_wrapper(
            search.embed,
        )
        self.rank = to_streamed_response_wrapper(
            search.rank,
        )

    @cached_property
    def groundedness(self) -> GroundednessResourceWithStreamingResponse:
        return GroundednessResourceWithStreamingResponse(self._search.groundedness)

    @cached_property
    def consistency(self) -> ConsistencyResourceWithStreamingResponse:
        return ConsistencyResourceWithStreamingResponse(self._search.consistency)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.embed = async_to_streamed_response_wrapper(
            search.embed,
        )
        self.rank = async_to_streamed_response_wrapper(
            search.rank,
        )

    @cached_property
    def groundedness(self) -> AsyncGroundednessResourceWithStreamingResponse:
        return AsyncGroundednessResourceWithStreamingResponse(self._search.groundedness)

    @cached_property
    def consistency(self) -> AsyncConsistencyResourceWithStreamingResponse:
        return AsyncConsistencyResourceWithStreamingResponse(self._search.consistency)
