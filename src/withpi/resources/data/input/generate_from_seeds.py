# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from ....types.data import SDKExplorationMode
from ...._base_client import make_request_options
from ....types.contracts import State
from ....types.data.input import generate_from_seed_list_params, generate_from_seed_create_params
from ....types.contracts.state import State
from ....types.data.sdk_exploration_mode import SDKExplorationMode
from ....types.data.input.data_generation_status import DataGenerationStatus
from ....types.data.input.generate_from_seed_list_response import GenerateFromSeedListResponse

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

    def create(
        self,
        *,
        application_description: str,
        num_inputs_to_generate: int,
        seeds: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: SDKExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGenerationStatus:
        """
        Launches a Data Generation job

        Args:
          application_description: The application description for which the inputs would be applicable.

          num_inputs_to_generate: The number of new LLM inputs to generate

          seeds: The list of LLM inputs to be used as seeds

          batch_size: Number of inputs to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for input generation. Defaults to `BALANCED`

          num_shots: Number of inputs to be included in the prompt for generation. Generally it could
              be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/input/generate_from_seeds",
            body=maybe_transform(
                {
                    "application_description": application_description,
                    "num_inputs_to_generate": num_inputs_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_from_seed_create_params.GenerateFromSeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
        )

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
        Checks the status of a Data Generation job

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
    ) -> GenerateFromSeedListResponse:
        """
        Lists the Data Generation Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/input/generate_from_seeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, generate_from_seed_list_params.GenerateFromSeedListParams),
            ),
            cast_to=GenerateFromSeedListResponse,
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
        Cancels a Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/data/input/generate_from_seeds/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def stream_data(
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
        Streams data from the Data Generation job

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
            f"/data/input/generate_from_seeds/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
        Opens a message stream about a Data Generation job

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

    async def create(
        self,
        *,
        application_description: str,
        num_inputs_to_generate: int,
        seeds: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: SDKExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGenerationStatus:
        """
        Launches a Data Generation job

        Args:
          application_description: The application description for which the inputs would be applicable.

          num_inputs_to_generate: The number of new LLM inputs to generate

          seeds: The list of LLM inputs to be used as seeds

          batch_size: Number of inputs to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for input generation. Defaults to `BALANCED`

          num_shots: Number of inputs to be included in the prompt for generation. Generally it could
              be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/input/generate_from_seeds",
            body=await async_maybe_transform(
                {
                    "application_description": application_description,
                    "num_inputs_to_generate": num_inputs_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_from_seed_create_params.GenerateFromSeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
        )

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
        Checks the status of a Data Generation job

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
    ) -> GenerateFromSeedListResponse:
        """
        Lists the Data Generation Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/input/generate_from_seeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, generate_from_seed_list_params.GenerateFromSeedListParams
                ),
            ),
            cast_to=GenerateFromSeedListResponse,
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
        Cancels a Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/data/input/generate_from_seeds/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def stream_data(
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
        Streams data from the Data Generation job

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
            f"/data/input/generate_from_seeds/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
        Opens a message stream about a Data Generation job

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

        self.create = to_raw_response_wrapper(
            generate_from_seeds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            generate_from_seeds.list,
        )
        self.cancel = to_raw_response_wrapper(
            generate_from_seeds.cancel,
        )
        self.stream_data = to_raw_response_wrapper(
            generate_from_seeds.stream_data,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class AsyncGenerateFromSeedsResourceWithRawResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.create = async_to_raw_response_wrapper(
            generate_from_seeds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            generate_from_seeds.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            generate_from_seeds.cancel,
        )
        self.stream_data = async_to_raw_response_wrapper(
            generate_from_seeds.stream_data,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class GenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: GenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.create = to_streamed_response_wrapper(
            generate_from_seeds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            generate_from_seeds.list,
        )
        self.cancel = to_streamed_response_wrapper(
            generate_from_seeds.cancel,
        )
        self.stream_data = to_streamed_response_wrapper(
            generate_from_seeds.stream_data,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate_from_seeds.stream_messages,
        )


class AsyncGenerateFromSeedsResourceWithStreamingResponse:
    def __init__(self, generate_from_seeds: AsyncGenerateFromSeedsResource) -> None:
        self._generate_from_seeds = generate_from_seeds

        self.create = async_to_streamed_response_wrapper(
            generate_from_seeds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generate_from_seeds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            generate_from_seeds.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            generate_from_seeds.cancel,
        )
        self.stream_data = async_to_streamed_response_wrapper(
            generate_from_seeds.stream_data,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate_from_seeds.stream_messages,
        )
