# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .groundedness import (
    GroundednessResource,
    AsyncGroundednessResource,
    GroundednessResourceWithRawResponse,
    AsyncGroundednessResourceWithRawResponse,
    GroundednessResourceWithStreamingResponse,
    AsyncGroundednessResourceWithStreamingResponse,
)
from .query_classifier import (
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
    def query_classifier(self) -> QueryClassifierResource:
        return QueryClassifierResource(self._client)

    @cached_property
    def groundedness(self) -> GroundednessResource:
        return GroundednessResource(self._client)

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
    def query_classifier(self) -> AsyncQueryClassifierResource:
        return AsyncQueryClassifierResource(self._client)

    @cached_property
    def groundedness(self) -> AsyncGroundednessResource:
        return AsyncGroundednessResource(self._client)

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
    def query_classifier(self) -> QueryClassifierResourceWithRawResponse:
        return QueryClassifierResourceWithRawResponse(self._search.query_classifier)

    @cached_property
    def groundedness(self) -> GroundednessResourceWithRawResponse:
        return GroundednessResourceWithRawResponse(self._search.groundedness)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def query_classifier(self) -> AsyncQueryClassifierResourceWithRawResponse:
        return AsyncQueryClassifierResourceWithRawResponse(self._search.query_classifier)

    @cached_property
    def groundedness(self) -> AsyncGroundednessResourceWithRawResponse:
        return AsyncGroundednessResourceWithRawResponse(self._search.groundedness)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def query_classifier(self) -> QueryClassifierResourceWithStreamingResponse:
        return QueryClassifierResourceWithStreamingResponse(self._search.query_classifier)

    @cached_property
    def groundedness(self) -> GroundednessResourceWithStreamingResponse:
        return GroundednessResourceWithStreamingResponse(self._search.groundedness)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def query_classifier(self) -> AsyncQueryClassifierResourceWithStreamingResponse:
        return AsyncQueryClassifierResourceWithStreamingResponse(self._search.query_classifier)

    @cached_property
    def groundedness(self) -> AsyncGroundednessResourceWithStreamingResponse:
        return AsyncGroundednessResourceWithStreamingResponse(self._search.groundedness)
