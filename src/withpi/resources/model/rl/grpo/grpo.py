# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .completions import (
    CompletionsResource,
    AsyncCompletionsResource,
    CompletionsResourceWithRawResponse,
    AsyncCompletionsResourceWithRawResponse,
    CompletionsResourceWithStreamingResponse,
    AsyncCompletionsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .chat_completions import (
    ChatCompletionsResource,
    AsyncChatCompletionsResource,
    ChatCompletionsResourceWithRawResponse,
    AsyncChatCompletionsResourceWithRawResponse,
    ChatCompletionsResourceWithStreamingResponse,
    AsyncChatCompletionsResourceWithStreamingResponse,
)
from .....types.model.rl import grpo_start_job_params
from .....types.shared_params.contract import Contract
from .....types.model.rl.rl_grpo_status import RlGrpoStatus
from .....types.model.rl.grpo_check_response import GrpoCheckResponse

__all__ = ["GrpoResource", "AsyncGrpoResource"]


class GrpoResource(SyncAPIResource):
    @cached_property
    def chat_completions(self) -> ChatCompletionsResource:
        return ChatCompletionsResource(self._client)

    @cached_property
    def completions(self) -> CompletionsResource:
        return CompletionsResource(self._client)

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
        Get the current status of the RL GRPO job

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

    def check(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoCheckResponse:
        """
        Check if the model is serving

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/model/rl/grpo/{job_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoCheckResponse,
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
    ) -> str:
        """Load the model into serving.

        This can support a very small amount of interactive
        traffic. Please reach out if you want to use this model in a production setting.

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
            cast_to=str,
        )

    def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[grpo_start_job_params.Example],
        model: Literal["LLAMA_3.2_1B"],
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Initialize the Group Relative Policy Optimization (GRPO) reinforcement learning
        job.

        Args:
          contract: The contract to use in the GRPO tuning process

          examples: Examples to use in the RL tuning process

          model: The model to start the RL process

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

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
                    "contract": contract,
                    "examples": examples,
                    "model": model,
                    "learning_rate": learning_rate,
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
        Streams messages from the RL GRPO job

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
    def chat_completions(self) -> AsyncChatCompletionsResource:
        return AsyncChatCompletionsResource(self._client)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        return AsyncCompletionsResource(self._client)

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
        Get the current status of the RL GRPO job

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

    async def check(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GrpoCheckResponse:
        """
        Check if the model is serving

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/model/rl/grpo/{job_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrpoCheckResponse,
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
    ) -> str:
        """Load the model into serving.

        This can support a very small amount of interactive
        traffic. Please reach out if you want to use this model in a production setting.

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
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[grpo_start_job_params.Example],
        model: Literal["LLAMA_3.2_1B"],
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RlGrpoStatus:
        """
        Initialize the Group Relative Policy Optimization (GRPO) reinforcement learning
        job.

        Args:
          contract: The contract to use in the GRPO tuning process

          examples: Examples to use in the RL tuning process

          model: The model to start the RL process

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

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
                    "contract": contract,
                    "examples": examples,
                    "model": model,
                    "learning_rate": learning_rate,
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
        Streams messages from the RL GRPO job

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
        self.check = to_raw_response_wrapper(
            grpo.check,
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

    @cached_property
    def chat_completions(self) -> ChatCompletionsResourceWithRawResponse:
        return ChatCompletionsResourceWithRawResponse(self._grpo.chat_completions)

    @cached_property
    def completions(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self._grpo.completions)


class AsyncGrpoResourceWithRawResponse:
    def __init__(self, grpo: AsyncGrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = async_to_raw_response_wrapper(
            grpo.retrieve,
        )
        self.check = async_to_raw_response_wrapper(
            grpo.check,
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

    @cached_property
    def chat_completions(self) -> AsyncChatCompletionsResourceWithRawResponse:
        return AsyncChatCompletionsResourceWithRawResponse(self._grpo.chat_completions)

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self._grpo.completions)


class GrpoResourceWithStreamingResponse:
    def __init__(self, grpo: GrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = to_streamed_response_wrapper(
            grpo.retrieve,
        )
        self.check = to_streamed_response_wrapper(
            grpo.check,
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

    @cached_property
    def chat_completions(self) -> ChatCompletionsResourceWithStreamingResponse:
        return ChatCompletionsResourceWithStreamingResponse(self._grpo.chat_completions)

    @cached_property
    def completions(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self._grpo.completions)


class AsyncGrpoResourceWithStreamingResponse:
    def __init__(self, grpo: AsyncGrpoResource) -> None:
        self._grpo = grpo

        self.retrieve = async_to_streamed_response_wrapper(
            grpo.retrieve,
        )
        self.check = async_to_streamed_response_wrapper(
            grpo.check,
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

    @cached_property
    def chat_completions(self) -> AsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncChatCompletionsResourceWithStreamingResponse(self._grpo.chat_completions)

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self._grpo.completions)
