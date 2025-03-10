# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import (
    QueryClassifyResponse,
    QueryGenerateFanoutsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify(self, client: PiClient) -> None:
        query = client.queries.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        )
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_with_all_params(self, client: PiClient) -> None:
        query = client.queries.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
            batch_size=10,
            examples=[
                {
                    "label": "factual",
                    "text": "When was the Eiffel Tower built?",
                },
                {
                    "label": "opinion",
                    "text": "Is jazz better than classical music?",
                },
                {
                    "label": "procedural",
                    "text": "How do I change a flat tire?",
                },
            ],
            mode="generative",
        )
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify(self, client: PiClient) -> None:
        response = client.queries.with_raw_response.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify(self, client: PiClient) -> None:
        with client.queries.with_streaming_response.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryClassifyResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_fanouts(self, client: PiClient) -> None:
        query = client.queries.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        )
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_fanouts_with_all_params(self, client: PiClient) -> None:
        query = client.queries.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
            example_fanout_queries=[
                {
                    "fanout_queries": [
                        "Genus of the cheetah",
                        "Genus of the pronghorn",
                        "Genus of the springbok",
                        "Genus of the wildebeest",
                        "Genus of the lion",
                    ],
                    "query": "What are the genera of the five fastest land animals?",
                }
            ],
            num_fanout_queries=5,
        )
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_fanouts(self, client: PiClient) -> None:
        response = client.queries.with_raw_response.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_fanouts(self, client: PiClient) -> None:
        with client.queries.with_streaming_response.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify(self, async_client: AsyncPiClient) -> None:
        query = await async_client.queries.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        )
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncPiClient) -> None:
        query = await async_client.queries.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
            batch_size=10,
            examples=[
                {
                    "label": "factual",
                    "text": "When was the Eiffel Tower built?",
                },
                {
                    "label": "opinion",
                    "text": "Is jazz better than classical music?",
                },
                {
                    "label": "procedural",
                    "text": "How do I change a flat tire?",
                },
            ],
            mode="generative",
        )
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncPiClient) -> None:
        response = await async_client.queries.with_raw_response.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryClassifyResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncPiClient) -> None:
        async with async_client.queries.with_streaming_response.classify(
            classes=[
                {
                    "description": "Questions seeking objective, verifiable information or facts",
                    "label": "factual",
                },
                {
                    "description": "Questions asking for subjective judgments, preferences, or personal views",
                    "label": "opinion",
                },
                {
                    "description": "Questions about how to perform tasks or follow specific processes",
                    "label": "procedural",
                },
            ],
            queries=[
                "What is the capital of France?",
                "How do I feel about the current political climate?",
                "What steps should I follow to bake a chocolate cake?",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryClassifyResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_fanouts(self, async_client: AsyncPiClient) -> None:
        query = await async_client.queries.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        )
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_fanouts_with_all_params(self, async_client: AsyncPiClient) -> None:
        query = await async_client.queries.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
            example_fanout_queries=[
                {
                    "fanout_queries": [
                        "Genus of the cheetah",
                        "Genus of the pronghorn",
                        "Genus of the springbok",
                        "Genus of the wildebeest",
                        "Genus of the lion",
                    ],
                    "query": "What are the genera of the five fastest land animals?",
                }
            ],
            num_fanout_queries=5,
        )
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_fanouts(self, async_client: AsyncPiClient) -> None:
        response = await async_client.queries.with_raw_response.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_fanouts(self, async_client: AsyncPiClient) -> None:
        async with async_client.queries.with_streaming_response.generate_fanouts(
            queries=[
                "Name the four largest fish and what they eat.",
                "What was the profession of both Ellery Queen and John Fowles?",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryGenerateFanoutsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True
