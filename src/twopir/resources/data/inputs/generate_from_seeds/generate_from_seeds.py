# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.data_generation_status import DataGenerationStatus

__all__ = ["GenerateFromSeedsResource", "AsyncGenerateFromSeedsResource"]


class GenerateFromSeedsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerateFromSeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateFromSeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateFromSeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return GenerateFromSeedsResourceWithStreamingResponse(self)

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
    ) -> DataGenerationStatus:
        """
        Start an input data generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/data/input/generate_from_seeds/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
        )


class AsyncGenerateFromSeedsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerateFromSeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateFromSeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateFromSeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return AsyncGenerateFromSeedsResourceWithStreamingResponse(self)

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
    ) -> DataGenerationStatus:
        """
        Start an input data generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/data/input/generate_from_seeds/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
        )


class GenerateFromSeedsResourceWithRawResponse:
    def __init__(self, generate_from_seeds: GenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._generate_from_seeds.messages)


class AsyncGenerateFromSeedsResourceWithRawResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = async_to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._generate_from_seeds.messages)


class GenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: GenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._generate_from_seeds.messages)


class AsyncGenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = async_to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._generate_from_seeds.messages)
