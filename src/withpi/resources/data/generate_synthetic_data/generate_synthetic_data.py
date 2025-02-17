# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .data import (
    DataResource,
    AsyncDataResource,
    DataResourceWithRawResponse,
    AsyncDataResourceWithRawResponse,
    DataResourceWithStreamingResponse,
    AsyncDataResourceWithStreamingResponse,
)
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
from ....types.data import generate_synthetic_data_create_params
from ...._base_client import make_request_options
from ....types.data.generate_synthetic_data_create_response import GenerateSyntheticDataCreateResponse
from ....types.data.generate_synthetic_data_retrieve_response import GenerateSyntheticDataRetrieveResponse

__all__ = ["GenerateSyntheticDataResource", "AsyncGenerateSyntheticDataResource"]


class GenerateSyntheticDataResource(SyncAPIResource):
    @cached_property
    def data(self) -> DataResource:
        return DataResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

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

    def create(
        self,
        *,
        application_description: str,
        num_examples_to_generate: int,
        seeds: Iterable[generate_synthetic_data_create_params.Seed],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: Literal["CONSERVATIVE", "BALANCED", "CREATIVE", "ADVENTUROUS"] | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateSyntheticDataCreateResponse:
        """
        Generates synthetic data from a list of seeds

        Args:
          application_description: The application description for which the synthetic data would be applicable.

          num_examples_to_generate: The number of new LLM examples to generate

          seeds: The list of LLM examples (inputs + outputs) to be used as seeds

          batch_size: Number of examples to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for examples generation. Defaults to `BALANCED`

          num_shots: Number of examples to be included in the prompt for generation. Generally it
              could be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/generate_synthetic_data",
            body=maybe_transform(
                {
                    "application_description": application_description,
                    "num_examples_to_generate": num_examples_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_synthetic_data_create_params.GenerateSyntheticDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateSyntheticDataCreateResponse,
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
    ) -> GenerateSyntheticDataRetrieveResponse:
        """
        Gets the current status of a synthetic data generation job

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
            cast_to=GenerateSyntheticDataRetrieveResponse,
        )


class AsyncGenerateSyntheticDataResource(AsyncAPIResource):
    @cached_property
    def data(self) -> AsyncDataResource:
        return AsyncDataResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

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

    async def create(
        self,
        *,
        application_description: str,
        num_examples_to_generate: int,
        seeds: Iterable[generate_synthetic_data_create_params.Seed],
        batch_size: int | NotGiven = NOT_GIVEN,
        exploration_mode: Literal["CONSERVATIVE", "BALANCED", "CREATIVE", "ADVENTUROUS"] | NotGiven = NOT_GIVEN,
        num_shots: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateSyntheticDataCreateResponse:
        """
        Generates synthetic data from a list of seeds

        Args:
          application_description: The application description for which the synthetic data would be applicable.

          num_examples_to_generate: The number of new LLM examples to generate

          seeds: The list of LLM examples (inputs + outputs) to be used as seeds

          batch_size: Number of examples to generate in one LLM call. Must be <=10. Generally it could
              be same as `num_shots`.

          exploration_mode: The exloration mode for examples generation. Defaults to `BALANCED`

          num_shots: Number of examples to be included in the prompt for generation. Generally it
              could be same as `batch_size`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/generate_synthetic_data",
            body=await async_maybe_transform(
                {
                    "application_description": application_description,
                    "num_examples_to_generate": num_examples_to_generate,
                    "seeds": seeds,
                    "batch_size": batch_size,
                    "exploration_mode": exploration_mode,
                    "num_shots": num_shots,
                },
                generate_synthetic_data_create_params.GenerateSyntheticDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateSyntheticDataCreateResponse,
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
    ) -> GenerateSyntheticDataRetrieveResponse:
        """
        Gets the current status of a synthetic data generation job

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
            cast_to=GenerateSyntheticDataRetrieveResponse,
        )


class GenerateSyntheticDataResourceWithRawResponse:
    def __init__(self, generate_synthetic_data: GenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.create = to_raw_response_wrapper(
            generate_synthetic_data.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generate_synthetic_data.retrieve,
        )

    @cached_property
    def data(self) -> DataResourceWithRawResponse:
        return DataResourceWithRawResponse(self._generate_synthetic_data.data)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._generate_synthetic_data.messages)


class AsyncGenerateSyntheticDataResourceWithRawResponse:
    def __init__(self, generate_synthetic_data: AsyncGenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.create = async_to_raw_response_wrapper(
            generate_synthetic_data.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generate_synthetic_data.retrieve,
        )

    @cached_property
    def data(self) -> AsyncDataResourceWithRawResponse:
        return AsyncDataResourceWithRawResponse(self._generate_synthetic_data.data)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._generate_synthetic_data.messages)


class GenerateSyntheticDataResourceWithStreamingResponse:
    def __init__(self, generate_synthetic_data: GenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.create = to_streamed_response_wrapper(
            generate_synthetic_data.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generate_synthetic_data.retrieve,
        )

    @cached_property
    def data(self) -> DataResourceWithStreamingResponse:
        return DataResourceWithStreamingResponse(self._generate_synthetic_data.data)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._generate_synthetic_data.messages)


class AsyncGenerateSyntheticDataResourceWithStreamingResponse:
    def __init__(self, generate_synthetic_data: AsyncGenerateSyntheticDataResource) -> None:
        self._generate_synthetic_data = generate_synthetic_data

        self.create = async_to_streamed_response_wrapper(
            generate_synthetic_data.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generate_synthetic_data.retrieve,
        )

    @cached_property
    def data(self) -> AsyncDataResourceWithStreamingResponse:
        return AsyncDataResourceWithStreamingResponse(self._generate_synthetic_data.data)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._generate_synthetic_data.messages)
