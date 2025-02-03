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
from ....types.model import sft_start_job_params
from ...._base_client import make_request_options
from ....types.model.sft_status import SftStatus
from ....types.shared_params.contract import Contract

__all__ = ["SftResource", "AsyncSftResource"]


class SftResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

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

    def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[sft_start_job_params.Example],
        base_sft_model: Literal["LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatus:
        """
        Start the model SFT tuning job

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the SFT tuning process

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
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

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

    async def start_job(
        self,
        *,
        contract: Contract,
        examples: Iterable[sft_start_job_params.Example],
        base_sft_model: Literal["LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatus:
        """
        Start the model SFT tuning job

        Args:
          contract: The contract to use in the SFT tuning process

          examples: Examples to use in the SFT tuning process

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
        self.start_job = to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._sft.messages)


class AsyncSftResourceWithRawResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.retrieve = async_to_raw_response_wrapper(
            sft.retrieve,
        )
        self.start_job = async_to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._sft.messages)


class SftResourceWithStreamingResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.retrieve = to_streamed_response_wrapper(
            sft.retrieve,
        )
        self.start_job = to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._sft.messages)


class AsyncSftResourceWithStreamingResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.retrieve = async_to_streamed_response_wrapper(
            sft.retrieve,
        )
        self.start_job = async_to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            sft.stream_messages,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._sft.messages)
