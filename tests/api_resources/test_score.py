# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import ScoreBundle

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Twopir) -> None:
        score = client.score.execute(
            scorer_id="scorer_id",
        )
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Twopir) -> None:
        score = client.score.execute(
            scorer_id="scorer_id",
            input="Please help me with this problem.",
            response="I am happy to help you with that.",
        )
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Twopir) -> None:
        response = client.score.with_raw_response.execute(
            scorer_id="scorer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Twopir) -> None:
        with client.score.with_streaming_response.execute(
            scorer_id="scorer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(ScoreBundle, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Twopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scorer_id` but received ''"):
            client.score.with_raw_response.execute(
                scorer_id="",
            )


class TestAsyncScore:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncTwopir) -> None:
        score = await async_client.score.execute(
            scorer_id="scorer_id",
        )
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncTwopir) -> None:
        score = await async_client.score.execute(
            scorer_id="scorer_id",
            input="Please help me with this problem.",
            response="I am happy to help you with that.",
        )
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncTwopir) -> None:
        response = await async_client.score.with_raw_response.execute(
            scorer_id="scorer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(ScoreBundle, score, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncTwopir) -> None:
        async with async_client.score.with_streaming_response.execute(
            scorer_id="scorer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(ScoreBundle, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncTwopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scorer_id` but received ''"):
            await async_client.score.with_raw_response.execute(
                scorer_id="",
            )
