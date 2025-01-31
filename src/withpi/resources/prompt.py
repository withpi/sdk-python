# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import prompt_optimize_params
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
from ..types.shared_params.contract import Contract
from ..types.prompt_optimization_status import PromptOptimizationStatus

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)

    def get_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Checks on a prompt optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/prompt/optimize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[prompt_optimize_params.Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "mock-llm"],
        tuning_algorithm: Literal["PI", "DSPY"],
        dspy_optimization_type: Optional[Literal["BOOTSTRAP_FEW_SHOT", "COPRO", "MIPROv2"]] | NotGiven = NOT_GIVEN,
        use_chain_of_thought: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Start a prompt optimization job

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          tuning_algorithm: The tuning algorithm to use

          dspy_optimization_type: The DSPY teleprompter/optimizer to use. This only applies for the DSPY otherwise
              leave it as None.

          use_chain_of_thought: Decides if to use chain of thought or not. This only applies for the DSPY
              otherwise leave it as False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prompt/optimize",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "initial_system_instruction": initial_system_instruction,
                    "model_id": model_id,
                    "tuning_algorithm": tuning_algorithm,
                    "dspy_optimization_type": dspy_optimization_type,
                    "use_chain_of_thought": use_chain_of_thought,
                },
                prompt_optimize_params.PromptOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    def stream_messages(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Opens a message stream about a prompt optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/prompt/optimize/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)

    async def get_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Checks on a prompt optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/prompt/optimize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    async def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[prompt_optimize_params.Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "mock-llm"],
        tuning_algorithm: Literal["PI", "DSPY"],
        dspy_optimization_type: Optional[Literal["BOOTSTRAP_FEW_SHOT", "COPRO", "MIPROv2"]] | NotGiven = NOT_GIVEN,
        use_chain_of_thought: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Start a prompt optimization job

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          tuning_algorithm: The tuning algorithm to use

          dspy_optimization_type: The DSPY teleprompter/optimizer to use. This only applies for the DSPY otherwise
              leave it as None.

          use_chain_of_thought: Decides if to use chain of thought or not. This only applies for the DSPY
              otherwise leave it as False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prompt/optimize",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "initial_system_instruction": initial_system_instruction,
                    "model_id": model_id,
                    "tuning_algorithm": tuning_algorithm,
                    "dspy_optimization_type": dspy_optimization_type,
                    "use_chain_of_thought": use_chain_of_thought,
                },
                prompt_optimize_params.PromptOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    async def stream_messages(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Opens a message stream about a prompt optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/prompt/optimize/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get_status = to_raw_response_wrapper(
            prompt.get_status,
        )
        self.optimize = to_raw_response_wrapper(
            prompt.optimize,
        )
        self.stream_messages = to_raw_response_wrapper(
            prompt.stream_messages,
        )


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get_status = async_to_raw_response_wrapper(
            prompt.get_status,
        )
        self.optimize = async_to_raw_response_wrapper(
            prompt.optimize,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            prompt.stream_messages,
        )


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get_status = to_streamed_response_wrapper(
            prompt.get_status,
        )
        self.optimize = to_streamed_response_wrapper(
            prompt.optimize,
        )
        self.stream_messages = to_streamed_response_wrapper(
            prompt.stream_messages,
        )


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get_status = async_to_streamed_response_wrapper(
            prompt.get_status,
        )
        self.optimize = async_to_streamed_response_wrapper(
            prompt.optimize,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            prompt.stream_messages,
        )
