# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import calibration_calibrate_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.calibration_result import CalibrationResult
from ..types.shared_params.contract import Contract

__all__ = ["CalibrationResource", "AsyncCalibrationResource"]


class CalibrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalibrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return CalibrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalibrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return CalibrationResourceWithStreamingResponse(self)

    def calibrate(
        self,
        *,
        contract: Contract,
        feedbacks: Iterable[calibration_calibrate_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationResult:
        """
        Calibrates a contract

        Args:
          contract: A collection of dimensions an LLM response must adhere to

          feedbacks: The list of Feedbacks to use for calibration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calibration",
            body=maybe_transform(
                {
                    "contract": contract,
                    "feedbacks": feedbacks,
                },
                calibration_calibrate_params.CalibrationCalibrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationResult,
        )


class AsyncCalibrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalibrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalibrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalibrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncCalibrationResourceWithStreamingResponse(self)

    async def calibrate(
        self,
        *,
        contract: Contract,
        feedbacks: Iterable[calibration_calibrate_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationResult:
        """
        Calibrates a contract

        Args:
          contract: A collection of dimensions an LLM response must adhere to

          feedbacks: The list of Feedbacks to use for calibration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calibration",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "feedbacks": feedbacks,
                },
                calibration_calibrate_params.CalibrationCalibrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationResult,
        )


class CalibrationResourceWithRawResponse:
    def __init__(self, calibration: CalibrationResource) -> None:
        self._calibration = calibration

        self.calibrate = to_raw_response_wrapper(
            calibration.calibrate,
        )


class AsyncCalibrationResourceWithRawResponse:
    def __init__(self, calibration: AsyncCalibrationResource) -> None:
        self._calibration = calibration

        self.calibrate = async_to_raw_response_wrapper(
            calibration.calibrate,
        )


class CalibrationResourceWithStreamingResponse:
    def __init__(self, calibration: CalibrationResource) -> None:
        self._calibration = calibration

        self.calibrate = to_streamed_response_wrapper(
            calibration.calibrate,
        )


class AsyncCalibrationResourceWithStreamingResponse:
    def __init__(self, calibration: AsyncCalibrationResource) -> None:
        self._calibration = calibration

        self.calibrate = async_to_streamed_response_wrapper(
            calibration.calibrate,
        )
