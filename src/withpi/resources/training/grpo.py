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
from ...types.training import grpo_list_params, grpo_download_params, grpo_start_job_params
from ...types.shared_params.scoring_spec import ScoringSpec
from ...types.training.grpo_list_response import GrpoListResponse
from ...types.training.grpo_load_response import GrpoLoadResponse
from ...types.training.grpo_retrieve_response import GrpoRetrieveResponse
from ...types.training.grpo_start_job_response import GrpoStartJobResponse

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
    ) -> GrpoRetrieveResponse:
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
            f"/training/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoRetrieveResponse,
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
            "/training/grpo",
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
            f"/training/grpo/{job_id}",
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
            f"/training/grpo/{job_id}/download",
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
    ) -> GrpoLoadResponse:
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
            f"/training/grpo/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoLoadResponse,
        )

    def start_job(
        self,
        *,
        base_rl_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"],
        examples: Iterable[grpo_start_job_params.Example],
        learning_rate: float,
        lora_config: grpo_start_job_params.LoraConfig,
        num_train_epochs: int,
        scoring_spec: ScoringSpec,
        system_prompt: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoStartJobResponse:
        """
        Starts a RL GRPO job

        Args:
          base_rl_model: The base model to start the RL tunning process

          examples: Examples to use in the RL tuning process

          learning_rate: GRPO learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: GRPO number of train epochs

          scoring_spec: The scoring spec to use in the GRPO tuning process

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/training/grpo",
            body=maybe_transform(
                {
                    "base_rl_model": base_rl_model,
                    "examples": examples,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "scoring_spec": scoring_spec,
                    "system_prompt": system_prompt,
                },
                grpo_start_job_params.GrpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoStartJobResponse,
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
            f"/training/grpo/{job_id}/messages",
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
    ) -> GrpoRetrieveResponse:
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
            f"/training/grpo/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoRetrieveResponse,
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
            "/training/grpo",
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
            f"/training/grpo/{job_id}",
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
            f"/training/grpo/{job_id}/download",
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
    ) -> GrpoLoadResponse:
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
            f"/training/grpo/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoLoadResponse,
        )

    async def start_job(
        self,
        *,
        base_rl_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"],
        examples: Iterable[grpo_start_job_params.Example],
        learning_rate: float,
        lora_config: grpo_start_job_params.LoraConfig,
        num_train_epochs: int,
        scoring_spec: ScoringSpec,
        system_prompt: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoStartJobResponse:
        """
        Starts a RL GRPO job

        Args:
          base_rl_model: The base model to start the RL tunning process

          examples: Examples to use in the RL tuning process

          learning_rate: GRPO learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: GRPO number of train epochs

          scoring_spec: The scoring spec to use in the GRPO tuning process

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/training/grpo",
            body=await async_maybe_transform(
                {
                    "base_rl_model": base_rl_model,
                    "examples": examples,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "scoring_spec": scoring_spec,
                    "system_prompt": system_prompt,
                },
                grpo_start_job_params.GrpoStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoStartJobResponse,
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
            f"/training/grpo/{job_id}/messages",
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
