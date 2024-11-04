# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

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
from ...types.contract import dimension_score_params, dimension_generate_params
from ...types.response_metrics import ResponseMetrics
from ...types.shared.dimension import Dimension as SharedDimension
from ...types.shared_params.dimension import Dimension as SharedParamsDimension
from ...types.shared_params.llm_response import LlmResponse

__all__ = ["DimensionResource", "AsyncDimensionResource"]


class DimensionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DimensionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return DimensionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DimensionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return DimensionResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        dimension: SharedParamsDimension,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedDimension:
        """
        Generates more subdimensions associated with a single dimension

        Args:
          dimension: A single dimension along which an LLM response will be scored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/dimensions/generate",
            body=maybe_transform({"dimension": dimension}, dimension_generate_params.DimensionGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedDimension,
        )

    def score(
        self,
        *,
        dimension: SharedParamsDimension,
        llm_input: Dict[str, Union[str, float]],
        llm_response: LlmResponse,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseMetrics:
        """
        Scores a single dimension

        Args:
          dimension: A single dimension along which an LLM response will be scored

          llm_input: Key/Value pairs constituting the input. If the input is just text, use the key
              "query"

          llm_response: The response from the LLM

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/dimensions/score",
            body=maybe_transform(
                {
                    "dimension": dimension,
                    "llm_input": llm_input,
                    "llm_response": llm_response,
                },
                dimension_score_params.DimensionScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseMetrics,
        )


class AsyncDimensionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDimensionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDimensionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDimensionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncDimensionResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        dimension: SharedParamsDimension,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedDimension:
        """
        Generates more subdimensions associated with a single dimension

        Args:
          dimension: A single dimension along which an LLM response will be scored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/dimensions/generate",
            body=await async_maybe_transform(
                {"dimension": dimension}, dimension_generate_params.DimensionGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedDimension,
        )

    async def score(
        self,
        *,
        dimension: SharedParamsDimension,
        llm_input: Dict[str, Union[str, float]],
        llm_response: LlmResponse,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseMetrics:
        """
        Scores a single dimension

        Args:
          dimension: A single dimension along which an LLM response will be scored

          llm_input: Key/Value pairs constituting the input. If the input is just text, use the key
              "query"

          llm_response: The response from the LLM

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/dimensions/score",
            body=await async_maybe_transform(
                {
                    "dimension": dimension,
                    "llm_input": llm_input,
                    "llm_response": llm_response,
                },
                dimension_score_params.DimensionScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseMetrics,
        )


class DimensionResourceWithRawResponse:
    def __init__(self, dimension: DimensionResource) -> None:
        self._dimension = dimension

        self.generate = to_raw_response_wrapper(
            dimension.generate,
        )
        self.score = to_raw_response_wrapper(
            dimension.score,
        )


class AsyncDimensionResourceWithRawResponse:
    def __init__(self, dimension: AsyncDimensionResource) -> None:
        self._dimension = dimension

        self.generate = async_to_raw_response_wrapper(
            dimension.generate,
        )
        self.score = async_to_raw_response_wrapper(
            dimension.score,
        )


class DimensionResourceWithStreamingResponse:
    def __init__(self, dimension: DimensionResource) -> None:
        self._dimension = dimension

        self.generate = to_streamed_response_wrapper(
            dimension.generate,
        )
        self.score = to_streamed_response_wrapper(
            dimension.score,
        )


class AsyncDimensionResourceWithStreamingResponse:
    def __init__(self, dimension: AsyncDimensionResource) -> None:
        self._dimension = dimension

        self.generate = async_to_streamed_response_wrapper(
            dimension.generate,
        )
        self.score = async_to_streamed_response_wrapper(
            dimension.score,
        )
