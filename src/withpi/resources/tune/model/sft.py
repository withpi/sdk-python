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
from ....types.tune.model import sft_start_job_params
from ....types.tune.model.sft_status import SftStatus
from ....types.shared_params.contract import Contract

__all__ = ["SftResource", "AsyncSftResource"]


class SftResource(SyncAPIResource):
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
        return self._post(
            f"/tune/model/sft/{job_id}",
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

          base_sft_model: The base model to use in the SFT.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tune/model/sft",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "base_sft_model": base_sft_model,
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
    ) -> object:
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
        return self._post(
            f"/tune/model/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSftResource(AsyncAPIResource):
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
        return await self._post(
            f"/tune/model/sft/{job_id}",
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

          base_sft_model: The base model to use in the SFT.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tune/model/sft",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "base_sft_model": base_sft_model,
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
    ) -> object:
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
        return await self._post(
            f"/tune/model/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SftResourceWithRawResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.get_status = to_raw_response_wrapper(
            sft.get_status,
        )
        self.start_job = to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            sft.stream_messages,
        )


class AsyncSftResourceWithRawResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.get_status = async_to_raw_response_wrapper(
            sft.get_status,
        )
        self.start_job = async_to_raw_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            sft.stream_messages,
        )


class SftResourceWithStreamingResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.get_status = to_streamed_response_wrapper(
            sft.get_status,
        )
        self.start_job = to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            sft.stream_messages,
        )


class AsyncSftResourceWithStreamingResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.get_status = async_to_streamed_response_wrapper(
            sft.get_status,
        )
        self.start_job = async_to_streamed_response_wrapper(
            sft.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            sft.stream_messages,
        )
