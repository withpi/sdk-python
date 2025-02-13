# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

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
from ...._base_client import make_request_options
from ....types.model.rl import ppo_start_job_params
from ....types.model.rl.rl_ppo_status import RlPpoStatus
from ....types.shared_params.contract import Contract

__all__ = ["PpoResource", "AsyncPpoResource"]


class PpoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PpoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PpoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PpoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return PpoResourceWithStreamingResponse(self)

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
    ) -> RlPpoStatus:
        """
        Get the current status of the RL PPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/model/rl/ppo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlPpoStatus,
        )

    def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[ppo_start_job_params.Example],
        model: Literal["LLAMA_3.2_1B"],
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlPpoStatus:
        """Initialize the Proximal Policy Optimization (PPO) reinforcement learning job.

        We
        implement Low-Rank Adaptation (LoRA) for the reinforcement learning process,
        with a fixed rank of 16.

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the RL tuning process

          model: The model to start the RL process

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/model/rl/ppo",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "model": model,
                    "learning_rate": learning_rate,
                    "num_train_epochs": num_train_epochs,
                },
                ppo_start_job_params.PpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlPpoStatus,
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
        Streams messages from the RL PPO job

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
            f"/model/rl/ppo/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncPpoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPpoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPpoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPpoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncPpoResourceWithStreamingResponse(self)

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
    ) -> RlPpoStatus:
        """
        Get the current status of the RL PPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/model/rl/ppo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlPpoStatus,
        )

    async def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[ppo_start_job_params.Example],
        model: Literal["LLAMA_3.2_1B"],
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlPpoStatus:
        """Initialize the Proximal Policy Optimization (PPO) reinforcement learning job.

        We
        implement Low-Rank Adaptation (LoRA) for the reinforcement learning process,
        with a fixed rank of 16.

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the RL tuning process

          model: The model to start the RL process

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/model/rl/ppo",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "model": model,
                    "learning_rate": learning_rate,
                    "num_train_epochs": num_train_epochs,
                },
                ppo_start_job_params.PpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlPpoStatus,
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
        Streams messages from the RL PPO job

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
            f"/model/rl/ppo/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class PpoResourceWithRawResponse:
    def __init__(self, ppo: PpoResource) -> None:
        self._ppo = ppo

        self.retrieve = to_raw_response_wrapper(
            ppo.retrieve,
        )
        self.start_job = to_raw_response_wrapper(
            ppo.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            ppo.stream_messages,
        )


class AsyncPpoResourceWithRawResponse:
    def __init__(self, ppo: AsyncPpoResource) -> None:
        self._ppo = ppo

        self.retrieve = async_to_raw_response_wrapper(
            ppo.retrieve,
        )
        self.start_job = async_to_raw_response_wrapper(
            ppo.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            ppo.stream_messages,
        )


class PpoResourceWithStreamingResponse:
    def __init__(self, ppo: PpoResource) -> None:
        self._ppo = ppo

        self.retrieve = to_streamed_response_wrapper(
            ppo.retrieve,
        )
        self.start_job = to_streamed_response_wrapper(
            ppo.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            ppo.stream_messages,
        )


class AsyncPpoResourceWithStreamingResponse:
    def __init__(self, ppo: AsyncPpoResource) -> None:
        self._ppo = ppo

        self.retrieve = async_to_streamed_response_wrapper(
            ppo.retrieve,
        )
        self.start_job = async_to_streamed_response_wrapper(
            ppo.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            ppo.stream_messages,
        )
