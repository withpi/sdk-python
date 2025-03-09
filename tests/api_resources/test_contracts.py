# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import (
    ContractScoreResponse,
)
from withpi.types.shared import Contract

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_dimensions(self, client: PiClient) -> None:
        contract = client.contracts.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_method_generate_dimensions_with_all_params(self, client: PiClient) -> None:
        contract = client.contracts.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
            try_auto_generating_python_code=False,
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_raw_response_generate_dimensions(self, client: PiClient) -> None:
        response = client.contracts.with_raw_response.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_streaming_response_generate_dimensions(self, client: PiClient) -> None:
        with client.contracts.with_streaming_response.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read_from_hf(self, client: PiClient) -> None:
        contract = client.contracts.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_method_read_from_hf_with_all_params(self, client: PiClient) -> None:
        contract = client.contracts.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_raw_response_read_from_hf(self, client: PiClient) -> None:
        response = client.contracts.with_raw_response.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_streaming_response_read_from_hf(self, client: PiClient) -> None:
        with client.contracts.with_streaming_response.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_score(self, client: PiClient) -> None:
        contract = client.contracts.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        )
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    def test_method_score_with_all_params(self, client: PiClient) -> None:
        contract = client.contracts.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
                "dimensions": [
                    {
                        "description": "Relevance of the response",
                        "label": "Relevance",
                        "sub_dimensions": [
                            {
                                "description": "Is the response relevant to the prompt?",
                                "label": "Relevance to Prompt",
                                "scoring_type": "PI_SCORER",
                                "custom_model_id": "your-model-id",
                                "parameters": [
                                    0.14285714285714285,
                                    0.2857142857142857,
                                    0.42857142857142855,
                                    0.5714285714285714,
                                    0.7142857142857143,
                                    0.8571428571428571,
                                ],
                                "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "parameters": [
                            0.14285714285714285,
                            0.2857142857142857,
                            0.42857142857142855,
                            0.5714285714285714,
                            0.7142857142857143,
                            0.8571428571428571,
                        ],
                        "weight": 1,
                    }
                ],
            },
        )
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: PiClient) -> None:
        response = client.contracts.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: PiClient) -> None:
        with client.contracts.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractScoreResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate_dimensions(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_method_generate_dimensions_with_all_params(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
            try_auto_generating_python_code=False,
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_raw_response_generate_dimensions(self, async_client: AsyncPiClient) -> None:
        response = await async_client.contracts.with_raw_response.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_streaming_response_generate_dimensions(self, async_client: AsyncPiClient) -> None:
        async with async_client.contracts.with_streaming_response.generate_dimensions(
            application_description="Write a children's story communicating a simple life lesson.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read_from_hf(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_method_read_from_hf_with_all_params(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_raw_response_read_from_hf(self, async_client: AsyncPiClient) -> None:
        response = await async_client.contracts.with_raw_response.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_streaming_response_read_from_hf(self, async_client: AsyncPiClient) -> None:
        async with async_client.contracts.with_streaming_response.read_from_hf(
            hf_scoring_system_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_score(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        )
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncPiClient) -> None:
        contract = await async_client.contracts.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
                "dimensions": [
                    {
                        "description": "Relevance of the response",
                        "label": "Relevance",
                        "sub_dimensions": [
                            {
                                "description": "Is the response relevant to the prompt?",
                                "label": "Relevance to Prompt",
                                "scoring_type": "PI_SCORER",
                                "custom_model_id": "your-model-id",
                                "parameters": [
                                    0.14285714285714285,
                                    0.2857142857142857,
                                    0.42857142857142855,
                                    0.5714285714285714,
                                    0.7142857142857143,
                                    0.8571428571428571,
                                ],
                                "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "parameters": [
                            0.14285714285714285,
                            0.2857142857142857,
                            0.42857142857142855,
                            0.5714285714285714,
                            0.7142857142857143,
                            0.8571428571428571,
                        ],
                        "weight": 1,
                    }
                ],
            },
        )
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncPiClient) -> None:
        response = await async_client.contracts.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractScoreResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncPiClient) -> None:
        async with async_client.contracts.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_system={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractScoreResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
