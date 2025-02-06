# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import contract_score_params, contract_generate_dimensions_params
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
from ...types.shared.contract import Contract as SharedContract
from ...types.shared_params.contract import Contract as SharedParamsContract
from ...types.contracts_score_metrics import ContractsScoreMetrics

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def calibrate(self) -> CalibrateResource:
        return CalibrateResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def generate_dimensions(
        self,
        *,
        contract_description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Generates dimensions for a contract which will be used to evaluate it

        Args:
          contract_description: The application description to generate contract for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/generate_dimensions",
            body=maybe_transform(
                {"contract_description": contract_description},
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
        llm_input: str,
        llm_output: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractsScoreMetrics:
        """
        Scores a contract based on the provided input and output

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
            cast_to=ContractsScoreMetrics,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def calibrate(self) -> AsyncCalibrateResource:
        return AsyncCalibrateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def generate_dimensions(
        self,
        *,
        contract_description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedContract:
        """
        Generates dimensions for a contract which will be used to evaluate it

        Args:
          contract_description: The application description to generate contract for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/generate_dimensions",
            body=await async_maybe_transform(
                {"contract_description": contract_description},
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
        llm_input: str,
        llm_output: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractsScoreMetrics:
        """
        Scores a contract based on the provided input and output

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
            cast_to=ContractsScoreMetrics,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.generate_dimensions = to_raw_response_wrapper(
            contracts.generate_dimensions,
        )
        self.score = to_raw_response_wrapper(
            contracts.score,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithRawResponse:
        return CalibrateResourceWithRawResponse(self._contracts.calibrate)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.generate_dimensions = async_to_raw_response_wrapper(
            contracts.generate_dimensions,
        )
        self.score = async_to_raw_response_wrapper(
            contracts.score,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithRawResponse:
        return AsyncCalibrateResourceWithRawResponse(self._contracts.calibrate)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.generate_dimensions = to_streamed_response_wrapper(
            contracts.generate_dimensions,
        )
        self.score = to_streamed_response_wrapper(
            contracts.score,
        )

    @cached_property
    def calibrate(self) -> CalibrateResourceWithStreamingResponse:
        return CalibrateResourceWithStreamingResponse(self._contracts.calibrate)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.generate_dimensions = async_to_streamed_response_wrapper(
            contracts.generate_dimensions,
        )
        self.score = async_to_streamed_response_wrapper(
            contracts.score,
        )

    @cached_property
    def calibrate(self) -> AsyncCalibrateResourceWithStreamingResponse:
        return AsyncCalibrateResourceWithStreamingResponse(self._contracts.calibrate)
