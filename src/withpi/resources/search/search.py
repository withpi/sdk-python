# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .query_fanout import (
    QueryFanoutResource,
    AsyncQueryFanoutResource,
    QueryFanoutResourceWithRawResponse,
    AsyncQueryFanoutResourceWithRawResponse,
    QueryFanoutResourceWithStreamingResponse,
    AsyncQueryFanoutResourceWithStreamingResponse,
)
from .query_classifier.query_classifier import (
    QueryClassifierResource,
    AsyncQueryClassifierResource,
    QueryClassifierResourceWithRawResponse,
    AsyncQueryClassifierResourceWithRawResponse,
    QueryClassifierResourceWithStreamingResponse,
    AsyncQueryClassifierResourceWithStreamingResponse,
)

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def query_fanout(self) -> QueryFanoutResource:
        return QueryFanoutResource(self._client)

    @cached_property
    def query_classifier(self) -> QueryClassifierResource:
        return QueryClassifierResource(self._client)

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


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def query_fanout(self) -> AsyncQueryFanoutResource:
        return AsyncQueryFanoutResource(self._client)

    @cached_property
    def query_classifier(self) -> AsyncQueryClassifierResource:
        return AsyncQueryClassifierResource(self._client)

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


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def query_fanout(self) -> QueryFanoutResourceWithRawResponse:
        return QueryFanoutResourceWithRawResponse(self._search.query_fanout)

    @cached_property
    def query_classifier(self) -> QueryClassifierResourceWithRawResponse:
        return QueryClassifierResourceWithRawResponse(self._search.query_classifier)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def query_fanout(self) -> AsyncQueryFanoutResourceWithRawResponse:
        return AsyncQueryFanoutResourceWithRawResponse(self._search.query_fanout)

    @cached_property
    def query_classifier(self) -> AsyncQueryClassifierResourceWithRawResponse:
        return AsyncQueryClassifierResourceWithRawResponse(self._search.query_classifier)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def query_fanout(self) -> QueryFanoutResourceWithStreamingResponse:
        return QueryFanoutResourceWithStreamingResponse(self._search.query_fanout)

    @cached_property
    def query_classifier(self) -> QueryClassifierResourceWithStreamingResponse:
        return QueryClassifierResourceWithStreamingResponse(self._search.query_classifier)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def query_fanout(self) -> AsyncQueryFanoutResourceWithStreamingResponse:
        return AsyncQueryFanoutResourceWithStreamingResponse(self._search.query_fanout)

    @cached_property
    def query_classifier(self) -> AsyncQueryClassifierResourceWithStreamingResponse:
        return AsyncQueryClassifierResourceWithStreamingResponse(self._search.query_classifier)
