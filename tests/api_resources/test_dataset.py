# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import DatasetSampleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_sample(self, client: PiClient) -> None:
        dataset = client.dataset.sample(
            name="name",
            split="split",
            subset="subset",
        )
        assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_sample(self, client: PiClient) -> None:
        response = client.dataset.with_raw_response.sample(
            name="name",
            split="split",
            subset="subset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_sample(self, client: PiClient) -> None:
        with client.dataset.with_streaming_response.sample(
            name="name",
            split="split",
            subset="subset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataset:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_sample(self, async_client: AsyncPiClient) -> None:
        dataset = await async_client.dataset.sample(
            name="name",
            split="split",
            subset="subset",
        )
        assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_sample(self, async_client: AsyncPiClient) -> None:
        response = await async_client.dataset.with_raw_response.sample(
            name="name",
            split="split",
            subset="subset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_sample(self, async_client: AsyncPiClient) -> None:
        async with async_client.dataset.with_streaming_response.sample(
            name="name",
            split="split",
            subset="subset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetSampleResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
