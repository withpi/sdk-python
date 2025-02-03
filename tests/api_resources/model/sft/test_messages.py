# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: PiClient) -> None:
        message = client.model.sft.messages.stream(
            "job_id",
        )
        assert_matches_type(str, message, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: PiClient) -> None:
        response = client.model.sft.messages.with_raw_response.stream(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(str, message, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: PiClient) -> None:
        with client.model.sft.messages.with_streaming_response.stream(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(str, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.sft.messages.with_raw_response.stream(
                "",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncPiClient) -> None:
        message = await async_client.model.sft.messages.stream(
            "job_id",
        )
        assert_matches_type(str, message, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.messages.with_raw_response.stream(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(str, message, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.messages.with_streaming_response.stream(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(str, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.sft.messages.with_raw_response.stream(
                "",
            )
