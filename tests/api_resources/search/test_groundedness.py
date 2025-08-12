# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.search import GroundednessCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroundedness:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check(self, client: PiClient) -> None:
        groundedness = client.search.groundedness.check(
            context="context",
            output="output",
        )
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: PiClient) -> None:
        groundedness = client.search.groundedness.check(
            context="context",
            output="output",
            processing_strategy="speed_optimized",
            query="query",
        )
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: PiClient) -> None:
        response = client.search.groundedness.with_raw_response.check(
            context="context",
            output="output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundedness = response.parse()
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: PiClient) -> None:
        with client.search.groundedness.with_streaming_response.check(
            context="context",
            output="output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundedness = response.parse()
            assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundedness:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncPiClient) -> None:
        groundedness = await async_client.search.groundedness.check(
            context="context",
            output="output",
        )
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncPiClient) -> None:
        groundedness = await async_client.search.groundedness.check(
            context="context",
            output="output",
            processing_strategy="speed_optimized",
            query="query",
        )
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.groundedness.with_raw_response.check(
            context="context",
            output="output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundedness = await response.parse()
        assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.groundedness.with_streaming_response.check(
            context="context",
            output="output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundedness = await response.parse()
            assert_matches_type(GroundednessCheckResponse, groundedness, path=["response"])

        assert cast(Any, response.is_closed) is True
