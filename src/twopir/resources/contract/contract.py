# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ...types import (
    contract_score_params,
    contract_calibrate_params,
    contract_generate_dimensions_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .dimension import (
    DimensionResource,
    AsyncDimensionResource,
    DimensionResourceWithRawResponse,
    AsyncDimensionResourceWithRawResponse,
    DimensionResourceWithStreamingResponse,
    AsyncDimensionResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.contract import Contract as SharedContract
from ...types.shared_params.contract import Contract as SharedParamsContract
from ...types.contract_score_response import ContractScoreResponse

__all__ = ["ContractResource", "AsyncContractResource"]


class ContractResource(SyncAPIResource):
    @cached_property
    def dimension(self) -> DimensionResource:
        return DimensionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return ContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return ContractResourceWithStreamingResponse(self)

    def calibrate(
        self,
        *,
        contract: SharedParamsContract,
        feedbacks: Iterable[contract_calibrate_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Calibrates a contract

        Args:
          contract: The contract to calibrate

          feedbacks: The feedbacks to use for calibration

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
                    "feedbacks": feedbacks,
                },
                contract_calibrate_params.ContractCalibrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedContract,
        )

    def generate_dimensions(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Genrate dimensions for a contract

        Args:
          description: The description of the contract

          name: The name of the contract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/generate_dimensions",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                contract_generate_dimensions_params.ContractGenerateDimensionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedContract,
        )

    def score(
        self,
        *,
        contract: SharedParamsContract,
        llm_input: Union[str, Dict[str, str]],
        llm_output: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractScoreResponse:
        """
        Scores a contract

        Args:
          contract: The contract to score

          llm_input: The input to score

          llm_output: The output to score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/score",
            body=maybe_transform(
                {
                    "contract": contract,
                    "llm_input": llm_input,
                    "llm_output": llm_output,
                },
                contract_score_params.ContractScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractScoreResponse,
        )


class AsyncContractResource(AsyncAPIResource):
    @cached_property
    def dimension(self) -> AsyncDimensionResource:
        return AsyncDimensionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncContractResourceWithStreamingResponse(self)

    async def calibrate(
        self,
        *,
        contract: SharedParamsContract,
        feedbacks: Iterable[contract_calibrate_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Calibrates a contract

        Args:
          contract: The contract to calibrate

          feedbacks: The feedbacks to use for calibration

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
                    "feedbacks": feedbacks,
                },
                contract_calibrate_params.ContractCalibrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedContract,
        )

    async def generate_dimensions(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Genrate dimensions for a contract

        Args:
          description: The description of the contract

          name: The name of the contract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/generate_dimensions",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                contract_generate_dimensions_params.ContractGenerateDimensionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedContract,
        )

    async def score(
        self,
        *,
        contract: SharedParamsContract,
        llm_input: Union[str, Dict[str, str]],
        llm_output: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractScoreResponse:
        """
        Scores a contract

        Args:
          contract: The contract to score

          llm_input: The input to score

          llm_output: The output to score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/score",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "llm_input": llm_input,
                    "llm_output": llm_output,
                },
                contract_score_params.ContractScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractScoreResponse,
        )


class ContractResourceWithRawResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.calibrate = to_raw_response_wrapper(
            contract.calibrate,
        )
        self.generate_dimensions = to_raw_response_wrapper(
            contract.generate_dimensions,
        )
        self.score = to_raw_response_wrapper(
            contract.score,
        )

    @cached_property
    def dimension(self) -> DimensionResourceWithRawResponse:
        return DimensionResourceWithRawResponse(self._contract.dimension)


class AsyncContractResourceWithRawResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.calibrate = async_to_raw_response_wrapper(
            contract.calibrate,
        )
        self.generate_dimensions = async_to_raw_response_wrapper(
            contract.generate_dimensions,
        )
        self.score = async_to_raw_response_wrapper(
            contract.score,
        )

    @cached_property
    def dimension(self) -> AsyncDimensionResourceWithRawResponse:
        return AsyncDimensionResourceWithRawResponse(self._contract.dimension)


class ContractResourceWithStreamingResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.calibrate = to_streamed_response_wrapper(
            contract.calibrate,
        )
        self.generate_dimensions = to_streamed_response_wrapper(
            contract.generate_dimensions,
        )
        self.score = to_streamed_response_wrapper(
            contract.score,
        )

    @cached_property
    def dimension(self) -> DimensionResourceWithStreamingResponse:
        return DimensionResourceWithStreamingResponse(self._contract.dimension)


class AsyncContractResourceWithStreamingResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.calibrate = async_to_streamed_response_wrapper(
            contract.calibrate,
        )
        self.generate_dimensions = async_to_streamed_response_wrapper(
            contract.generate_dimensions,
        )
        self.score = async_to_streamed_response_wrapper(
            contract.score,
        )

    @cached_property
    def dimension(self) -> AsyncDimensionResourceWithStreamingResponse:
        return AsyncDimensionResourceWithStreamingResponse(self._contract.dimension)
