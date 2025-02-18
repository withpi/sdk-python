# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        chat_completion = client.model.rl.grpo.chat_completions.list(
            "job_id",
        )
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.model.rl.grpo.chat_completions.with_raw_response.list(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.model.rl.grpo.chat_completions.with_streaming_response.list(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.rl.grpo.chat_completions.with_raw_response.list(
                "",
            )


class TestAsyncChatCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        chat_completion = await async_client.model.rl.grpo.chat_completions.list(
            "job_id",
        )
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.chat_completions.with_raw_response.list(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = await response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.chat_completions.with_streaming_response.list(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = await response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.rl.grpo.chat_completions.with_raw_response.list(
                "",
            )
