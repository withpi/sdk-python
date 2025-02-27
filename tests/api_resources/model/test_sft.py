# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.model import (
    SftStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        sft = client.model.sft.retrieve(
            "job_id",
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.model.sft.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.model.sft.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.sft.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_download(self, client: PiClient) -> None:
        sft = client.model.sft.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: PiClient) -> None:
        response = client.model.sft.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = response.parse()
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: PiClient) -> None:
        with client.model.sft.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = response.parse()
            assert_matches_type(str, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.sft.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @parametrize
    def test_method_load(self, client: PiClient) -> None:
        sft = client.model.sft.load(
            "job_id",
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_raw_response_load(self, client: PiClient) -> None:
        response = client.model.sft.with_raw_response.load(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_streaming_response_load(self, client: PiClient) -> None:
        with client.model.sft.with_streaming_response.load(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_load(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.sft.with_raw_response.load(
                "",
            )

    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        sft = client.model.sft.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        sft = client.model.sft.start_job(
            contract={
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
                                "action_dimension": {
                                    "description": "Is the response relevant to the prompt?",
                                    "label": "Relevance to Prompt",
                                    "scoring_type": "PI_SCORER",
                                    "action_on_low_score": True,
                                    "custom_model_id": "your-model-id",
                                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
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
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "custom_model_id": "your-model-id",
                            "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                        },
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
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            base_sft_model="LLAMA_3.2_3B",
            learning_rate=0.0002,
            lora_config={"lora_rank": "R_16"},
            num_train_epochs=10,
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.model.sft.with_raw_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.model.sft.with_streaming_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        sft = client.model.sft.stream_messages(
            "job_id",
        )
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.model.sft.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = response.parse()
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.model.sft.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = response.parse()
            assert_matches_type(str, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.sft.with_raw_response.stream_messages(
                "",
            )


class TestAsyncSft:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.retrieve(
            "job_id",
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = await response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = await response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.sft.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_download(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = await response.parse()
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = await response.parse()
            assert_matches_type(str, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.sft.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @parametrize
    async def test_method_load(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.load(
            "job_id",
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_raw_response_load(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.with_raw_response.load(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = await response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_streaming_response_load(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.with_streaming_response.load(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = await response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_load(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.sft.with_raw_response.load(
                "",
            )

    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.start_job(
            contract={
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
                                "action_dimension": {
                                    "description": "Is the response relevant to the prompt?",
                                    "label": "Relevance to Prompt",
                                    "scoring_type": "PI_SCORER",
                                    "action_on_low_score": True,
                                    "custom_model_id": "your-model-id",
                                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
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
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "custom_model_id": "your-model-id",
                            "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                        },
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
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            base_sft_model="LLAMA_3.2_3B",
            learning_rate=0.0002,
            lora_config={"lora_rank": "R_16"},
            num_train_epochs=10,
        )
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.with_raw_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = await response.parse()
        assert_matches_type(SftStatus, sft, path=["response"])

    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.with_streaming_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = await response.parse()
            assert_matches_type(SftStatus, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        sft = await async_client.model.sft.stream_messages(
            "job_id",
        )
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.sft.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sft = await response.parse()
        assert_matches_type(str, sft, path=["response"])

    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.sft.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sft = await response.parse()
            assert_matches_type(str, sft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.sft.with_raw_response.stream_messages(
                "",
            )
