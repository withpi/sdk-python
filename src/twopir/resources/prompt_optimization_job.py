# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import prompt_optimization_job_optimize_params
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

__all__ = ["PromptOptimizationJobResource", "AsyncPromptOptimizationJobResource"]


class PromptOptimizationJobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptOptimizationJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return PromptOptimizationJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptOptimizationJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return PromptOptimizationJobResourceWithStreamingResponse(self)

    def get(
        self,
        job_id: int,
        *,
        optimizer_id: int,
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
        return self._get(
            f"/prompt_optimizers/{optimizer_id}/optimize_job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    def optimize(
        self,
        optimizer_id: int,
        *,
        contract: Contract,
        experiment_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Runs prompt optimization

        Args:
          contract: A collection of dimensions an LLM response must adhere to

          experiment_id: The ID of a completed experiment to use for optimization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/prompt_optimizers/{optimizer_id}/optimize_job",
            body=maybe_transform(
                {
                    "contract": contract,
                    "experiment_id": experiment_id,
                },
                prompt_optimization_job_optimize_params.PromptOptimizationJobOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )


class AsyncPromptOptimizationJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptOptimizationJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptOptimizationJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptOptimizationJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncPromptOptimizationJobResourceWithStreamingResponse(self)

    async def get(
        self,
        job_id: int,
        *,
        optimizer_id: int,
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
        return await self._get(
            f"/prompt_optimizers/{optimizer_id}/optimize_job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )

    async def optimize(
        self,
        optimizer_id: int,
        *,
        contract: Contract,
        experiment_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptOptimizationStatus:
        """
        Runs prompt optimization

        Args:
          contract: A collection of dimensions an LLM response must adhere to

          experiment_id: The ID of a completed experiment to use for optimization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/prompt_optimizers/{optimizer_id}/optimize_job",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "experiment_id": experiment_id,
                },
                prompt_optimization_job_optimize_params.PromptOptimizationJobOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationStatus,
        )


class PromptOptimizationJobResourceWithRawResponse:
    def __init__(self, prompt_optimization_job: PromptOptimizationJobResource) -> None:
        self._prompt_optimization_job = prompt_optimization_job

        self.get = to_raw_response_wrapper(
            prompt_optimization_job.get,
        )
        self.optimize = to_raw_response_wrapper(
            prompt_optimization_job.optimize,
        )


class AsyncPromptOptimizationJobResourceWithRawResponse:
    def __init__(self, prompt_optimization_job: AsyncPromptOptimizationJobResource) -> None:
        self._prompt_optimization_job = prompt_optimization_job

        self.get = async_to_raw_response_wrapper(
            prompt_optimization_job.get,
        )
        self.optimize = async_to_raw_response_wrapper(
            prompt_optimization_job.optimize,
        )


class PromptOptimizationJobResourceWithStreamingResponse:
    def __init__(self, prompt_optimization_job: PromptOptimizationJobResource) -> None:
        self._prompt_optimization_job = prompt_optimization_job

        self.get = to_streamed_response_wrapper(
            prompt_optimization_job.get,
        )
        self.optimize = to_streamed_response_wrapper(
            prompt_optimization_job.optimize,
        )


class AsyncPromptOptimizationJobResourceWithStreamingResponse:
    def __init__(self, prompt_optimization_job: AsyncPromptOptimizationJobResource) -> None:
        self._prompt_optimization_job = prompt_optimization_job

        self.get = async_to_streamed_response_wrapper(
            prompt_optimization_job.get,
        )
        self.optimize = async_to_streamed_response_wrapper(
            prompt_optimization_job.optimize,
        )
