# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
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
from ...types.search import query_classifier_classify_params
from ...types.search.query_classifier_classify_response import QueryClassifierClassifyResponse

__all__ = ["QueryClassifierResource", "AsyncQueryClassifierResource"]


class QueryClassifierResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return QueryClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return QueryClassifierResourceWithStreamingResponse(self)

    def classify(
        self,
        *,
        classes: Iterable[query_classifier_classify_params.Class],
        queries: SequenceNotStr[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        examples: Optional[Iterable[query_classifier_classify_params.Example]] | NotGiven = NOT_GIVEN,
        mode: Literal["generative", "probabilistic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryClassifierClassifyResponse:
        """
        Classifies queries into provided classes based on a custom taxonomy.

        Args:
          classes: The list of class definitions to classify the queries into. Must be <= 20.

          queries: The list of queries to classify. Must be <= 10.

          batch_size: Number of inputs to generate in one LLM call. Must be <=10.

          examples: Optional list of examples to provide as few-shot examples for the classifier.
              Must be <= 20.

          mode: The mode to use for the classification. The probabilistic mode returns
              probabilities for each class.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/query_classifier/classify",
            body=maybe_transform(
                {
                    "classes": classes,
                    "queries": queries,
                    "batch_size": batch_size,
                    "examples": examples,
                    "mode": mode,
                },
                query_classifier_classify_params.QueryClassifierClassifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryClassifierClassifyResponse,
        )


class AsyncQueryClassifierResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncQueryClassifierResourceWithStreamingResponse(self)

    async def classify(
        self,
        *,
        classes: Iterable[query_classifier_classify_params.Class],
        queries: SequenceNotStr[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        examples: Optional[Iterable[query_classifier_classify_params.Example]] | NotGiven = NOT_GIVEN,
        mode: Literal["generative", "probabilistic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryClassifierClassifyResponse:
        """
        Classifies queries into provided classes based on a custom taxonomy.

        Args:
          classes: The list of class definitions to classify the queries into. Must be <= 20.

          queries: The list of queries to classify. Must be <= 10.

          batch_size: Number of inputs to generate in one LLM call. Must be <=10.

          examples: Optional list of examples to provide as few-shot examples for the classifier.
              Must be <= 20.

          mode: The mode to use for the classification. The probabilistic mode returns
              probabilities for each class.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/query_classifier/classify",
            body=await async_maybe_transform(
                {
                    "classes": classes,
                    "queries": queries,
                    "batch_size": batch_size,
                    "examples": examples,
                    "mode": mode,
                },
                query_classifier_classify_params.QueryClassifierClassifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryClassifierClassifyResponse,
        )


class QueryClassifierResourceWithRawResponse:
    def __init__(self, query_classifier: QueryClassifierResource) -> None:
        self._query_classifier = query_classifier

        self.classify = to_raw_response_wrapper(
            query_classifier.classify,
        )


class AsyncQueryClassifierResourceWithRawResponse:
    def __init__(self, query_classifier: AsyncQueryClassifierResource) -> None:
        self._query_classifier = query_classifier

        self.classify = async_to_raw_response_wrapper(
            query_classifier.classify,
        )


class QueryClassifierResourceWithStreamingResponse:
    def __init__(self, query_classifier: QueryClassifierResource) -> None:
        self._query_classifier = query_classifier

        self.classify = to_streamed_response_wrapper(
            query_classifier.classify,
        )


class AsyncQueryClassifierResourceWithStreamingResponse:
    def __init__(self, query_classifier: AsyncQueryClassifierResource) -> None:
        self._query_classifier = query_classifier

        self.classify = async_to_streamed_response_wrapper(
            query_classifier.classify,
        )
