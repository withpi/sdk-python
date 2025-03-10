# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import rag_classify_query_params, rag_generate_fanout_params
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
from ..types.rag_classify_query_response import RagClassifyQueryResponse
from ..types.rag_generate_fanout_response import RagGenerateFanoutResponse
from ..types.shared_params.query_fanout_example import QueryFanoutExample

__all__ = ["RagResource", "AsyncRagResource"]


class RagResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return RagResourceWithStreamingResponse(self)

    def classify_query(
        self,
        *,
        classes: Iterable[rag_classify_query_params.Class],
        queries: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        examples: Optional[Iterable[rag_classify_query_params.Example]] | NotGiven = NOT_GIVEN,
        mode: Literal["generative", "probabilistic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagClassifyQueryResponse:
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
            "/rag/query_classify",
            body=maybe_transform(
                {
                    "classes": classes,
                    "queries": queries,
                    "batch_size": batch_size,
                    "examples": examples,
                    "mode": mode,
                },
                rag_classify_query_params.RagClassifyQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagClassifyQueryResponse,
        )

    def generate_fanout(
        self,
        *,
        queries: List[str],
        example_fanout_queries: Iterable[QueryFanoutExample] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagGenerateFanoutResponse:
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
            "/rag/query_fanout",
            body=maybe_transform(
                {
                    "queries": queries,
                    "example_fanout_queries": example_fanout_queries,
                    "num_fanout_queries": num_fanout_queries,
                },
                rag_generate_fanout_params.RagGenerateFanoutParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagGenerateFanoutResponse,
        )


class AsyncRagResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncRagResourceWithStreamingResponse(self)

    async def classify_query(
        self,
        *,
        classes: Iterable[rag_classify_query_params.Class],
        queries: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        examples: Optional[Iterable[rag_classify_query_params.Example]] | NotGiven = NOT_GIVEN,
        mode: Literal["generative", "probabilistic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagClassifyQueryResponse:
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
            "/rag/query_classify",
            body=await async_maybe_transform(
                {
                    "classes": classes,
                    "queries": queries,
                    "batch_size": batch_size,
                    "examples": examples,
                    "mode": mode,
                },
                rag_classify_query_params.RagClassifyQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagClassifyQueryResponse,
        )

    async def generate_fanout(
        self,
        *,
        queries: List[str],
        example_fanout_queries: Iterable[QueryFanoutExample] | NotGiven = NOT_GIVEN,
        num_fanout_queries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RagGenerateFanoutResponse:
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
            "/rag/query_fanout",
            body=await async_maybe_transform(
                {
                    "queries": queries,
                    "example_fanout_queries": example_fanout_queries,
                    "num_fanout_queries": num_fanout_queries,
                },
                rag_generate_fanout_params.RagGenerateFanoutParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RagGenerateFanoutResponse,
        )


class RagResourceWithRawResponse:
    def __init__(self, rag: RagResource) -> None:
        self._rag = rag

        self.classify_query = to_raw_response_wrapper(
            rag.classify_query,
        )
        self.generate_fanout = to_raw_response_wrapper(
            rag.generate_fanout,
        )


class AsyncRagResourceWithRawResponse:
    def __init__(self, rag: AsyncRagResource) -> None:
        self._rag = rag

        self.classify_query = async_to_raw_response_wrapper(
            rag.classify_query,
        )
        self.generate_fanout = async_to_raw_response_wrapper(
            rag.generate_fanout,
        )


class RagResourceWithStreamingResponse:
    def __init__(self, rag: RagResource) -> None:
        self._rag = rag

        self.classify_query = to_streamed_response_wrapper(
            rag.classify_query,
        )
        self.generate_fanout = to_streamed_response_wrapper(
            rag.generate_fanout,
        )


class AsyncRagResourceWithStreamingResponse:
    def __init__(self, rag: AsyncRagResource) -> None:
        self._rag = rag

        self.classify_query = async_to_streamed_response_wrapper(
            rag.classify_query,
        )
        self.generate_fanout = async_to_streamed_response_wrapper(
            rag.generate_fanout,
        )
