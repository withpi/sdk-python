# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.tune import prompt_optimize_params
from ...._base_client import make_request_options
from ....types.optimization_status import OptimizationStatus
from ....types.shared_params.contract import Contract

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)

    def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizationStatus:
        """
        Polls the status of a prompt optimization job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/tune/prompt/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationStatus,
        )

    def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[prompt_optimize_params.Example],
        model_id: Literal["gpt-4o-mini", "mock-llm"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizationStatus:
        """
        Do Pi Prompt optimization.

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          model_id: The model to use for generating responses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tune/prompt",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "model_id": model_id,
                },
                prompt_optimize_params.PromptOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationStatus,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)

    async def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizationStatus:
        """
        Polls the status of a prompt optimization job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/tune/prompt/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationStatus,
        )

    async def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[prompt_optimize_params.Example],
        model_id: Literal["gpt-4o-mini", "mock-llm"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizationStatus:
        """
        Do Pi Prompt optimization.

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          model_id: The model to use for generating responses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tune/prompt",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "model_id": model_id,
                },
                prompt_optimize_params.PromptOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationStatus,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get = to_raw_response_wrapper(
            prompt.get,
        )
        self.optimize = to_raw_response_wrapper(
            prompt.optimize,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._prompt.messages)


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get = async_to_raw_response_wrapper(
            prompt.get,
        )
        self.optimize = async_to_raw_response_wrapper(
            prompt.optimize,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._prompt.messages)


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get = to_streamed_response_wrapper(
            prompt.get,
        )
        self.optimize = to_streamed_response_wrapper(
            prompt.optimize,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._prompt.messages)


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get = async_to_streamed_response_wrapper(
            prompt.get,
        )
        self.optimize = async_to_streamed_response_wrapper(
            prompt.optimize,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._prompt.messages)
