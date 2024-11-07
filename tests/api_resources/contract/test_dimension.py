# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import ContractsScoreMetrics
from twopir.types.shared import Dimension

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDimension:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Twopir) -> None:
        dimension = client.contract.dimension.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        )
        assert_matches_type(Dimension, dimension, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Twopir) -> None:
        response = client.contract.dimension.with_raw_response.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = response.parse()
        assert_matches_type(Dimension, dimension, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Twopir) -> None:
        with client.contract.dimension.with_streaming_response.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = response.parse()
            assert_matches_type(Dimension, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_score(self, client: Twopir) -> None:
        dimension = client.contract.dimension.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Twopir) -> None:
        response = client.contract.dimension.with_raw_response.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = response.parse()
        assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Twopir) -> None:
        with client.contract.dimension.with_streaming_response.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = response.parse()
            assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDimension:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncTwopir) -> None:
        dimension = await async_client.contract.dimension.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        )
        assert_matches_type(Dimension, dimension, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contract.dimension.with_raw_response.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = await response.parse()
        assert_matches_type(Dimension, dimension, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncTwopir) -> None:
        async with async_client.contract.dimension.with_streaming_response.generate(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = await response.parse()
            assert_matches_type(Dimension, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_score(self, async_client: AsyncTwopir) -> None:
        dimension = await async_client.contract.dimension.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contract.dimension.with_raw_response.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = await response.parse()
        assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncTwopir) -> None:
        async with async_client.contract.dimension.with_streaming_response.score(
            dimension={
                "description": "description",
                "label": "label",
                "sub_dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                    {
                        "description": "description",
                        "label": "label",
                    },
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = await response.parse()
            assert_matches_type(ContractsScoreMetrics, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True
