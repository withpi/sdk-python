# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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
from ..._base_client import make_request_options
from ...types.scoring_system import calibrate_list_params, calibrate_start_job_params
from ...types.shared_params.scoring_spec import ScoringSpec
from ...types.scoring_system.calibrate_list_response import CalibrateListResponse
from ...types.scoring_system.calibrate_retrieve_response import CalibrateRetrieveResponse
from ...types.scoring_system.calibrate_start_job_response import CalibrateStartJobResponse

__all__ = ["CalibrateResource", "AsyncCalibrateResource"]


class CalibrateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalibrateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return CalibrateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalibrateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return CalibrateResourceWithStreamingResponse(self)

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
    ) -> CalibrateRetrieveResponse:
        """
        Checks the status of a Scoring Spec Calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/scoring_system/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrateRetrieveResponse,
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
    ) -> CalibrateListResponse:
        """
        Lists the Scoring Spec Calibration Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/scoring_system/calibrate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, calibrate_list_params.CalibrateListParams),
            ),
            cast_to=CalibrateListResponse,
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
        Cancels a Scoring Spec Calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/scoring_system/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def start_job(
        self,
        *,
        scoring_spec: ScoringSpec,
        examples: Optional[Iterable[calibrate_start_job_params.Example]] | NotGiven = NOT_GIVEN,
        preference_examples: Optional[Iterable[calibrate_start_job_params.PreferenceExample]] | NotGiven = NOT_GIVEN,
        strategy: Literal["LITE", "FULL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrateStartJobResponse:
        """
        Starts a Scoring Spec Calibration job

        Args:
          scoring_spec: The scoring spec to calibrate

          examples: Rated examples to use when calibrating the scoring spec. Must specify either the
              examples or the preference examples

          preference_examples: Preference examples to use when calibrating the scoring spec. Must specify
              either the examples or preference examples

          strategy: The strategy to use to calibrate the scoring spec. FULL would take longer than
              LITE but may result in better result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scoring_system/calibrate",
            body=maybe_transform(
                {
                    "scoring_spec": scoring_spec,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "strategy": strategy,
                },
                calibrate_start_job_params.CalibrateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrateStartJobResponse,
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
        Opens a message stream about a Scoring Spec Calibration job

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
            f"/scoring_system/calibrate/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncCalibrateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalibrateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalibrateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalibrateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncCalibrateResourceWithStreamingResponse(self)

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
    ) -> CalibrateRetrieveResponse:
        """
        Checks the status of a Scoring Spec Calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/scoring_system/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrateRetrieveResponse,
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
    ) -> CalibrateListResponse:
        """
        Lists the Scoring Spec Calibration Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/scoring_system/calibrate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"state": state}, calibrate_list_params.CalibrateListParams),
            ),
            cast_to=CalibrateListResponse,
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
        Cancels a Scoring Spec Calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/scoring_system/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def start_job(
        self,
        *,
        scoring_spec: ScoringSpec,
        examples: Optional[Iterable[calibrate_start_job_params.Example]] | NotGiven = NOT_GIVEN,
        preference_examples: Optional[Iterable[calibrate_start_job_params.PreferenceExample]] | NotGiven = NOT_GIVEN,
        strategy: Literal["LITE", "FULL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrateStartJobResponse:
        """
        Starts a Scoring Spec Calibration job

        Args:
          scoring_spec: The scoring spec to calibrate

          examples: Rated examples to use when calibrating the scoring spec. Must specify either the
              examples or the preference examples

          preference_examples: Preference examples to use when calibrating the scoring spec. Must specify
              either the examples or preference examples

          strategy: The strategy to use to calibrate the scoring spec. FULL would take longer than
              LITE but may result in better result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scoring_system/calibrate",
            body=await async_maybe_transform(
                {
                    "scoring_spec": scoring_spec,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "strategy": strategy,
                },
                calibrate_start_job_params.CalibrateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrateStartJobResponse,
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
        Opens a message stream about a Scoring Spec Calibration job

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
            f"/scoring_system/calibrate/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class CalibrateResourceWithRawResponse:
    def __init__(self, calibrate: CalibrateResource) -> None:
        self._calibrate = calibrate

        self.retrieve = to_raw_response_wrapper(
            calibrate.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calibrate.list,
        )
        self.cancel = to_raw_response_wrapper(
            calibrate.cancel,
        )
        self.start_job = to_raw_response_wrapper(
            calibrate.start_job,
        )
        self.stream_messages = to_raw_response_wrapper(
            calibrate.stream_messages,
        )


class AsyncCalibrateResourceWithRawResponse:
    def __init__(self, calibrate: AsyncCalibrateResource) -> None:
        self._calibrate = calibrate

        self.retrieve = async_to_raw_response_wrapper(
            calibrate.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calibrate.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            calibrate.cancel,
        )
        self.start_job = async_to_raw_response_wrapper(
            calibrate.start_job,
        )
        self.stream_messages = async_to_raw_response_wrapper(
            calibrate.stream_messages,
        )


class CalibrateResourceWithStreamingResponse:
    def __init__(self, calibrate: CalibrateResource) -> None:
        self._calibrate = calibrate

        self.retrieve = to_streamed_response_wrapper(
            calibrate.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calibrate.list,
        )
        self.cancel = to_streamed_response_wrapper(
            calibrate.cancel,
        )
        self.start_job = to_streamed_response_wrapper(
            calibrate.start_job,
        )
        self.stream_messages = to_streamed_response_wrapper(
            calibrate.stream_messages,
        )


class AsyncCalibrateResourceWithStreamingResponse:
    def __init__(self, calibrate: AsyncCalibrateResource) -> None:
        self._calibrate = calibrate

        self.retrieve = async_to_streamed_response_wrapper(
            calibrate.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calibrate.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            calibrate.cancel,
        )
        self.start_job = async_to_streamed_response_wrapper(
            calibrate.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            calibrate.stream_messages,
        )
