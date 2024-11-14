# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inference_run_params
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
from ..types.inference_run_response import InferenceRunResponse

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        llm_input: inference_run_params.LlmInput,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRunResponse:
        """
        Runs inference, returning a response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/inference/run",
            body=maybe_transform(llm_input, inference_run_params.InferenceRunParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRunResponse,
        )


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        llm_input: inference_run_params.LlmInput,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRunResponse:
        """
        Runs inference, returning a response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/inference/run",
            body=await async_maybe_transform(llm_input, inference_run_params.InferenceRunParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRunResponse,
        )


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.run = to_raw_response_wrapper(
            inference.run,
        )


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.run = async_to_raw_response_wrapper(
            inference.run,
        )


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.run = to_streamed_response_wrapper(
            inference.run,
        )


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.run = async_to_streamed_response_wrapper(
            inference.run,
        )
