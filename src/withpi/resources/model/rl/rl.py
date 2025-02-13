# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .grpo import (
    GrpoResource,
    AsyncGrpoResource,
    GrpoResourceWithRawResponse,
    AsyncGrpoResourceWithRawResponse,
    GrpoResourceWithStreamingResponse,
    AsyncGrpoResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RlResource", "AsyncRlResource"]


class RlResource(SyncAPIResource):
    @cached_property
    def grpo(self) -> GrpoResource:
        return GrpoResource(self._client)

    @cached_property
    def with_raw_response(self) -> RlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return RlResourceWithStreamingResponse(self)


class AsyncRlResource(AsyncAPIResource):
    @cached_property
    def grpo(self) -> AsyncGrpoResource:
        return AsyncGrpoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/withpi/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/withpi/sdk-python#with_streaming_response
        """
        return AsyncRlResourceWithStreamingResponse(self)


class RlResourceWithRawResponse:
    def __init__(self, rl: RlResource) -> None:
        self._rl = rl

    @cached_property
    def grpo(self) -> GrpoResourceWithRawResponse:
        return GrpoResourceWithRawResponse(self._rl.grpo)


class AsyncRlResourceWithRawResponse:
    def __init__(self, rl: AsyncRlResource) -> None:
        self._rl = rl

    @cached_property
    def grpo(self) -> AsyncGrpoResourceWithRawResponse:
        return AsyncGrpoResourceWithRawResponse(self._rl.grpo)


class RlResourceWithStreamingResponse:
    def __init__(self, rl: RlResource) -> None:
        self._rl = rl

    @cached_property
    def grpo(self) -> GrpoResourceWithStreamingResponse:
        return GrpoResourceWithStreamingResponse(self._rl.grpo)


class AsyncRlResourceWithStreamingResponse:
    def __init__(self, rl: AsyncRlResource) -> None:
        self._rl = rl

    @cached_property
    def grpo(self) -> AsyncGrpoResourceWithStreamingResponse:
        return AsyncGrpoResourceWithStreamingResponse(self._rl.grpo)
