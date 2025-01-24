# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ....types.data.inputs import generate_from_seed_generate_params
from ....types.data_generation_status import DataGenerationStatus

__all__ = ["GenerateFromSeedsResource", "AsyncGenerateFromSeedsResource"]


class GenerateFromSeedsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateFromSeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateFromSeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateFromSeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
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
        Gets the current status of a data generation job

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

    def generate(
        self,
        *,
        contract_description: str,
        num_inputs: int,
        seeds: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGenerationStatus:
        """
        Generates input data from a list of seeds

        Args:
          contract_description: The application description to generate contract for.

          num_inputs: The number of LLM inputs to generate

          seeds: The list of LLM inputs to be used as seeds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/input/generate_from_seeds",
            body=maybe_transform(
                {
                    "contract_description": contract_description,
                    "num_inputs": num_inputs,
                    "seeds": seeds,
                },
                generate_from_seed_generate_params.GenerateFromSeedGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
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
        Streams messages from the data generation job

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
            f"/data/input/generate_from_seeds/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerateFromSeedsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateFromSeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateFromSeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateFromSeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
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
        Gets the current status of a data generation job

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

    async def generate(
        self,
        *,
        contract_description: str,
        num_inputs: int,
        seeds: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGenerationStatus:
        """
        Generates input data from a list of seeds

        Args:
          contract_description: The application description to generate contract for.

          num_inputs: The number of LLM inputs to generate

          seeds: The list of LLM inputs to be used as seeds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/input/generate_from_seeds",
            body=await async_maybe_transform(
                {
                    "contract_description": contract_description,
                    "num_inputs": num_inputs,
                    "seeds": seeds,
                },
                generate_from_seed_generate_params.GenerateFromSeedGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
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
        Streams messages from the data generation job

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
            f"/data/input/generate_from_seeds/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerateFromSeedsResourceWithRawResponse:
    def __init__(self, generate_from_seeds: GenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.generate = to_raw_response_wrapper(
            generate_from_seeds.generate,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class AsyncGenerateFromSeedsResourceWithRawResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = async_to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.generate = async_to_raw_response_wrapper(
            generate_from_seeds.generate,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class GenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: GenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.generate = to_streamed_response_wrapper(
            generate_from_seeds.generate,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class AsyncGenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.retrieve = async_to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.generate = async_to_streamed_response_wrapper(
            generate_from_seeds.generate,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate_from_seeds.stream_messages,
        )
