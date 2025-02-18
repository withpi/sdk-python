# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import RlGrpoStatus
from withpi.types.model.rl import GrpoCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGrpo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.retrieve(
            "job_id",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.model.rl.grpo.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = response.parse()
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.model.rl.grpo.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = response.parse()
            assert_matches_type(RlGrpoStatus, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.rl.grpo.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_check(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.check(
            "job_id",
        )
        assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: PiClient) -> None:
        response = client.model.rl.grpo.with_raw_response.check(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = response.parse()
        assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: PiClient) -> None:
        with client.model.rl.grpo.with_streaming_response.check(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = response.parse()
            assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_check(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.rl.grpo.with_raw_response.check(
                "",
            )

    @parametrize
    def test_method_load(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.load(
            "job_id",
        )
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    def test_raw_response_load(self, client: PiClient) -> None:
        response = client.model.rl.grpo.with_raw_response.load(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = response.parse()
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    def test_streaming_response_load(self, client: PiClient) -> None:
        with client.model.rl.grpo.with_streaming_response.load(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = response.parse()
            assert_matches_type(str, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_load(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.rl.grpo.with_raw_response.load(
                "",
            )

    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.start_job(
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
                                    "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                    "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
                                "custom_model_id": "your-model-id",
                                "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                "parameters": [
                                    0.14285714285714285,
                                    0.2857142857142857,
                                    0.42857142857142855,
                                    0.5714285714285714,
                                    0.7142857142857143,
                                    0.8571428571428571,
                                ],
                                "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "custom_model_id": "your-model-id",
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
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
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
            learning_rate=0.0002,
            num_train_epochs=10,
            system_prompt="system_prompt",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.model.rl.grpo.with_raw_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = response.parse()
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.model.rl.grpo.with_streaming_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = response.parse()
            assert_matches_type(RlGrpoStatus, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        grpo = client.model.rl.grpo.stream_messages(
            "job_id",
        )
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.model.rl.grpo.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = response.parse()
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.model.rl.grpo.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = response.parse()
            assert_matches_type(str, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.rl.grpo.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGrpo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.retrieve(
            "job_id",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = await response.parse()
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = await response.parse()
            assert_matches_type(RlGrpoStatus, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.rl.grpo.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_check(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.check(
            "job_id",
        )
        assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.with_raw_response.check(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = await response.parse()
        assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.with_streaming_response.check(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = await response.parse()
            assert_matches_type(GrpoCheckResponse, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_check(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.rl.grpo.with_raw_response.check(
                "",
            )

    @parametrize
    async def test_method_load(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.load(
            "job_id",
        )
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    async def test_raw_response_load(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.with_raw_response.load(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = await response.parse()
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    async def test_streaming_response_load(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.with_streaming_response.load(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = await response.parse()
            assert_matches_type(str, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_load(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.rl.grpo.with_raw_response.load(
                "",
            )

    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.start_job(
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
                                    "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                    "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
                                "custom_model_id": "your-model-id",
                                "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                "parameters": [
                                    0.14285714285714285,
                                    0.2857142857142857,
                                    0.42857142857142855,
                                    0.5714285714285714,
                                    0.7142857142857143,
                                    0.8571428571428571,
                                ],
                                "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "custom_model_id": "your-model-id",
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
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
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
            learning_rate=0.0002,
            num_train_epochs=10,
            system_prompt="system_prompt",
        )
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.with_raw_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = await response.parse()
        assert_matches_type(RlGrpoStatus, grpo, path=["response"])

    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.with_streaming_response.start_job(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            examples=[{"llm_input": "Tell me something different"}],
            model="LLAMA_3.2_1B",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = await response.parse()
            assert_matches_type(RlGrpoStatus, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        grpo = await async_client.model.rl.grpo.stream_messages(
            "job_id",
        )
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.rl.grpo.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grpo = await response.parse()
        assert_matches_type(str, grpo, path=["response"])

    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.rl.grpo.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grpo = await response.parse()
            assert_matches_type(str, grpo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.rl.grpo.with_raw_response.stream_messages(
                "",
            )
