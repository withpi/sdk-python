# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.data import (
    SDKExplorationMode,
    generate_synthetic_data_list_params,
    generate_synthetic_data_start_job_params,
)
from ..._base_client import make_request_options
from ...types.contracts import State
from ...types.contracts.state import State
from ...types.data.sdk_example_param import SDKExampleParam
from ...types.data.sdk_exploration_mode import SDKExplorationMode
from ...types.data.synthetic_data_status import SyntheticDataStatus
from ...types.data.generate_synthetic_data_list_response import GenerateSyntheticDataListResponse
from ...types.data.generate_synthetic_data_stream_data_response import GenerateSyntheticDataStreamDataResponse

__all__ = ["GenerateSyntheticDataResource", "AsyncGenerateSyntheticDataResource"]


class GenerateSyntheticDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateSyntheticDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateSyntheticDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateSyntheticDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GenerateSyntheticDataResourceWithStreamingResponse(self)

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
        Checks the status of a Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/data/generate_synthetic_data/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateSyntheticDataListResponse:
        """
        Lists the Synthetic Data Generation Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/generate_synthetic_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"state": state}, generate_synthetic_data_list_params.GenerateSyntheticDataListParams
                ),
            ),
            cast_to=GenerateSyntheticDataListResponse,
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
        Cancels a Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/data/generate_synthetic_data/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def start_job(
        self,
        *,
        num_examples_to_generate: int,
        seeds: Iterable[SDKExampleParam],
        application_description: Optional[str] | NotGiven = NOT_GIVEN,
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: SDKExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataStatus:
        """
        Launches a Synthetic Data Generation job

        Args:
          num_examples_to_generate: The number of new LLM examples to generate

          seeds: The list of LLM examples (inputs + outputs) to be used as seeds

          application_description: The application description for which the synthetic data would be applicable.

          batch_size: Number of examples to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exploration mode for examples generation. Defaults to `BALANCED`

          num_shots: Number of examples to be included in the prompt for generation

          system_prompt: The system prompt to generate the responses for the application's inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/generate_synthetic_data",
            body=maybe_transform(
                {
                    "num_examples_to_generate": num_examples_to_generate,
                    "seeds": seeds,
                    "application_description": application_description,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                    "system_prompt": system_prompt,
                },
                generate_synthetic_data_start_job_params.GenerateSyntheticDataStartJobParams,
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
    ) -> GenerateSyntheticDataStreamDataResponse:
        """
        Streams data from the Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/data/generate_synthetic_data/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateSyntheticDataStreamDataResponse,
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
        Opens a message stream about a Synthetic Data Generation job

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
            f"/data/generate_synthetic_data/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerateSyntheticDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateSyntheticDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateSyntheticDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateSyntheticDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGenerateSyntheticDataResourceWithStreamingResponse(self)

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
        Checks the status of a Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/data/generate_synthetic_data/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataStatus,
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
    ) -> GenerateSyntheticDataListResponse:
        """
        Lists the Synthetic Data Generation Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/generate_synthetic_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, generate_synthetic_data_list_params.GenerateSyntheticDataListParams
                ),
            ),
            cast_to=GenerateSyntheticDataListResponse,
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
        Cancels a Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/data/generate_synthetic_data/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        num_examples_to_generate: int,
        seeds: Iterable[SDKExampleParam],
        application_description: Optional[str] | NotGiven = NOT_GIVEN,
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: SDKExplorationMode | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataStatus:
        """
        Launches a Synthetic Data Generation job

        Args:
          num_examples_to_generate: The number of new LLM examples to generate

          seeds: The list of LLM examples (inputs + outputs) to be used as seeds

          application_description: The application description for which the synthetic data would be applicable.

          batch_size: Number of examples to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exploration mode for examples generation. Defaults to `BALANCED`

          num_shots: Number of examples to be included in the prompt for generation

          system_prompt: The system prompt to generate the responses for the application's inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/generate_synthetic_data",
            body=await async_maybe_transform(
                {
                    "num_examples_to_generate": num_examples_to_generate,
                    "seeds": seeds,
                    "application_description": application_description,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                    "system_prompt": system_prompt,
                },
                generate_synthetic_data_start_job_params.GenerateSyntheticDataStartJobParams,
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
    ) -> GenerateSyntheticDataStreamDataResponse:
        """
        Streams data from the Synthetic Data Generation job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/data/generate_synthetic_data/{job_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateSyntheticDataStreamDataResponse,
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
        Opens a message stream about a Synthetic Data Generation job

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
            f"/data/generate_synthetic_data/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerateSyntheticDataResourceWithRawResponse:
    def __init__(self, generate_synthetic_data: GenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.retrieve = to_raw_response_wrapper(
            generate_synthetic_data.retrieve,
        )
        self.list = to_raw_response_wrapper(
            generate_synthetic_data.list,
        )
        self.cancel = to_raw_response_wrapper(
            generate_synthetic_data.cancel,
        )
        self.start_job = to_raw_response_wrapper(
            generate_synthetic_data.start_job,
        )
        self.stream_data = to_raw_response_wrapper(
            generate_synthetic_data.stream_data,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate_synthetic_data.stream_messages,
        )


class AsyncGenerateSyntheticDataResourceWithRawResponse:
    def __init__(self, generate_synthetic_data: AsyncGenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.retrieve = async_to_raw_response_wrapper(
            generate_synthetic_data.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            generate_synthetic_data.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            generate_synthetic_data.cancel,
        )
        self.start_job = async_to_raw_response_wrapper(
            generate_synthetic_data.start_job,
        )
        self.stream_data = async_to_raw_response_wrapper(
            generate_synthetic_data.stream_data,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate_synthetic_data.stream_messages,
        )


class GenerateSyntheticDataResourceWithStreamingResponse:
    def __init__(self, generate_synthetic_data: GenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.retrieve = to_streamed_response_wrapper(
            generate_synthetic_data.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            generate_synthetic_data.list,
        )
        self.cancel = to_streamed_response_wrapper(
            generate_synthetic_data.cancel,
        )
        self.start_job = to_streamed_response_wrapper(
            generate_synthetic_data.start_job,
        )
        self.stream_data = to_streamed_response_wrapper(
            generate_synthetic_data.stream_data,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate_synthetic_data.stream_messages,
        )


class AsyncGenerateSyntheticDataResourceWithStreamingResponse:
    def __init__(self, generate_synthetic_data: AsyncGenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.retrieve = async_to_streamed_response_wrapper(
            generate_synthetic_data.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            generate_synthetic_data.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            generate_synthetic_data.cancel,
        )
        self.start_job = async_to_streamed_response_wrapper(
            generate_synthetic_data.start_job,
        )
        self.stream_data = async_to_streamed_response_wrapper(
            generate_synthetic_data.stream_data,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate_synthetic_data.stream_messages,
        )
