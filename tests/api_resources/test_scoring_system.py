# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import (
    ScoringSystemImportSpecResponse,
)
from withpi.types.shared import ScoringSystemMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoringSystem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_spec(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_spec_with_all_params(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
            source="HUGGINGFACE",
        )
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_spec(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_spec(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_score(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_score_with_all_params(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[
                {
                    "question": "Is this response truthful?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
                {
                    "question": "Is this response relevant?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
            ],
            aggregation_method="ARITHMETIC_MEAN",
            kwargs={"any_param": "any_value"},
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_score(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_score(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_to_huggingface(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_to_huggingface_with_all_params(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[
                {
                    "question": "Is this response truthful?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
                {
                    "question": "Is this response relevant?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
            ],
            hf_token="hf_token",
        )
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_to_huggingface(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_to_huggingface(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(str, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScoringSystem:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_spec(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_spec_with_all_params(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
            source="HUGGINGFACE",
        )
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_spec(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_spec(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(ScoringSystemImportSpecResponse, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_score(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[
                {
                    "question": "Is this response truthful?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
                {
                    "question": "Is this response relevant?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
            ],
            aggregation_method="ARITHMETIC_MEAN",
            kwargs={"any_param": "any_value"},
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_score(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_to_huggingface(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_to_huggingface_with_all_params(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[
                {
                    "question": "Is this response truthful?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
                {
                    "question": "Is this response relevant?",
                    "custom_model_id": "your-model-id",
                    "label": "Relevance to Prompt",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                },
            ],
            hf_token="hf_token",
        )
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_to_huggingface(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(str, scoring_system, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_to_huggingface(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.upload_to_huggingface(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            scoring_spec=[{"question": "Is this response truthful?"}, {"question": "Is this response relevant?"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(str, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True
