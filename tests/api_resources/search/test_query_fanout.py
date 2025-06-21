# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.search import QueryFanoutGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueryFanout:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate(self, client: PiClient) -> None:
        query_fanout = client.search.query_fanout.generate(
            query="Name the four largest fish and what they eat.",
        )
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_with_all_params(self, client: PiClient) -> None:
        query_fanout = client.search.query_fanout.generate(
            query="Name the four largest fish and what they eat.",
            few_shot_examples=[
                {
                    "fanout_queries": [
                        "Genus of the cheetah",
                        "Genus of the pronghorn",
                        "Genus of the springbok",
                        "Genus of the wildebeest",
                        "Genus of the lion",
                    ],
                    "query": "What are the genera of the five fastest land animals?",
                }
            ],
            num_fanout_queries=5,
        )
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate(self, client: PiClient) -> None:
        response = client.search.query_fanout.with_raw_response.generate(
            query="Name the four largest fish and what they eat.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_fanout = response.parse()
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate(self, client: PiClient) -> None:
        with client.search.query_fanout.with_streaming_response.generate(
            query="Name the four largest fish and what they eat.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_fanout = response.parse()
            assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueryFanout:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate(self, async_client: AsyncPiClient) -> None:
        query_fanout = await async_client.search.query_fanout.generate(
            query="Name the four largest fish and what they eat.",
        )
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncPiClient) -> None:
        query_fanout = await async_client.search.query_fanout.generate(
            query="Name the four largest fish and what they eat.",
            few_shot_examples=[
                {
                    "fanout_queries": [
                        "Genus of the cheetah",
                        "Genus of the pronghorn",
                        "Genus of the springbok",
                        "Genus of the wildebeest",
                        "Genus of the lion",
                    ],
                    "query": "What are the genera of the five fastest land animals?",
                }
            ],
            num_fanout_queries=5,
        )
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_fanout.with_raw_response.generate(
            query="Name the four largest fish and what they eat.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_fanout = await response.parse()
        assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_fanout.with_streaming_response.generate(
            query="Name the four largest fish and what they eat.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_fanout = await response.parse()
            assert_matches_type(QueryFanoutGenerateResponse, query_fanout, path=["response"])

        assert cast(Any, response.is_closed) is True
