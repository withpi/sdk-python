# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.search import QueryToPassageRankDocumentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueryToPassage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rank_documents(self, client: PiClient) -> None:
        query_to_passage = client.search.query_to_passage.rank_documents(
            passages=["string"],
            query="query",
        )
        assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rank_documents(self, client: PiClient) -> None:
        response = client.search.query_to_passage.with_raw_response.rank_documents(
            passages=["string"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_to_passage = response.parse()
        assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rank_documents(self, client: PiClient) -> None:
        with client.search.query_to_passage.with_streaming_response.rank_documents(
            passages=["string"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_to_passage = response.parse()
            assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueryToPassage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rank_documents(self, async_client: AsyncPiClient) -> None:
        query_to_passage = await async_client.search.query_to_passage.rank_documents(
            passages=["string"],
            query="query",
        )
        assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rank_documents(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_to_passage.with_raw_response.rank_documents(
            passages=["string"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_to_passage = await response.parse()
        assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rank_documents(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_to_passage.with_streaming_response.rank_documents(
            passages=["string"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_to_passage = await response.parse()
            assert_matches_type(QueryToPassageRankDocumentsResponse, query_to_passage, path=["response"])

        assert cast(Any, response.is_closed) is True
