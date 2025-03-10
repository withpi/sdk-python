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
from ...types.training import sft_list_params, sft_launch_params, sft_download_params
from ...types.shared_params.scorer import Scorer
from ...types.training.sft_list_response import SftListResponse
from ...types.training.sft_load_response import SftLoadResponse
from ...types.training.sft_launch_response import SftLaunchResponse
from ...types.training.sft_status_response import SftStatusResponse

__all__ = ["SftResource", "AsyncSftResource"]


class SftResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return SftResourceWithStreamingResponse(self)

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
    ) -> SftListResponse:
        """
        Lists the SFT Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/training/sft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, sft_list_params.SftListParams),
            ),
            cast_to=SftListResponse,
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
        Cancels a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/training/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def download(
        self,
        job_id: str,
        *,
        serving_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Allows downloading a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/training/sft/{job_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"serving_id": serving_id}, sft_download_params.SftDownloadParams),
            ),
            cast_to=str,
        )

    def launch(
        self,
        *,
        examples: Iterable[sft_launch_params.Example],
        scorer: Scorer,
        base_sft_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        lora_config: sft_launch_params.LoraConfig | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftLaunchResponse:
        """Launches a SFT job

        Args:
          examples: Examples to use in the SFT tuning process.

        We split this data into train/eval
              90/10.

          scorer: The scoring system to use in the SFT tuning process

          base_sft_model: The base model to start the SFT tuning process.

          learning_rate: SFT learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: SFT number of train epochs: <= 10.

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/training/sft",
            body=maybe_transform(
                {
                    "examples": examples,
                    "scorer": scorer,
                    "base_sft_model": base_sft_model,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "system_prompt": system_prompt,
                },
                sft_launch_params.SftLaunchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftLaunchResponse,
        )

    def load(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftLoadResponse:
        """
        Loads a SFT model into serving for a limited period of time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            f"/training/sft/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftLoadResponse,
        )

    def messages(
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
        Opens a message stream about a SFT job

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
            f"/training/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatusResponse:
        """
        Checks the status of a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/training/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatusResponse,
        )


class AsyncSftResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncSftResourceWithStreamingResponse(self)

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
    ) -> SftListResponse:
        """
        Lists the SFT Jobs owned by a user

        Args:
          state: Filter jobs by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/training/sft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"state": state}, sft_list_params.SftListParams),
            ),
            cast_to=SftListResponse,
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
        Cancels a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/training/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def download(
        self,
        job_id: str,
        *,
        serving_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Allows downloading a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/training/sft/{job_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"serving_id": serving_id}, sft_download_params.SftDownloadParams),
            ),
            cast_to=str,
        )

    async def launch(
        self,
        *,
        examples: Iterable[sft_launch_params.Example],
        scorer: Scorer,
        base_sft_model: Literal["LLAMA_3.2_3B", "LLAMA_3.1_8B"] | NotGiven = NOT_GIVEN,
        learning_rate: float | NotGiven = NOT_GIVEN,
        lora_config: sft_launch_params.LoraConfig | NotGiven = NOT_GIVEN,
        num_train_epochs: int | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftLaunchResponse:
        """Launches a SFT job

        Args:
          examples: Examples to use in the SFT tuning process.

        We split this data into train/eval
              90/10.

          scorer: The scoring system to use in the SFT tuning process

          base_sft_model: The base model to start the SFT tuning process.

          learning_rate: SFT learning rate

          lora_config: The LoRA configuration.

          num_train_epochs: SFT number of train epochs: <= 10.

          system_prompt: A custom system prompt to use during the RL tuning process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/training/sft",
            body=await async_maybe_transform(
                {
                    "examples": examples,
                    "scorer": scorer,
                    "base_sft_model": base_sft_model,
                    "learning_rate": learning_rate,
                    "lora_config": lora_config,
                    "num_train_epochs": num_train_epochs,
                    "system_prompt": system_prompt,
                },
                sft_launch_params.SftLaunchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftLaunchResponse,
        )

    async def load(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftLoadResponse:
        """
        Loads a SFT model into serving for a limited period of time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            f"/training/sft/{job_id}/load",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftLoadResponse,
        )

    async def messages(
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
        Opens a message stream about a SFT job

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
            f"/training/sft/{job_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SftStatusResponse:
        """
        Checks the status of a SFT job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/training/sft/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftStatusResponse,
        )


class SftResourceWithRawResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.list = to_raw_response_wrapper(
            sft.list,
        )
        self.cancel = to_raw_response_wrapper(
            sft.cancel,
        )
        self.download = to_raw_response_wrapper(
            sft.download,
        )
        self.launch = to_raw_response_wrapper(
            sft.launch,
        )
        self.load = to_raw_response_wrapper(
            sft.load,
        )
        self.messages = to_raw_response_wrapper(
            sft.messages,
        )
        self.status = to_raw_response_wrapper(
            sft.status,
        )


class AsyncSftResourceWithRawResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.list = async_to_raw_response_wrapper(
            sft.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            sft.cancel,
        )
        self.download = async_to_raw_response_wrapper(
            sft.download,
        )
        self.launch = async_to_raw_response_wrapper(
            sft.launch,
        )
        self.load = async_to_raw_response_wrapper(
            sft.load,
        )
        self.messages = async_to_raw_response_wrapper(
            sft.messages,
        )
        self.status = async_to_raw_response_wrapper(
            sft.status,
        )


class SftResourceWithStreamingResponse:
    def __init__(self, sft: SftResource) -> None:
        self._sft = sft

        self.list = to_streamed_response_wrapper(
            sft.list,
        )
        self.cancel = to_streamed_response_wrapper(
            sft.cancel,
        )
        self.download = to_streamed_response_wrapper(
            sft.download,
        )
        self.launch = to_streamed_response_wrapper(
            sft.launch,
        )
        self.load = to_streamed_response_wrapper(
            sft.load,
        )
        self.messages = to_streamed_response_wrapper(
            sft.messages,
        )
        self.status = to_streamed_response_wrapper(
            sft.status,
        )


class AsyncSftResourceWithStreamingResponse:
    def __init__(self, sft: AsyncSftResource) -> None:
        self._sft = sft

        self.list = async_to_streamed_response_wrapper(
            sft.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            sft.cancel,
        )
        self.download = async_to_streamed_response_wrapper(
            sft.download,
        )
        self.launch = async_to_streamed_response_wrapper(
            sft.launch,
        )
        self.load = async_to_streamed_response_wrapper(
            sft.load,
        )
        self.messages = async_to_streamed_response_wrapper(
            sft.messages,
        )
        self.status = async_to_streamed_response_wrapper(
            sft.status,
        )
