# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ....types.model.rl import grpo_list_params, grpo_download_params, grpo_start_job_params
from ....types.shared.state import State
from ....types.shared.rl_grpo_status import RlGrpoStatus
from ....types.shared_params.contract import Contract
from ....types.shared_params.lora_config import LoraConfig
from ....types.model.rl.grpo_list_response import GrpoListResponse
from ....types.shared.finetuning_base_model import FinetuningBaseModel

__all__ = ["GrpoResource", "AsyncGrpoResource"]


class GrpoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GrpoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GrpoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrpoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GrpoResourceWithStreamingResponse(self)

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
    ) -> RlGrpoStatus:
        """
        Checks the status of a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/model/rl/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
        )

    def list(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoListResponse:
        """
        Lists the RL GRPO Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/model/rl/grpo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, grpo_list_params.GrpoListParams),
            ),
            cast_to=GrpoListResponse,
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
        Cancels a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/model/rl/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def download(
        self,
        job_id: str,
        *,
        serving_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Allows downloading a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/model/rl/grpo/{job_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"serving_id": serving_id}, grpo_download_params.GrpoDownloadParams),
            ),
            cast_to=str,
        )

    def load(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Loads a RL GRPO model into serving for a limited period of time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/model/rl/grpo/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
        )

    def start_job(
        self,
        *,
        base_rl_model: FinetuningBaseModel,
        contract: Contract,
        examples: Iterable[grpo_start_job_params.Example],
        learning_rate: float,
        lora_config: LoraConfig,
        num_train_epochs: int,
        system_prompt: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Launches a RL GRPO job

        Args:
          base_rl_model: The base model to start the RL tunning process

          contract: The contract to use in the GRPO tuning process

          examples: Examples to use in the RL tuning process

          learning_rate: GRPO learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: GRPO number of train epochs

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/model/rl/grpo",
            body=maybe_transform(
                {
                    "base_rl_model": base_rl_model,
                    "contract": contract,
                    "examples": examples,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "system_prompt": system_prompt,
                },
                grpo_start_job_params.GrpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
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
        Opens a message stream about a RL GRPO job

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
            f"/model/rl/grpo/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGrpoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGrpoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGrpoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrpoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGrpoResourceWithStreamingResponse(self)

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
    ) -> RlGrpoStatus:
        """
        Checks the status of a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/model/rl/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
        )

    async def list(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoListResponse:
        """
        Lists the RL GRPO Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/model/rl/grpo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"state": state}, grpo_list_params.GrpoListParams),
            ),
            cast_to=GrpoListResponse,
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
        Cancels a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/model/rl/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def download(
        self,
        job_id: str,
        *,
        serving_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Allows downloading a RL GRPO job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/model/rl/grpo/{job_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"serving_id": serving_id}, grpo_download_params.GrpoDownloadParams),
            ),
            cast_to=str,
        )

    async def load(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Loads a RL GRPO model into serving for a limited period of time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/model/rl/grpo/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
        )

    async def start_job(
        self,
        *,
        base_rl_model: FinetuningBaseModel,
        contract: Contract,
        examples: Iterable[grpo_start_job_params.Example],
        learning_rate: float,
        lora_config: LoraConfig,
        num_train_epochs: int,
        system_prompt: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Launches a RL GRPO job

        Args:
          base_rl_model: The base model to start the RL tunning process

          contract: The contract to use in the GRPO tuning process

          examples: Examples to use in the RL tuning process

          learning_rate: GRPO learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: GRPO number of train epochs

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/model/rl/grpo",
            body=await async_maybe_transform(
                {
                    "base_rl_model": base_rl_model,
                    "contract": contract,
                    "examples": examples,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "system_prompt": system_prompt,
                },
                grpo_start_job_params.GrpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RlGrpoStatus,
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
        Opens a message stream about a RL GRPO job

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
            f"/model/rl/grpo/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GrpoResourceWithRawResponse:
    def __init__(self, grpo: GrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = to_raw_response_wrapper(
            grpo.retrieve,
        )
        self.list = to_raw_response_wrapper(
            grpo.list,
        )
        self.cancel = to_raw_response_wrapper(
            grpo.cancel,
        )
        self.download = to_raw_response_wrapper(
            grpo.download,
        )
        self.load = to_raw_response_wrapper(
            grpo.load,
        )
        self.start_job = to_raw_response_wrapper(
            grpo.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            grpo.stream_messages,
        )


class AsyncGrpoResourceWithRawResponse:
    def __init__(self, grpo: AsyncGrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = async_to_raw_response_wrapper(
            grpo.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            grpo.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            grpo.cancel,
        )
        self.download = async_to_raw_response_wrapper(
            grpo.download,
        )
        self.load = async_to_raw_response_wrapper(
            grpo.load,
        )
        self.start_job = async_to_raw_response_wrapper(
            grpo.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            grpo.stream_messages,
        )


class GrpoResourceWithStreamingResponse:
    def __init__(self, grpo: GrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = to_streamed_response_wrapper(
            grpo.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            grpo.list,
        )
        self.cancel = to_streamed_response_wrapper(
            grpo.cancel,
        )
        self.download = to_streamed_response_wrapper(
            grpo.download,
        )
        self.load = to_streamed_response_wrapper(
            grpo.load,
        )
        self.start_job = to_streamed_response_wrapper(
            grpo.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            grpo.stream_messages,
        )


class AsyncGrpoResourceWithStreamingResponse:
    def __init__(self, grpo: AsyncGrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = async_to_streamed_response_wrapper(
            grpo.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            grpo.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            grpo.cancel,
        )
        self.download = async_to_streamed_response_wrapper(
            grpo.download,
        )
        self.load = async_to_streamed_response_wrapper(
            grpo.load,
        )
        self.start_job = async_to_streamed_response_wrapper(
            grpo.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            grpo.stream_messages,
        )
