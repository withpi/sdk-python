# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import SearchEmbedDocumentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_embed_documents(self, client: PiClient) -> None:
        search = client.search.embed_documents(
            batch=["string"],
            query=["string"],
        )
        assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_embed_documents(self, client: PiClient) -> None:
        response = client.search.with_raw_response.embed_documents(
            batch=["string"],
            query=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_embed_documents(self, client: PiClient) -> None:
        with client.search.with_streaming_response.embed_documents(
            batch=["string"],
            query=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_embed_documents(self, async_client: AsyncPiClient) -> None:
        search = await async_client.search.embed_documents(
            batch=["string"],
            query=["string"],
        )
        assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_embed_documents(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.with_raw_response.embed_documents(
            batch=["string"],
            query=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_embed_documents(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.with_streaming_response.embed_documents(
            batch=["string"],
            query=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchEmbedDocumentsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
