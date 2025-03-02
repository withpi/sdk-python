# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import data_list_question_answer_jobs_params
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
from .inputs.inputs import (
    InputsResource,
    AsyncInputsResource,
    InputsResourceWithRawResponse,
    AsyncInputsResourceWithRawResponse,
    InputsResourceWithStreamingResponse,
    AsyncInputsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.contracts import State
from ...types.contracts.state import State
from .generate_synthetic_data import (
    GenerateSyntheticDataResource,
    AsyncGenerateSyntheticDataResource,
    GenerateSyntheticDataResourceWithRawResponse,
    AsyncGenerateSyntheticDataResourceWithRawResponse,
    GenerateSyntheticDataResourceWithStreamingResponse,
    AsyncGenerateSyntheticDataResourceWithStreamingResponse,
)
from ...types.data_list_question_answer_jobs_response import DataListQuestionAnswerJobsResponse

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def inputs(self) -> InputsResource:
        return InputsResource(self._client)

    @cached_property
    def generate_synthetic_data(self) -> GenerateSyntheticDataResource:
        return GenerateSyntheticDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)

    def list_question_answer_jobs(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataListQuestionAnswerJobsResponse:
        """
        Returns a list of question answer jobs, optionally filtered by state

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/generate_question_answers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"state": state}, data_list_question_answer_jobs_params.DataListQuestionAnswerJobsParams
                ),
            ),
            cast_to=DataListQuestionAnswerJobsResponse,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def inputs(self) -> AsyncInputsResource:
        return AsyncInputsResource(self._client)

    @cached_property
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResource:
        return AsyncGenerateSyntheticDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)

    async def list_question_answer_jobs(
        self,
        *,
        state: Optional[State] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataListQuestionAnswerJobsResponse:
        """
        Returns a list of question answer jobs, optionally filtered by state

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/generate_question_answers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, data_list_question_answer_jobs_params.DataListQuestionAnswerJobsParams
                ),
            ),
            cast_to=DataListQuestionAnswerJobsResponse,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.list_question_answer_jobs = to_raw_response_wrapper(
            data.list_question_answer_jobs,
        )

    @cached_property
    def inputs(self) -> InputsResourceWithRawResponse:
        return InputsResourceWithRawResponse(self._data.inputs)

    @cached_property
    def generate_synthetic_data(self) -> GenerateSyntheticDataResourceWithRawResponse:
        return GenerateSyntheticDataResourceWithRawResponse(self._data.generate_synthetic_data)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.list_question_answer_jobs = async_to_raw_response_wrapper(
            data.list_question_answer_jobs,
        )

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithRawResponse:
        return AsyncInputsResourceWithRawResponse(self._data.inputs)

    @cached_property
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResourceWithRawResponse:
        return AsyncGenerateSyntheticDataResourceWithRawResponse(self._data.generate_synthetic_data)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.list_question_answer_jobs = to_streamed_response_wrapper(
            data.list_question_answer_jobs,
        )

    @cached_property
    def inputs(self) -> InputsResourceWithStreamingResponse:
        return InputsResourceWithStreamingResponse(self._data.inputs)

    @cached_property
    def generate_synthetic_data(self) -> GenerateSyntheticDataResourceWithStreamingResponse:
        return GenerateSyntheticDataResourceWithStreamingResponse(self._data.generate_synthetic_data)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.list_question_answer_jobs = async_to_streamed_response_wrapper(
            data.list_question_answer_jobs,
        )

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithStreamingResponse:
        return AsyncInputsResourceWithStreamingResponse(self._data.inputs)

    @cached_property
    def generate_synthetic_data(self) -> AsyncGenerateSyntheticDataResourceWithStreamingResponse:
        return AsyncGenerateSyntheticDataResourceWithStreamingResponse(self._data.generate_synthetic_data)
