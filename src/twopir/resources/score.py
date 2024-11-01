# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import score_execute_params
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
from ..types.score_bundle import ScoreBundle

__all__ = ["ScoreResource", "AsyncScoreResource"]


class ScoreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return ScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return ScoreResourceWithStreamingResponse(self)

    def execute(
        self,
        scorer_id: int,
        *,
        input: str | NotGiven = NOT_GIVEN,
        response: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreBundle:
        """
        Executes the provided scorer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/score/{scorer_id}",
            body=maybe_transform(
                {
                    "input": input,
                    "response": response,
                },
                score_execute_params.ScoreExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreBundle,
        )


class AsyncScoreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncScoreResourceWithStreamingResponse(self)

    async def execute(
        self,
        scorer_id: int,
        *,
        input: str | NotGiven = NOT_GIVEN,
        response: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreBundle:
        """
        Executes the provided scorer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/score/{scorer_id}",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "response": response,
                },
                score_execute_params.ScoreExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreBundle,
        )


class ScoreResourceWithRawResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.execute = to_raw_response_wrapper(
            score.execute,
        )


class AsyncScoreResourceWithRawResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.execute = async_to_raw_response_wrapper(
            score.execute,
        )


class ScoreResourceWithStreamingResponse:
    def __init__(self, score: ScoreResource) -> None:
        self._score = score

        self.execute = to_streamed_response_wrapper(
            score.execute,
        )


class AsyncScoreResourceWithStreamingResponse:
    def __init__(self, score: AsyncScoreResource) -> None:
        self._score = score

        self.execute = async_to_streamed_response_wrapper(
            score.execute,
        )
