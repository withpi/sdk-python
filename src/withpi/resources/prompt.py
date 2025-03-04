# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import prompt_optimize_params, prompt_list_optimization_jobs_params
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
from ..types.shared.state import State
from ..types.shared_params.example import Example
from ..types.shared_params.contract import Contract
from ..types.shared.prompt_optimization_status import PromptOptimizationStatus
from ..types.prompt_list_optimization_jobs_response import PromptListOptimizationJobsResponse

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

    def retrieve(
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
        Checks the status of a Prompt Optimization job

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

    def cancel_optimization_job(
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
        Cancels a Prompt Optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/prompt/optimize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list_optimization_jobs(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptListOptimizationJobsResponse:
        """
        Lists the Prompt Optimization Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/prompt/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"state": state}, prompt_list_optimization_jobs_params.PromptListOptimizationJobsParams
                ),
            ),
            cast_to=PromptListOptimizationJobsResponse,
        )

    def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"],
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
        Launches a Prompt Optimization job

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          tuning_algorithm: The tuning algorithm to use

          dspy_optimization_type: The DSPY teleprompter/optimizer to use. This only applies for the DSPY. Leave it
              as None if tuning_algorithm != DSPY.

          use_chain_of_thought: Decides if to use chain of thought or not. This only applies for the DSPY. Leave
              it as None if tuning_algorithm != DSPY.

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
        Opens a message stream about a Prompt Optimization job

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

    async def retrieve(
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
        Checks the status of a Prompt Optimization job

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

    async def cancel_optimization_job(
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
        Cancels a Prompt Optimization job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/prompt/optimize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list_optimization_jobs(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptListOptimizationJobsResponse:
        """
        Lists the Prompt Optimization Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/prompt/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, prompt_list_optimization_jobs_params.PromptListOptimizationJobsParams
                ),
            ),
            cast_to=PromptListOptimizationJobsResponse,
        )

    async def optimize(
        self,
        *,
        contract: Contract,
        examples: Iterable[Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"],
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
        Launches a Prompt Optimization job

        Args:
          contract: The contract to optimize

          examples: The examples to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          tuning_algorithm: The tuning algorithm to use

          dspy_optimization_type: The DSPY teleprompter/optimizer to use. This only applies for the DSPY. Leave it
              as None if tuning_algorithm != DSPY.

          use_chain_of_thought: Decides if to use chain of thought or not. This only applies for the DSPY. Leave
              it as None if tuning_algorithm != DSPY.

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
        Opens a message stream about a Prompt Optimization job

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

        self.retrieve = to_raw_response_wrapper(
            prompt.retrieve,
        )
        self.cancel_optimization_job = to_raw_response_wrapper(
            prompt.cancel_optimization_job,
        )
        self.list_optimization_jobs = to_raw_response_wrapper(
            prompt.list_optimization_jobs,
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

        self.retrieve = async_to_raw_response_wrapper(
            prompt.retrieve,
        )
        self.cancel_optimization_job = async_to_raw_response_wrapper(
            prompt.cancel_optimization_job,
        )
        self.list_optimization_jobs = async_to_raw_response_wrapper(
            prompt.list_optimization_jobs,
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

        self.retrieve = to_streamed_response_wrapper(
            prompt.retrieve,
        )
        self.cancel_optimization_job = to_streamed_response_wrapper(
            prompt.cancel_optimization_job,
        )
        self.list_optimization_jobs = to_streamed_response_wrapper(
            prompt.list_optimization_jobs,
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

        self.retrieve = async_to_streamed_response_wrapper(
            prompt.retrieve,
        )
        self.cancel_optimization_job = async_to_streamed_response_wrapper(
            prompt.cancel_optimization_job,
        )
        self.list_optimization_jobs = async_to_streamed_response_wrapper(
            prompt.list_optimization_jobs,
        )
        self.optimize = async_to_streamed_response_wrapper(
            prompt.optimize,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            prompt.stream_messages,
        )
