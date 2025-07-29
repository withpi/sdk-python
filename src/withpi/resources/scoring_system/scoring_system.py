# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    scoring_system_score_params,
    scoring_system_import_spec_params,
    scoring_system_upload_to_huggingface_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
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
from ...types.shared_params.question import Question
from ...types.shared.scoring_system_metrics import ScoringSystemMetrics
from ...types.scoring_system_import_spec_response import ScoringSystemImportSpecResponse

__all__ = ["ScoringSystemResource", "AsyncScoringSystemResource"]


class ScoringSystemResource(SyncAPIResource):
    @cached_property
    def calibrate(self) -> CalibrateResource:
        return CalibrateResource(self._client)

    @cached_property
    def generate(self) -> GenerateResource:
        return GenerateResource(self._client)

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

    def import_spec(
        self,
        *,
        hf_scoring_spec_name: str,
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        source: Literal["HUGGINGFACE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemImportSpecResponse:
        """
        Import a scoring spec from various sources

        Args:
          hf_scoring_spec_name: Huggingface dataset e.g. withpi/my_scoring_system containing the Scoring spec.
              This is only needed for the source=HUGGINGFACE.

          hf_token: Huggingface token to use if you want to read to your own HF organization. This
              is only needed for the source=HUGGINGFACE.

          source: Source of where to get the Scoring spec

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/import_spec",
            body=maybe_transform(
                {
                    "hf_scoring_spec_name": hf_scoring_spec_name,
                    "hf_token": hf_token,
                    "source": source,
                },
                scoring_system_import_spec_params.ScoringSystemImportSpecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemImportSpecResponse,
        )

    def score(
        self,
        *,
        llm_input: str,
        llm_output: str,
        scoring_spec: Iterable[Question],
        aggregation_method: Literal["ARITHMETIC_MEAN", "GEOMETRIC_MEAN", "HARMONIC_MEAN"] | NotGiven = NOT_GIVEN,
        kwargs: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemMetrics:
        """
        Scores the provided input and output based on the given scoring spec or a list
        of questions

        Args:
          llm_input: The input to score

          llm_output: The output to score

          scoring_spec: Either a scoring spec or a list of questions to score

          aggregation_method: The strategy to combine the individual question scores to get the total score.
              Defaults to HARMONIC_MEAN.

          kwargs: Optional additional parameters (keyword arguments)

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
                    "scoring_spec": scoring_spec,
                    "aggregation_method": aggregation_method,
                    "kwargs": kwargs,
                },
                scoring_system_score_params.ScoringSystemScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemMetrics,
        )

    def upload_to_huggingface(
        self,
        *,
        hf_scoring_spec_name: str,
        scoring_spec: Iterable[Question],
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Write a scoring spec to Huggingface dataset

        Args:
          hf_scoring_spec_name: Huggingface scoring spec name e.g. withpi/my_scoring_system. By default we
              export to the withpi organization. If you want to use your own organization, we
              provide the hf_token.

          scoring_spec: The list of questions or the scoring spec to write to Huggingface

          hf_token: Huggingface token to use if you want to write to your own HF organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/to_huggingface",
            body=maybe_transform(
                {
                    "hf_scoring_spec_name": hf_scoring_spec_name,
                    "scoring_spec": scoring_spec,
                    "hf_token": hf_token,
                },
                scoring_system_upload_to_huggingface_params.ScoringSystemUploadToHuggingfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncScoringSystemResource(AsyncAPIResource):
    @cached_property
    def calibrate(self) -> AsyncCalibrateResource:
        return AsyncCalibrateResource(self._client)

    @cached_property
    def generate(self) -> AsyncGenerateResource:
        return AsyncGenerateResource(self._client)

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

    async def import_spec(
        self,
        *,
        hf_scoring_spec_name: str,
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        source: Literal["HUGGINGFACE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemImportSpecResponse:
        """
        Import a scoring spec from various sources

        Args:
          hf_scoring_spec_name: Huggingface dataset e.g. withpi/my_scoring_system containing the Scoring spec.
              This is only needed for the source=HUGGINGFACE.

          hf_token: Huggingface token to use if you want to read to your own HF organization. This
              is only needed for the source=HUGGINGFACE.

          source: Source of where to get the Scoring spec

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/import_spec",
            body=await async_maybe_transform(
                {
                    "hf_scoring_spec_name": hf_scoring_spec_name,
                    "hf_token": hf_token,
                    "source": source,
                },
                scoring_system_import_spec_params.ScoringSystemImportSpecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemImportSpecResponse,
        )

    async def score(
        self,
        *,
        llm_input: str,
        llm_output: str,
        scoring_spec: Iterable[Question],
        aggregation_method: Literal["ARITHMETIC_MEAN", "GEOMETRIC_MEAN", "HARMONIC_MEAN"] | NotGiven = NOT_GIVEN,
        kwargs: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoringSystemMetrics:
        """
        Scores the provided input and output based on the given scoring spec or a list
        of questions

        Args:
          llm_input: The input to score

          llm_output: The output to score

          scoring_spec: Either a scoring spec or a list of questions to score

          aggregation_method: The strategy to combine the individual question scores to get the total score.
              Defaults to HARMONIC_MEAN.

          kwargs: Optional additional parameters (keyword arguments)

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
                    "scoring_spec": scoring_spec,
                    "aggregation_method": aggregation_method,
                    "kwargs": kwargs,
                },
                scoring_system_score_params.ScoringSystemScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringSystemMetrics,
        )

    async def upload_to_huggingface(
        self,
        *,
        hf_scoring_spec_name: str,
        scoring_spec: Iterable[Question],
        hf_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Write a scoring spec to Huggingface dataset

        Args:
          hf_scoring_spec_name: Huggingface scoring spec name e.g. withpi/my_scoring_system. By default we
              export to the withpi organization. If you want to use your own organization, we
              provide the hf_token.

          scoring_spec: The list of questions or the scoring spec to write to Huggingface

          hf_token: Huggingface token to use if you want to write to your own HF organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/to_huggingface",
            body=await async_maybe_transform(
                {
                    "hf_scoring_spec_name": hf_scoring_spec_name,
                    "scoring_spec": scoring_spec,
                    "hf_token": hf_token,
                },
                scoring_system_upload_to_huggingface_params.ScoringSystemUploadToHuggingfaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ScoringSystemResourceWithRawResponse:
    def __init__(self, scoring_system: ScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.import_spec = to_raw_response_wrapper(
            scoring_system.import_spec,
        )
        self.score = to_raw_response_wrapper(
            scoring_system.score,
        )
        self.upload_to_huggingface = to_raw_response_wrapper(
            scoring_system.upload_to_huggingface,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithRawResponse:
        return CalibrateResourceWithRawResponse(self._scoring_system.calibrate)

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._scoring_system.generate)


class AsyncScoringSystemResourceWithRawResponse:
    def __init__(self, scoring_system: AsyncScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.import_spec = async_to_raw_response_wrapper(
            scoring_system.import_spec,
        )
        self.score = async_to_raw_response_wrapper(
            scoring_system.score,
        )
        self.upload_to_huggingface = async_to_raw_response_wrapper(
            scoring_system.upload_to_huggingface,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithRawResponse:
        return AsyncCalibrateResourceWithRawResponse(self._scoring_system.calibrate)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._scoring_system.generate)


class ScoringSystemResourceWithStreamingResponse:
    def __init__(self, scoring_system: ScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.import_spec = to_streamed_response_wrapper(
            scoring_system.import_spec,
        )
        self.score = to_streamed_response_wrapper(
            scoring_system.score,
        )
        self.upload_to_huggingface = to_streamed_response_wrapper(
            scoring_system.upload_to_huggingface,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithStreamingResponse:
        return CalibrateResourceWithStreamingResponse(self._scoring_system.calibrate)

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._scoring_system.generate)


class AsyncScoringSystemResourceWithStreamingResponse:
    def __init__(self, scoring_system: AsyncScoringSystemResource) -> None:
        self._scoring_system = scoring_system

        self.import_spec = async_to_streamed_response_wrapper(
            scoring_system.import_spec,
        )
        self.score = async_to_streamed_response_wrapper(
            scoring_system.score,
        )
        self.upload_to_huggingface = async_to_streamed_response_wrapper(
            scoring_system.upload_to_huggingface,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithStreamingResponse:
        return AsyncCalibrateResourceWithStreamingResponse(self._scoring_system.calibrate)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._scoring_system.generate)
