# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import FeedbackClusterResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cluster(self, client: Twopir) -> None:
        feedback = client.feedback.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        )
        assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_cluster(self, client: Twopir) -> None:
        response = client.feedback.with_raw_response.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_cluster(self, client: Twopir) -> None:
        with client.feedback.with_streaming_response.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cluster(self, async_client: AsyncTwopir) -> None:
        feedback = await async_client.feedback.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        )
        assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_cluster(self, async_client: AsyncTwopir) -> None:
        response = await async_client.feedback.with_raw_response.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_cluster(self, async_client: AsyncTwopir) -> None:
        async with async_client.feedback.with_streaming_response.cluster(
            feedbacks=[
                {
                    "comment": "comment",
                    "identifier": "identifier",
                    "llm_input": "string",
                    "llm_output": "llm_output",
                    "rating": "positive",
                    "source": "internal",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackClusterResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
