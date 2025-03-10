# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
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
from ...types.data import generate_input_list_params, generate_input_create_params
from ..._base_client import make_request_options
from ...types.shared.exploration_mode import ExplorationMode
from ...types.shared.data_generation_status import DataGenerationStatus
from ...types.data.generate_input_list_response import GenerateInputListResponse

__all__ = ["GenerateInputsResource", "AsyncGenerateInputsResource"]


class GenerateInputsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GenerateInputsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        application_description: str,
        num_inputs_to_generate: int,
        seeds: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: ExplorationMode | NotGiven = NOT_GIVEN,
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

          batch_size: Number of inputs to generate in one LLM call. Must be <= 10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for input generation. Defaults to `BALANCED`

          num_shots: Number of inputs to be included in the prompt for generation. Must be <= 10.
              Generally it could be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/generate_inputs",
            body=maybe_transform(
                {
                    "application_description": application_description,
                    "num_inputs_to_generate": num_inputs_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_input_create_params.GenerateInputCreateParams,
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
            f"/data/generate_inputs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
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
    ) -> GenerateInputListResponse:
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
            "/data/generate_inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, generate_input_list_params.GenerateInputListParams),
            ),
            cast_to=GenerateInputListResponse,
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
            f"/data/generate_inputs/{job_id}",
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
            f"/data/generate_inputs/{job_id}/data",
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
            f"/data/generate_inputs/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerateInputsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGenerateInputsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        application_description: str,
        num_inputs_to_generate: int,
        seeds: List[str],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: ExplorationMode | NotGiven = NOT_GIVEN,
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

          batch_size: Number of inputs to generate in one LLM call. Must be <= 10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for input generation. Defaults to `BALANCED`

          num_shots: Number of inputs to be included in the prompt for generation. Must be <= 10.
              Generally it could be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/generate_inputs",
            body=await async_maybe_transform(
                {
                    "application_description": application_description,
                    "num_inputs_to_generate": num_inputs_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_input_create_params.GenerateInputCreateParams,
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
            f"/data/generate_inputs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGenerationStatus,
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
    ) -> GenerateInputListResponse:
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
            "/data/generate_inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"state": state}, generate_input_list_params.GenerateInputListParams),
            ),
            cast_to=GenerateInputListResponse,
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
            f"/data/generate_inputs/{job_id}",
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
            f"/data/generate_inputs/{job_id}/data",
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
            f"/data/generate_inputs/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerateInputsResourceWithRawResponse:
    def __init__(self, generate_inputs: GenerateInputsResource) -> None:
        self._generate_inputs = generate_inputs

        self.create = to_raw_response_wrapper(
            generate_inputs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generate_inputs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            generate_inputs.list,
        )
        self.cancel = to_raw_response_wrapper(
            generate_inputs.cancel,
        )
        self.stream_data = to_raw_response_wrapper(
            generate_inputs.stream_data,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate_inputs.stream_messages,
        )


class AsyncGenerateInputsResourceWithRawResponse:
    def __init__(self, generate_inputs: AsyncGenerateInputsResource) -> None:
        self._generate_inputs = generate_inputs

        self.create = async_to_raw_response_wrapper(
            generate_inputs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generate_inputs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            generate_inputs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            generate_inputs.cancel,
        )
        self.stream_data = async_to_raw_response_wrapper(
            generate_inputs.stream_data,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate_inputs.stream_messages,
        )


class GenerateInputsResourceWithStreamingResponse:
    def __init__(self, generate_inputs: GenerateInputsResource) -> None:
        self._generate_inputs = generate_inputs

        self.create = to_streamed_response_wrapper(
            generate_inputs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generate_inputs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            generate_inputs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            generate_inputs.cancel,
        )
        self.stream_data = to_streamed_response_wrapper(
            generate_inputs.stream_data,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate_inputs.stream_messages,
        )


class AsyncGenerateInputsResourceWithStreamingResponse:
    def __init__(self, generate_inputs: AsyncGenerateInputsResource) -> None:
        self._generate_inputs = generate_inputs

        self.create = async_to_streamed_response_wrapper(
            generate_inputs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generate_inputs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            generate_inputs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            generate_inputs.cancel,
        )
        self.stream_data = async_to_streamed_response_wrapper(
            generate_inputs.stream_data,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate_inputs.stream_messages,
        )
