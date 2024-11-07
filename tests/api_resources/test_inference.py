# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import InferenceRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_overload_1(self, client: Twopir) -> None:
        inference = client.inference.run(
            body="body",
        )
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    def test_raw_response_run_overload_1(self, client: Twopir) -> None:
        response = client.inference.with_raw_response.run(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_1(self, client: Twopir) -> None:
        with client.inference.with_streaming_response.run(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceRunResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_2(self, client: Twopir) -> None:
        inference = client.inference.run(
            body={"foo": "string"},
        )
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    def test_raw_response_run_overload_2(self, client: Twopir) -> None:
        response = client.inference.with_raw_response.run(
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Twopir) -> None:
        with client.inference.with_streaming_response.run(
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceRunResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInference:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncTwopir) -> None:
        inference = await async_client.inference.run(
            body="body",
        )
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncTwopir) -> None:
        response = await async_client.inference.with_raw_response.run(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncTwopir) -> None:
        async with async_client.inference.with_streaming_response.run(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceRunResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncTwopir) -> None:
        inference = await async_client.inference.run(
            body={"foo": "string"},
        )
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncTwopir) -> None:
        response = await async_client.inference.with_raw_response.run(
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceRunResponse, inference, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncTwopir) -> None:
        async with async_client.inference.with_streaming_response.run(
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceRunResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True
