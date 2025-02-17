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
from .completions import (
    CompletionsResource,
    AsyncCompletionsResource,
    CompletionsResourceWithRawResponse,
    AsyncCompletionsResourceWithRawResponse,
    CompletionsResourceWithStreamingResponse,
    AsyncCompletionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.model import sft_start_job_params
from ...._base_client import make_request_options
from .chat_completions import (
    ChatCompletionsResource,
    AsyncChatCompletionsResource,
    ChatCompletionsResourceWithRawResponse,
    AsyncChatCompletionsResourceWithRawResponse,
    ChatCompletionsResourceWithStreamingResponse,
    AsyncChatCompletionsResourceWithStreamingResponse,
)
from ....types.model.sft_status import SftStatus
from ....types.shared_params.contract import Contract
from ....types.model.sft_check_response import SftCheckResponse

__all__ = ["SftResource", "AsyncSftResource"]


class SftResource(SyncAPIResource):
    @cached_property
    def chat_completions(self) -> ChatCompletionsResource:
        return ChatCompletionsResource(self._client)

    @cached_property
    def completions(self) -> CompletionsResource:
        return CompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return SftResourceWithStreamingResponse(self)

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
    ) -> SftStatus:
        """
        Get the current status of a model SFT tuning job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/model/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatus,
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
    ) -> SftCheckResponse:
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
            f"/model/sft/{job_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftCheckResponse,
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
        """Load the SFT model into serving.

        This can support a very small amount of
        interactive traffic. Please reach out if you want to use this model in a
        production setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/model/sft/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[sft_start_job_params.Example],
        base_sft_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatus:
        """Initialize the supervised fine-tuning (SFT) job for the model.

        We implement
        Low-Rank Adaptation (LoRA) for the fine-tuning process, with a fixed rank of 16.

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the SFT tuning process. We split this data into train/eval
              90/10.

          base_sft_model: The base model to start the SFT tuning process.

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/model/sft",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "base_sft_model": base_sft_model,
                    "learning_rate": learning_rate,
                    "num_train_epochs": num_train_epochs,
                },
                sft_start_job_params.SftStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatus,
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
        Streams messages from a model SFT tuning job

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
            f"/model/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncSftResource(AsyncAPIResource):
    @cached_property
    def chat_completions(self) -> AsyncChatCompletionsResource:
        return AsyncChatCompletionsResource(self._client)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        return AsyncCompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncSftResourceWithStreamingResponse(self)

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
    ) -> SftStatus:
        """
        Get the current status of a model SFT tuning job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/model/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatus,
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
    ) -> SftCheckResponse:
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
            f"/model/sft/{job_id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftCheckResponse,
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
        """Load the SFT model into serving.

        This can support a very small amount of
        interactive traffic. Please reach out if you want to use this model in a
        production setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/model/sft/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[sft_start_job_params.Example],
        base_sft_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatus:
        """Initialize the supervised fine-tuning (SFT) job for the model.

        We implement
        Low-Rank Adaptation (LoRA) for the fine-tuning process, with a fixed rank of 16.

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the SFT tuning process. We split this data into train/eval
              90/10.

          base_sft_model: The base model to start the SFT tuning process.

          learning_rate: SFT learning rate

          num_train_epochs: SFT number of train epochs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/model/sft",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "base_sft_model": base_sft_model,
                    "learning_rate": learning_rate,
                    "num_train_epochs": num_train_epochs,
                },
                sft_start_job_params.SftStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatus,
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
        Streams messages from a model SFT tuning job

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
            f"/model/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class SftResourceWithRawResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.retrieve = to_raw_response_wrapper(
            sft.retrieve,
        )
        self.check = to_raw_response_wrapper(
            sft.check,
        )
        self.load = to_raw_response_wrapper(
            sft.load,
        )
        self.start_job = to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def chat_completions(self) -> ChatCompletionsResourceWithRawResponse:
        return ChatCompletionsResourceWithRawResponse(self._sft.chat_completions)

    @cached_property
    def completions(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self._sft.completions)


class AsyncSftResourceWithRawResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.retrieve = async_to_raw_response_wrapper(
            sft.retrieve,
        )
        self.check = async_to_raw_response_wrapper(
            sft.check,
        )
        self.load = async_to_raw_response_wrapper(
            sft.load,
        )
        self.start_job = async_to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def chat_completions(self) -> AsyncChatCompletionsResourceWithRawResponse:
        return AsyncChatCompletionsResourceWithRawResponse(self._sft.chat_completions)

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self._sft.completions)


class SftResourceWithStreamingResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.retrieve = to_streamed_response_wrapper(
            sft.retrieve,
        )
        self.check = to_streamed_response_wrapper(
            sft.check,
        )
        self.load = to_streamed_response_wrapper(
            sft.load,
        )
        self.start_job = to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def chat_completions(self) -> ChatCompletionsResourceWithStreamingResponse:
        return ChatCompletionsResourceWithStreamingResponse(self._sft.chat_completions)

    @cached_property
    def completions(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self._sft.completions)


class AsyncSftResourceWithStreamingResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.retrieve = async_to_streamed_response_wrapper(
            sft.retrieve,
        )
        self.check = async_to_streamed_response_wrapper(
            sft.check,
        )
        self.load = async_to_streamed_response_wrapper(
            sft.load,
        )
        self.start_job = async_to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def chat_completions(self) -> AsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncChatCompletionsResourceWithStreamingResponse(self._sft.chat_completions)

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self._sft.completions)
