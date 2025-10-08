# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.search import ConsistencyCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsistency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check(self, client: PiClient) -> None:
        consistency = client.search.consistency.check(
            output1="output1",
            output2="output2",
        )
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: PiClient) -> None:
        consistency = client.search.consistency.check(
            output1="output1",
            output2="output2",
            query="query",
        )
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: PiClient) -> None:
        response = client.search.consistency.with_raw_response.check(
            output1="output1",
            output2="output2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consistency = response.parse()
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: PiClient) -> None:
        with client.search.consistency.with_streaming_response.check(
            output1="output1",
            output2="output2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consistency = response.parse()
            assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConsistency:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncPiClient) -> None:
        consistency = await async_client.search.consistency.check(
            output1="output1",
            output2="output2",
        )
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncPiClient) -> None:
        consistency = await async_client.search.consistency.check(
            output1="output1",
            output2="output2",
            query="query",
        )
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.consistency.with_raw_response.check(
            output1="output1",
            output2="output2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consistency = await response.parse()
        assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.consistency.with_streaming_response.check(
            output1="output1",
            output2="output2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consistency = await response.parse()
            assert_matches_type(ConsistencyCheckResponse, consistency, path=["response"])

        assert cast(Any, response.is_closed) is True
