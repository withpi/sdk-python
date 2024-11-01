# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import ScoreBundle

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScorers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: Twopir) -> None:
        scorer = client.scorers.score(
            scorer_id=0,
            example={},
        )
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    def test_method_score_with_all_params(self, client: Twopir) -> None:
        scorer = client.scorers.score(
            scorer_id=0,
            example={
                "input": "Please help me with this problem.",
                "response": "I am happy to help you with that.",
            },
        )
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Twopir) -> None:
        response = client.scorers.with_raw_response.score(
            scorer_id=0,
            example={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Twopir) -> None:
        with client.scorers.with_streaming_response.score(
            scorer_id=0,
            example={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(ScoreBundle, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScorers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_score(self, async_client: AsyncTwopir) -> None:
        scorer = await async_client.scorers.score(
            scorer_id=0,
            example={},
        )
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncTwopir) -> None:
        scorer = await async_client.scorers.score(
            scorer_id=0,
            example={
                "input": "Please help me with this problem.",
                "response": "I am happy to help you with that.",
            },
        )
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncTwopir) -> None:
        response = await async_client.scorers.with_raw_response.score(
            scorer_id=0,
            example={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(ScoreBundle, scorer, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncTwopir) -> None:
        async with async_client.scorers.with_streaming_response.score(
            scorer_id=0,
            example={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(ScoreBundle, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True
