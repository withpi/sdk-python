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
from ..._base_client import make_request_options
from ...types.scoring_system import generate_list_params, generate_start_job_params
from ...types.shared_params.question import Question
from ...types.scoring_system.generate_list_response import GenerateListResponse
from ...types.scoring_system.generate_retrieve_response import GenerateRetrieveResponse
from ...types.scoring_system.generate_start_job_response import GenerateStartJobResponse

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

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
    ) -> GenerateRetrieveResponse:
        """
        Checks the status of a Generate Scoring Spec job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/scoring_system/generate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateRetrieveResponse,
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
    ) -> GenerateListResponse:
        """
        Lists the Generate Scoring Spec Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/scoring_system/generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, generate_list_params.GenerateListParams),
            ),
            cast_to=GenerateListResponse,
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
        Cancels a Generate Scoring Spec job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/scoring_system/generate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def start_job(
        self,
        *,
        application_description: str,
        examples: Iterable[generate_start_job_params.Example],
        preference_examples: Iterable[generate_start_job_params.PreferenceExample],
        batch_size: int | NotGiven = NOT_GIVEN,
        existing_questions: Iterable[Question] | NotGiven = NOT_GIVEN,
        num_questions: int | NotGiven = NOT_GIVEN,
        retain_existing_questions: bool | NotGiven = NOT_GIVEN,
        try_auto_generating_python_code: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateStartJobResponse:
        """
        Starts a Generate Scoring Spec job

        Args:
          application_description: The application description to generate a scoring spec for.

          examples: Rated examples to use for generating the discriminating questions. The scores
              can be class labels or actual scores (but must be between 0 and 1)

          preference_examples: Preference examples to use for generating the discriminating questions. Must
              specify either the examples or preference examples

          batch_size: Number of examples to use in one batch to generate the questions.

          existing_questions: Existing questions for the applications, these may or may not be retained in the
              output depending on their performance

          num_questions: The number of questions that the generated scoring system should contain. If <=
              0, then the number is auto selected.

          retain_existing_questions: If true, only generate new questions that improve the accuracy.

          try_auto_generating_python_code: If true, try to generate python code for the generated questions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/generate",
            body=maybe_transform(
                {
                    "application_description": application_description,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "batch_size": batch_size,
                    "existing_questions": existing_questions,
                    "num_questions": num_questions,
                    "retain_existing_questions": retain_existing_questions,
                    "try_auto_generating_python_code": try_auto_generating_python_code,
                },
                generate_start_job_params.GenerateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateStartJobResponse,
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
        Opens a message stream about a Generate Scoring Spec job

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
            f"/scoring_system/generate/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

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
    ) -> GenerateRetrieveResponse:
        """
        Checks the status of a Generate Scoring Spec job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/scoring_system/generate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateRetrieveResponse,
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
    ) -> GenerateListResponse:
        """
        Lists the Generate Scoring Spec Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/scoring_system/generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"state": state}, generate_list_params.GenerateListParams),
            ),
            cast_to=GenerateListResponse,
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
        Cancels a Generate Scoring Spec job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/scoring_system/generate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        application_description: str,
        examples: Iterable[generate_start_job_params.Example],
        preference_examples: Iterable[generate_start_job_params.PreferenceExample],
        batch_size: int | NotGiven = NOT_GIVEN,
        existing_questions: Iterable[Question] | NotGiven = NOT_GIVEN,
        num_questions: int | NotGiven = NOT_GIVEN,
        retain_existing_questions: bool | NotGiven = NOT_GIVEN,
        try_auto_generating_python_code: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateStartJobResponse:
        """
        Starts a Generate Scoring Spec job

        Args:
          application_description: The application description to generate a scoring spec for.

          examples: Rated examples to use for generating the discriminating questions. The scores
              can be class labels or actual scores (but must be between 0 and 1)

          preference_examples: Preference examples to use for generating the discriminating questions. Must
              specify either the examples or preference examples

          batch_size: Number of examples to use in one batch to generate the questions.

          existing_questions: Existing questions for the applications, these may or may not be retained in the
              output depending on their performance

          num_questions: The number of questions that the generated scoring system should contain. If <=
              0, then the number is auto selected.

          retain_existing_questions: If true, only generate new questions that improve the accuracy.

          try_auto_generating_python_code: If true, try to generate python code for the generated questions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/generate",
            body=await async_maybe_transform(
                {
                    "application_description": application_description,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "batch_size": batch_size,
                    "existing_questions": existing_questions,
                    "num_questions": num_questions,
                    "retain_existing_questions": retain_existing_questions,
                    "try_auto_generating_python_code": try_auto_generating_python_code,
                },
                generate_start_job_params.GenerateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateStartJobResponse,
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
        Opens a message stream about a Generate Scoring Spec job

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
            f"/scoring_system/generate/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.retrieve = to_raw_response_wrapper(
            generate.retrieve,
        )
        self.list = to_raw_response_wrapper(
            generate.list,
        )
        self.cancel = to_raw_response_wrapper(
            generate.cancel,
        )
        self.start_job = to_raw_response_wrapper(
            generate.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            generate.stream_messages,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.retrieve = async_to_raw_response_wrapper(
            generate.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            generate.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            generate.cancel,
        )
        self.start_job = async_to_raw_response_wrapper(
            generate.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            generate.stream_messages,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.retrieve = to_streamed_response_wrapper(
            generate.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            generate.list,
        )
        self.cancel = to_streamed_response_wrapper(
            generate.cancel,
        )
        self.start_job = to_streamed_response_wrapper(
            generate.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            generate.stream_messages,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.retrieve = async_to_streamed_response_wrapper(
            generate.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            generate.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            generate.cancel,
        )
        self.start_job = async_to_streamed_response_wrapper(
            generate.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            generate.stream_messages,
        )
