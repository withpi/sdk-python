# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.search import groundedness_check_params
from ...types.search.groundedness_check_response import GroundednessCheckResponse

__all__ = ["GroundednessResource", "AsyncGroundednessResource"]


class GroundednessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroundednessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GroundednessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroundednessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GroundednessResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        context: str,
        output: str,
        processing_strategy: Literal["speed_optimized", "balanced", "quality_optimized"] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroundednessCheckResponse:
        """
        Checks if the generated output is grounded in the provided context.

        Args:
          context: The context to check groundedness against.

          output: The generated output to check for groundedness.

          processing_strategy: The processing strategy to use for the groundedness check.

          query: The optional query that generated the output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/groundedness/check",
            body=maybe_transform(
                {
                    "context": context,
                    "output": output,
                    "processing_strategy": processing_strategy,
                    "query": query,
                },
                groundedness_check_params.GroundednessCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroundednessCheckResponse,
        )


class AsyncGroundednessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroundednessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroundednessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroundednessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGroundednessResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        context: str,
        output: str,
        processing_strategy: Literal["speed_optimized", "balanced", "quality_optimized"] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroundednessCheckResponse:
        """
        Checks if the generated output is grounded in the provided context.

        Args:
          context: The context to check groundedness against.

          output: The generated output to check for groundedness.

          processing_strategy: The processing strategy to use for the groundedness check.

          query: The optional query that generated the output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/groundedness/check",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "output": output,
                    "processing_strategy": processing_strategy,
                    "query": query,
                },
                groundedness_check_params.GroundednessCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroundednessCheckResponse,
        )


class GroundednessResourceWithRawResponse:
    def __init__(self, groundedness: GroundednessResource) -> None:
        self._groundedness = groundedness

        self.check = to_raw_response_wrapper(
            groundedness.check,
        )


class AsyncGroundednessResourceWithRawResponse:
    def __init__(self, groundedness: AsyncGroundednessResource) -> None:
        self._groundedness = groundedness

        self.check = async_to_raw_response_wrapper(
            groundedness.check,
        )


class GroundednessResourceWithStreamingResponse:
    def __init__(self, groundedness: GroundednessResource) -> None:
        self._groundedness = groundedness

        self.check = to_streamed_response_wrapper(
            groundedness.check,
        )


class AsyncGroundednessResourceWithStreamingResponse:
    def __init__(self, groundedness: AsyncGroundednessResource) -> None:
        self._groundedness = groundedness

        self.check = async_to_streamed_response_wrapper(
            groundedness.check,
        )
