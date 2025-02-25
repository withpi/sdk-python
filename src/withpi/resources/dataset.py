# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import dataset_sample_params
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
from ..types.dataset_sample_response import DatasetSampleResponse

__all__ = ["DatasetResource", "AsyncDatasetResource"]


class DatasetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return DatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return DatasetResourceWithStreamingResponse(self)

    def sample(
        self,
        *,
        name: str,
        split: str,
        subset: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetSampleResponse:
        """Takes 100 uniform samples without replacement from a dataset on Hugging Face.

        If
        the dataset does not have more than 100 rows, the entire dataset is returned.

        Args:
          name: The name of a dataset hosted on Hugging Face.

          split: The split to sample from.

          subset: The subset to sample from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/sample_from_hf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "split": split,
                        "subset": subset,
                    },
                    dataset_sample_params.DatasetSampleParams,
                ),
            ),
            cast_to=DatasetSampleResponse,
        )


class AsyncDatasetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncDatasetResourceWithStreamingResponse(self)

    async def sample(
        self,
        *,
        name: str,
        split: str,
        subset: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetSampleResponse:
        """Takes 100 uniform samples without replacement from a dataset on Hugging Face.

        If
        the dataset does not have more than 100 rows, the entire dataset is returned.

        Args:
          name: The name of a dataset hosted on Hugging Face.

          split: The split to sample from.

          subset: The subset to sample from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/sample_from_hf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "split": split,
                        "subset": subset,
                    },
                    dataset_sample_params.DatasetSampleParams,
                ),
            ),
            cast_to=DatasetSampleResponse,
        )


class DatasetResourceWithRawResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.sample = to_raw_response_wrapper(
            dataset.sample,
        )


class AsyncDatasetResourceWithRawResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.sample = async_to_raw_response_wrapper(
            dataset.sample,
        )


class DatasetResourceWithStreamingResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.sample = to_streamed_response_wrapper(
            dataset.sample,
        )


class AsyncDatasetResourceWithStreamingResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.sample = async_to_streamed_response_wrapper(
            dataset.sample,
        )
