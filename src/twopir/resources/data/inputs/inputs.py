# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

import httpx

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
from ....types.data import input_evaluate_params
from ...._base_client import make_request_options
from .generate_from_seeds import (
    GenerateFromSeedsResource,
    AsyncGenerateFromSeedsResource,
    GenerateFromSeedsResourceWithRawResponse,
    AsyncGenerateFromSeedsResourceWithRawResponse,
    GenerateFromSeedsResourceWithStreamingResponse,
    AsyncGenerateFromSeedsResourceWithStreamingResponse,
)
from ....types.shared_params.contract import Contract
from ....types.input_evaluation_metrics import InputEvaluationMetrics
from .generate_from_seeds.generate_from_seeds import GenerateFromSeedsResource, AsyncGenerateFromSeedsResource

__all__ = ["InputsResource", "AsyncInputsResource"]


class InputsResource(SyncAPIResource):
    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResource:
        return GenerateFromSeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return InputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return InputsResourceWithStreamingResponse(self)

    def evaluate(
        self,
        *,
        contract: Contract,
        llm_input: Union[str, Dict[str, str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputEvaluationMetrics:
        """
        Evaluate an input

        Args:
          contract: The contract the input is intended to drive

          llm_input: The input to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/input/evaluate",
            body=maybe_transform(
                {
                    "contract": contract,
                    "llm_input": llm_input,
                },
                input_evaluate_params.InputEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputEvaluationMetrics,
        )


class AsyncInputsResource(AsyncAPIResource):
    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResource:
        return AsyncGenerateFromSeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/2pir-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/2pir-ai/sdk-python#with_streaming_response
        """
        return AsyncInputsResourceWithStreamingResponse(self)

    async def evaluate(
        self,
        *,
        contract: Contract,
        llm_input: Union[str, Dict[str, str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputEvaluationMetrics:
        """
        Evaluate an input

        Args:
          contract: The contract the input is intended to drive

          llm_input: The input to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/input/evaluate",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "llm_input": llm_input,
                },
                input_evaluate_params.InputEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputEvaluationMetrics,
        )


class InputsResourceWithRawResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.evaluate = to_raw_response_wrapper(
            inputs.evaluate,
        )

    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResourceWithRawResponse:
        return GenerateFromSeedsResourceWithRawResponse(self._inputs.generate_from_seeds)


class AsyncInputsResourceWithRawResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.evaluate = async_to_raw_response_wrapper(
            inputs.evaluate,
        )

    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResourceWithRawResponse:
        return AsyncGenerateFromSeedsResourceWithRawResponse(self._inputs.generate_from_seeds)


class InputsResourceWithStreamingResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.evaluate = to_streamed_response_wrapper(
            inputs.evaluate,
        )

    @cached_property
    def generate_from_seeds(self) -> GenerateFromSeedsResourceWithStreamingResponse:
        return GenerateFromSeedsResourceWithStreamingResponse(self._inputs.generate_from_seeds)


class AsyncInputsResourceWithStreamingResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.evaluate = async_to_streamed_response_wrapper(
            inputs.evaluate,
        )

    @cached_property
    def generate_from_seeds(self) -> AsyncGenerateFromSeedsResourceWithStreamingResponse:
        return AsyncGenerateFromSeedsResourceWithStreamingResponse(self._inputs.generate_from_seeds)
