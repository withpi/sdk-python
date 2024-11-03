# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import ResponseMetric

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScorer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: Twopir) -> None:
        scorer = client.scorer.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )
        assert_matches_type(ResponseMetric, scorer, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Twopir) -> None:
        response = client.scorer.with_raw_response.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(ResponseMetric, scorer, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Twopir) -> None:
        with client.scorer.with_streaming_response.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(ResponseMetric, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScorer:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_score(self, async_client: AsyncTwopir) -> None:
        scorer = await async_client.scorer.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )
        assert_matches_type(ResponseMetric, scorer, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncTwopir) -> None:
        response = await async_client.scorer.with_raw_response.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(ResponseMetric, scorer, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncTwopir) -> None:
        async with async_client.scorer.with_streaming_response.score(
            scorer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(ResponseMetric, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True
