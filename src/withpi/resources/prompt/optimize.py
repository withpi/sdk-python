# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

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
from ...types.prompt import optimize_list_params, optimize_start_job_params
from ...types.shared_params.example import Example
from ...types.shared_params.scoring_spec import ScoringSpec
from ...types.prompt.optimize_list_response import OptimizeListResponse
from ...types.shared.prompt_optimization_status import PromptOptimizationStatus

__all__ = ["OptimizeResource", "AsyncOptimizeResource"]


class OptimizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptimizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return OptimizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return OptimizeResourceWithStreamingResponse(self)

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

    def list(
        self,
        *,
        state: Optional[Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizeListResponse:
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
                query=maybe_transform({"state": state}, optimize_list_params.OptimizeListParams),
            ),
            cast_to=OptimizeListResponse,
        )

    def cancel(
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

    def start_job(
        self,
        *,
        examples: Iterable[Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"],
        scoring_spec: ScoringSpec,
        tuning_algorithm: Literal["DSPY", "PI"],
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
        Starts a Prompt Optimization job

        Args:
          examples: The examples (input-response pairs) to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          scoring_spec: The scoring spec to optimize

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
                    "examples": examples,
                    "initial_system_instruction": initial_system_instruction,
                    "model_id": model_id,
                    "scoring_spec": scoring_spec,
                    "tuning_algorithm": tuning_algorithm,
                    "dspy_optimization_type": dspy_optimization_type,
                    "use_chain_of_thought": use_chain_of_thought,
                },
                optimize_start_job_params.OptimizeStartJobParams,
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


class AsyncOptimizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptimizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptimizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncOptimizeResourceWithStreamingResponse(self)

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

    async def list(
        self,
        *,
        state: Optional[Literal["QUEUED", "RUNNING", "DONE", "ERROR", "CANCELLED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptimizeListResponse:
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
                query=await async_maybe_transform({"state": state}, optimize_list_params.OptimizeListParams),
            ),
            cast_to=OptimizeListResponse,
        )

    async def cancel(
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

    async def start_job(
        self,
        *,
        examples: Iterable[Example],
        initial_system_instruction: str,
        model_id: Literal["gpt-4o-mini", "llama-3.1-8b", "mock-llm"],
        scoring_spec: ScoringSpec,
        tuning_algorithm: Literal["DSPY", "PI"],
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
        Starts a Prompt Optimization job

        Args:
          examples: The examples (input-response pairs) to train and validate on

          initial_system_instruction: The initial system instruction

          model_id: The model to use for generating responses

          scoring_spec: The scoring spec to optimize

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
                    "examples": examples,
                    "initial_system_instruction": initial_system_instruction,
                    "model_id": model_id,
                    "scoring_spec": scoring_spec,
                    "tuning_algorithm": tuning_algorithm,
                    "dspy_optimization_type": dspy_optimization_type,
                    "use_chain_of_thought": use_chain_of_thought,
                },
                optimize_start_job_params.OptimizeStartJobParams,
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


class OptimizeResourceWithRawResponse:
    def __init__(self, optimize: OptimizeResource) -> None:
        self._optimize = optimize

        self.retrieve = to_raw_response_wrapper(
            optimize.retrieve,
        )
        self.list = to_raw_response_wrapper(
            optimize.list,
        )
        self.cancel = to_raw_response_wrapper(
            optimize.cancel,
        )
        self.start_job = to_raw_response_wrapper(
            optimize.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            optimize.stream_messages,
        )


class AsyncOptimizeResourceWithRawResponse:
    def __init__(self, optimize: AsyncOptimizeResource) -> None:
        self._optimize = optimize

        self.retrieve = async_to_raw_response_wrapper(
            optimize.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            optimize.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            optimize.cancel,
        )
        self.start_job = async_to_raw_response_wrapper(
            optimize.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            optimize.stream_messages,
        )


class OptimizeResourceWithStreamingResponse:
    def __init__(self, optimize: OptimizeResource) -> None:
        self._optimize = optimize

        self.retrieve = to_streamed_response_wrapper(
            optimize.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            optimize.list,
        )
        self.cancel = to_streamed_response_wrapper(
            optimize.cancel,
        )
        self.start_job = to_streamed_response_wrapper(
            optimize.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            optimize.stream_messages,
        )


class AsyncOptimizeResourceWithStreamingResponse:
    def __init__(self, optimize: AsyncOptimizeResource) -> None:
        self._optimize = optimize

        self.retrieve = async_to_streamed_response_wrapper(
            optimize.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            optimize.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            optimize.cancel,
        )
        self.start_job = async_to_streamed_response_wrapper(
            optimize.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            optimize.stream_messages,
        )
