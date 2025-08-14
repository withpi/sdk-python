# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.search import QueryClassifierClassifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueryClassifier:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify(self, client: PiClient) -> None:
        query_classifier = client.search.query_classifier.classify(
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
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify_with_all_params(self, client: PiClient) -> None:
        query_classifier = client.search.query_classifier.classify(
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
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_classify(self, client: PiClient) -> None:
        response = client.search.query_classifier.with_raw_response.classify(
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
        query_classifier = response.parse()
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_classify(self, client: PiClient) -> None:
        with client.search.query_classifier.with_streaming_response.classify(
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

            query_classifier = response.parse()
            assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueryClassifier:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify(self, async_client: AsyncPiClient) -> None:
        query_classifier = await async_client.search.query_classifier.classify(
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
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncPiClient) -> None:
        query_classifier = await async_client.search.query_classifier.classify(
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
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.with_raw_response.classify(
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
        query_classifier = await response.parse()
        assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.with_streaming_response.classify(
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

            query_classifier = await response.parse()
            assert_matches_type(QueryClassifierClassifyResponse, query_classifier, path=["response"])

        assert cast(Any, response.is_closed) is True
