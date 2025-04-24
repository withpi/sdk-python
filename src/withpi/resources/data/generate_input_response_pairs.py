# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.data import generate_input_response_pair_list_params, generate_input_response_pair_start_job_params
from ..._base_client import make_request_options
from ...types.shared_params.example import Example
from ...types.shared.exploration_mode import ExplorationMode
from ...types.shared.synthetic_data_status import SyntheticDataStatus
from ...types.data.generate_input_response_pair_list_response import GenerateInputResponsePairListResponse
from ...types.data.generate_input_response_pair_stream_data_response import GenerateInputResponsePairStreamDataResponse

__all__ = ["GenerateInputResponsePairsResource", "AsyncGenerateInputResponsePairsResource"]


class GenerateInputResponsePairsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateInputResponsePairsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateInputResponsePairsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateInputResponsePairsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GenerateInputResponsePairsResourceWithStreamingResponse(self)

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
    ) -> SyntheticDataStatus:
        """
        Checks the status of a Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/data/generate_input_response_pairs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateInputResponsePairListResponse:
        """
        Lists the Generation Input-Response Pairs Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/generate_input_response_pairs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"state": state}, generate_input_response_pair_list_params.GenerateInputResponsePairListParams
                ),
            ),
            cast_to=GenerateInputResponsePairListResponse,
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
        Cancels a Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/data/generate_input_response_pairs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def start_job(
        self,
        *,
        num_pairs_to_generate: int,
        seeds: Iterable[Example],
        application_description: Optional[str] | NotGiven = NOT_GIVEN,
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: ExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        run_parallel_batches: bool | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataStatus:
        """
        Starts a Generation Input-Response Pairs job

        Args:
          num_pairs_to_generate: The number of new LLM input-response pairs to generate

          seeds: The list of LLM input response-pairs to be used as seeds

          application_description: The application description for which the synthetic data would be applicable.

          batch_size: Number of input-response pairs to generate in one LLM call. Must be <=10.
              Generally it could be same as `num_shots`.

          exploration_mode: The exploration mode for input-response pairs generation. Defaults to `BALANCED`

          num_shots: Number of input-response pairs to be included in the prompt for generation

          run_parallel_batches: If true, multiple batches of generation and critique run concurrently.

          system_prompt: The system prompt to generate the responses for the application's inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/generate_input_response_pairs",
            body=maybe_transform(
                {
                    "num_pairs_to_generate": num_pairs_to_generate,
                    "seeds": seeds,
                    "application_description": application_description,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                    "run_parallel_batches": run_parallel_batches,
                    "system_prompt": system_prompt,
                },
                generate_input_response_pair_start_job_params.GenerateInputResponsePairStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateInputResponsePairStreamDataResponse:
        """
        Streams data from the Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/data/generate_input_response_pairs/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateInputResponsePairStreamDataResponse,
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
        Opens a message stream about a Generation Input-Response Pairs job

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
            f"/data/generate_input_response_pairs/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerateInputResponsePairsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateInputResponsePairsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateInputResponsePairsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateInputResponsePairsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGenerateInputResponsePairsResourceWithStreamingResponse(self)

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
    ) -> SyntheticDataStatus:
        """
        Checks the status of a Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/data/generate_input_response_pairs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateInputResponsePairListResponse:
        """
        Lists the Generation Input-Response Pairs Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/generate_input_response_pairs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, generate_input_response_pair_list_params.GenerateInputResponsePairListParams
                ),
            ),
            cast_to=GenerateInputResponsePairListResponse,
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
        Cancels a Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/data/generate_input_response_pairs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        num_pairs_to_generate: int,
        seeds: Iterable[Example],
        application_description: Optional[str] | NotGiven = NOT_GIVEN,
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: ExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        run_parallel_batches: bool | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataStatus:
        """
        Starts a Generation Input-Response Pairs job

        Args:
          num_pairs_to_generate: The number of new LLM input-response pairs to generate

          seeds: The list of LLM input response-pairs to be used as seeds

          application_description: The application description for which the synthetic data would be applicable.

          batch_size: Number of input-response pairs to generate in one LLM call. Must be <=10.
              Generally it could be same as `num_shots`.

          exploration_mode: The exploration mode for input-response pairs generation. Defaults to `BALANCED`

          num_shots: Number of input-response pairs to be included in the prompt for generation

          run_parallel_batches: If true, multiple batches of generation and critique run concurrently.

          system_prompt: The system prompt to generate the responses for the application's inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/generate_input_response_pairs",
            body=await async_maybe_transform(
                {
                    "num_pairs_to_generate": num_pairs_to_generate,
                    "seeds": seeds,
                    "application_description": application_description,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                    "run_parallel_batches": run_parallel_batches,
                    "system_prompt": system_prompt,
                },
                generate_input_response_pair_start_job_params.GenerateInputResponsePairStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateInputResponsePairStreamDataResponse:
        """
        Streams data from the Generation Input-Response Pairs job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/data/generate_input_response_pairs/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateInputResponsePairStreamDataResponse,
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
        Opens a message stream about a Generation Input-Response Pairs job

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
            f"/data/generate_input_response_pairs/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerateInputResponsePairsResourceWithRawResponse:
    def __init__(self, generate_input_response_pairs: GenerateInputResponsePairsResource) -> None:
        self._generate_input_response_pairs = generate_input_response_pairs

        self.retrieve = to_raw_response_wrapper(
            generate_input_response_pairs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            generate_input_response_pairs.list,
        )
        self.cancel = to_raw_response_wrapper(
            generate_input_response_pairs.cancel,
        )
        self.start_job = to_raw_response_wrapper(
            generate_input_response_pairs.start_job,
        )
        self.stream_data = to_raw_response_wrapper(
            generate_input_response_pairs.stream_data,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate_input_response_pairs.stream_messages,
        )


class AsyncGenerateInputResponsePairsResourceWithRawResponse:
    def __init__(self, generate_input_response_pairs: AsyncGenerateInputResponsePairsResource) -> None:
        self._generate_input_response_pairs = generate_input_response_pairs

        self.retrieve = async_to_raw_response_wrapper(
            generate_input_response_pairs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            generate_input_response_pairs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            generate_input_response_pairs.cancel,
        )
        self.start_job = async_to_raw_response_wrapper(
            generate_input_response_pairs.start_job,
        )
        self.stream_data = async_to_raw_response_wrapper(
            generate_input_response_pairs.stream_data,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate_input_response_pairs.stream_messages,
        )


class GenerateInputResponsePairsResourceWithStreamingResponse:
    def __init__(self, generate_input_response_pairs: GenerateInputResponsePairsResource) -> None:
        self._generate_input_response_pairs = generate_input_response_pairs

        self.retrieve = to_streamed_response_wrapper(
            generate_input_response_pairs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            generate_input_response_pairs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            generate_input_response_pairs.cancel,
        )
        self.start_job = to_streamed_response_wrapper(
            generate_input_response_pairs.start_job,
        )
        self.stream_data = to_streamed_response_wrapper(
            generate_input_response_pairs.stream_data,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate_input_response_pairs.stream_messages,
        )


class AsyncGenerateInputResponsePairsResourceWithStreamingResponse:
    def __init__(self, generate_input_response_pairs: AsyncGenerateInputResponsePairsResource) -> None:
        self._generate_input_response_pairs = generate_input_response_pairs

        self.retrieve = async_to_streamed_response_wrapper(
            generate_input_response_pairs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            generate_input_response_pairs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            generate_input_response_pairs.cancel,
        )
        self.start_job = async_to_streamed_response_wrapper(
            generate_input_response_pairs.start_job,
        )
        self.stream_data = async_to_streamed_response_wrapper(
            generate_input_response_pairs.stream_data,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate_input_response_pairs.stream_messages,
        )
