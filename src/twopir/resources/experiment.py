# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import experiment_create_params
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
from ..types.experiment_status import ExperimentStatus

__all__ = ["ExperimentResource", "AsyncExperimentResource"]


class ExperimentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperimentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return ExperimentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return ExperimentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        contract: experiment_create_params.Contract,
        examples: Iterable[experiment_create_params.Example],
        scorer_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentStatus:
        """
        Launches an experiment on a set of data

        Args:
          contract: The contract to evaluate against

          examples: The examples to evaluate

          scorer_id: The scorer id to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experiments",
            body=maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "scorer_id": scorer_id,
                },
                experiment_create_params.ExperimentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperimentStatus,
        )


class AsyncExperimentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperimentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twopir-python#with_streaming_response
        """
        return AsyncExperimentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        contract: experiment_create_params.Contract,
        examples: Iterable[experiment_create_params.Example],
        scorer_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentStatus:
        """
        Launches an experiment on a set of data

        Args:
          contract: The contract to evaluate against

          examples: The examples to evaluate

          scorer_id: The scorer id to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experiments",
            body=await async_maybe_transform(
                {
                    "contract": contract,
                    "examples": examples,
                    "scorer_id": scorer_id,
                },
                experiment_create_params.ExperimentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperimentStatus,
        )


class ExperimentResourceWithRawResponse:
    def __init__(self, experiment: ExperimentResource) -> None:
        self._experiment = experiment

        self.create = to_raw_response_wrapper(
            experiment.create,
        )


class AsyncExperimentResourceWithRawResponse:
    def __init__(self, experiment: AsyncExperimentResource) -> None:
        self._experiment = experiment

        self.create = async_to_raw_response_wrapper(
            experiment.create,
        )


class ExperimentResourceWithStreamingResponse:
    def __init__(self, experiment: ExperimentResource) -> None:
        self._experiment = experiment

        self.create = to_streamed_response_wrapper(
            experiment.create,
        )


class AsyncExperimentResourceWithStreamingResponse:
    def __init__(self, experiment: AsyncExperimentResource) -> None:
        self._experiment = experiment

        self.create = async_to_streamed_response_wrapper(
            experiment.create,
        )
