# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    scoring_system_score_params,
    scoring_system_read_from_hf_params,
    scoring_system_generate_dimensions_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .calibrate import (
    CalibrateResource,
    AsyncCalibrateResource,
    CalibrateResourceWithRawResponse,
    AsyncCalibrateResourceWithRawResponse,
    CalibrateResourceWithStreamingResponse,
    AsyncCalibrateResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.scoring_system_score_response import ScoringSystemScoreResponse
from ...types.scoring_system_read_from_hf_response import ScoringSystemReadFromHfResponse
from ...types.scoring_system_generate_dimensions_response import ScoringSystemGenerateDimensionsResponse

__all__ = ["ScoringSystemResource", "AsyncScoringSystemResource"]


class ScoringSystemResource(SyncAPIResource):
    @cached_property
    def calibrate(self) -> CalibrateResource:
        return CalibrateResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScoringSystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScoringSystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoringSystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return ScoringSystemResourceWithStreamingResponse(self)

    def generate_dimensions(
        self,
        *,
        application_description: str,
        try_auto_generating_python_code: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemGenerateDimensionsResponse:
        """
        Generates dimensions for a scoring system which will be used to evaluate it

        Args:
          application_description: The application description to generate a scoring system for.

          try_auto_generating_python_code: If true, try to generate python code for sub-dimensions with structured
              evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/generate_dimensions",
            body=maybe_transform(
                {
                    "application_description": application_description,
                    "try_auto_generating_python_code": try_auto_generating_python_code,
                },
                scoring_system_generate_dimensions_params.ScoringSystemGenerateDimensionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemGenerateDimensionsResponse,
        )

    def read_from_hf(
        self,
        *,
        hf_scoring_system_name: str,
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemReadFromHfResponse:
        """
        Read a scoring system from Huggingface dataset

        Args:
          hf_scoring_system_name: Huggingface scoring system name e.g. withpi/my_scoring_system. You need to
              provide the hf_token if the scoring system dataset is not public or not own by
              the withpi organization.

          hf_token: Huggingface token to use if you want to read to your own HF organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/read_from_hf",
            body=maybe_transform(
                {
                    "hf_scoring_system_name": hf_scoring_system_name,
                    "hf_token": hf_token,
                },
                scoring_system_read_from_hf_params.ScoringSystemReadFromHfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemReadFromHfResponse,
        )

    def score(
        self,
        *,
        llm_input: str,
        llm_output: str,
        scoring_system: scoring_system_score_params.ScoringSystem,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemScoreResponse:
        """
        Scores a scoring system based on the provided input and output

        Args:
          llm_input: The input to score

          llm_output: The output to score

          scoring_system: The scoring system to score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/score",
            body=maybe_transform(
                {
                    "llm_input": llm_input,
                    "llm_output": llm_output,
                    "scoring_system": scoring_system,
                },
                scoring_system_score_params.ScoringSystemScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemScoreResponse,
        )


class AsyncScoringSystemResource(AsyncAPIResource):
    @cached_property
    def calibrate(self) -> AsyncCalibrateResource:
        return AsyncCalibrateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScoringSystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoringSystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoringSystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncScoringSystemResourceWithStreamingResponse(self)

    async def generate_dimensions(
        self,
        *,
        application_description: str,
        try_auto_generating_python_code: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemGenerateDimensionsResponse:
        """
        Generates dimensions for a scoring system which will be used to evaluate it

        Args:
          application_description: The application description to generate a scoring system for.

          try_auto_generating_python_code: If true, try to generate python code for sub-dimensions with structured
              evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/generate_dimensions",
            body=await async_maybe_transform(
                {
                    "application_description": application_description,
                    "try_auto_generating_python_code": try_auto_generating_python_code,
                },
                scoring_system_generate_dimensions_params.ScoringSystemGenerateDimensionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemGenerateDimensionsResponse,
        )

    async def read_from_hf(
        self,
        *,
        hf_scoring_system_name: str,
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemReadFromHfResponse:
        """
        Read a scoring system from Huggingface dataset

        Args:
          hf_scoring_system_name: Huggingface scoring system name e.g. withpi/my_scoring_system. You need to
              provide the hf_token if the scoring system dataset is not public or not own by
              the withpi organization.

          hf_token: Huggingface token to use if you want to read to your own HF organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/read_from_hf",
            body=await async_maybe_transform(
                {
                    "hf_scoring_system_name": hf_scoring_system_name,
                    "hf_token": hf_token,
                },
                scoring_system_read_from_hf_params.ScoringSystemReadFromHfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemReadFromHfResponse,
        )

    async def score(
        self,
        *,
        llm_input: str,
        llm_output: str,
        scoring_system: scoring_system_score_params.ScoringSystem,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemScoreResponse:
        """
        Scores a scoring system based on the provided input and output

        Args:
          llm_input: The input to score

          llm_output: The output to score

          scoring_system: The scoring system to score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/score",
            body=await async_maybe_transform(
                {
                    "llm_input": llm_input,
                    "llm_output": llm_output,
                    "scoring_system": scoring_system,
                },
                scoring_system_score_params.ScoringSystemScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemScoreResponse,
        )


class ScoringSystemResourceWithRawResponse:
    def __init__(self, scoring_system: ScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.generate_dimensions = to_raw_response_wrapper(
            scoring_system.generate_dimensions,
        )
        self.read_from_hf = to_raw_response_wrapper(
            scoring_system.read_from_hf,
        )
        self.score = to_raw_response_wrapper(
            scoring_system.score,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithRawResponse:
        return CalibrateResourceWithRawResponse(self._scoring_system.calibrate)


class AsyncScoringSystemResourceWithRawResponse:
    def __init__(self, scoring_system: AsyncScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.generate_dimensions = async_to_raw_response_wrapper(
            scoring_system.generate_dimensions,
        )
        self.read_from_hf = async_to_raw_response_wrapper(
            scoring_system.read_from_hf,
        )
        self.score = async_to_raw_response_wrapper(
            scoring_system.score,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithRawResponse:
        return AsyncCalibrateResourceWithRawResponse(self._scoring_system.calibrate)


class ScoringSystemResourceWithStreamingResponse:
    def __init__(self, scoring_system: ScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.generate_dimensions = to_streamed_response_wrapper(
            scoring_system.generate_dimensions,
        )
        self.read_from_hf = to_streamed_response_wrapper(
            scoring_system.read_from_hf,
        )
        self.score = to_streamed_response_wrapper(
            scoring_system.score,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithStreamingResponse:
        return CalibrateResourceWithStreamingResponse(self._scoring_system.calibrate)


class AsyncScoringSystemResourceWithStreamingResponse:
    def __init__(self, scoring_system: AsyncScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.generate_dimensions = async_to_streamed_response_wrapper(
            scoring_system.generate_dimensions,
        )
        self.read_from_hf = async_to_streamed_response_wrapper(
            scoring_system.read_from_hf,
        )
        self.score = async_to_streamed_response_wrapper(
            scoring_system.score,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithStreamingResponse:
        return AsyncCalibrateResourceWithStreamingResponse(self._scoring_system.calibrate)
