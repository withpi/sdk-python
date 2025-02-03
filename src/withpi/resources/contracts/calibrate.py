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
from ...types.contracts import calibrate_start_job_params
from ...types.shared_params.contract import Contract
from ...types.contracts.contract_calibration_status import ContractCalibrationStatus

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
    ) -> ContractCalibrationStatus:
        """
        Checks on a contract calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/contracts/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCalibrationStatus,
        )

    def start_job(
        self,
        *,
        contract: Contract,
        examples: Optional[Iterable[calibrate_start_job_params.Example]] | NotGiven = NOT_GIVEN,
        preference_examples: Optional[Iterable[calibrate_start_job_params.PreferenceExample]] | NotGiven = NOT_GIVEN,
        strategy: Literal["LITE", "FULL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractCalibrationStatus:
        """
        Start a contract calibration job

        Args:
          contract: The contract to calibrate

          examples: Rated examples to use when calibrating the contract. Must specify either the
              examples or the preference examples

          preference_examples: Preference examples to use when calibrating the contract. Must specify either
              the examples or preference examples

          strategy: The strategy to use to calibrate the contract. FULL would take longer than LITE
              but may result in better result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/calibrate",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "strategy": strategy,
                },
                calibrate_start_job_params.CalibrateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCalibrationStatus,
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
        Opens a message stream about a contract calibration job

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
            f"/contracts/calibrate/{job_id}/messages",
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
    ) -> ContractCalibrationStatus:
        """
        Checks on a contract calibration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/contracts/calibrate/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCalibrationStatus,
        )

    async def start_job(
        self,
        *,
        contract: Contract,
        examples: Optional[Iterable[calibrate_start_job_params.Example]] | NotGiven = NOT_GIVEN,
        preference_examples: Optional[Iterable[calibrate_start_job_params.PreferenceExample]] | NotGiven = NOT_GIVEN,
        strategy: Literal["LITE", "FULL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractCalibrationStatus:
        """
        Start a contract calibration job

        Args:
          contract: The contract to calibrate

          examples: Rated examples to use when calibrating the contract. Must specify either the
              examples or the preference examples

          preference_examples: Preference examples to use when calibrating the contract. Must specify either
              the examples or preference examples

          strategy: The strategy to use to calibrate the contract. FULL would take longer than LITE
              but may result in better result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/calibrate",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "preference_examples": preference_examples,
                    "strategy": strategy,
                },
                calibrate_start_job_params.CalibrateStartJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCalibrationStatus,
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
        Opens a message stream about a contract calibration job

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
            f"/contracts/calibrate/{job_id}/messages",
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
        self.start_job = async_to_streamed_response_wrapper(
            calibrate.start_job,
        )
        self.stream_messages = async_to_streamed_response_wrapper(
            calibrate.stream_messages,
        )
