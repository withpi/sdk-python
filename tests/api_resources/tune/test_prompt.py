# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import PromptOptimizationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_detailed_messages(self, client: PiClient) -> None:
        prompt = client.tune.prompt.get_detailed_messages(
            "job_id",
        )
        assert_matches_type(str, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_detailed_messages(self, client: PiClient) -> None:
        response = client.tune.prompt.with_raw_response.get_detailed_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(str, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_detailed_messages(self, client: PiClient) -> None:
        with client.tune.prompt.with_streaming_response.get_detailed_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(str, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_detailed_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.tune.prompt.with_raw_response.get_detailed_messages(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: PiClient) -> None:
        prompt = client.tune.prompt.get_status(
            "job_id",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: PiClient) -> None:
        response = client.tune.prompt.with_raw_response.get_status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: PiClient) -> None:
        with client.tune.prompt.with_streaming_response.get_status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.tune.prompt.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_optimize(self, client: PiClient) -> None:
        prompt = client.tune.prompt.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_method_optimize_with_all_params(self, client: PiClient) -> None:
        prompt = client.tune.prompt.optimize(
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
                                    "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                    "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
                                "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                                "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                        },
                        "weight": 1,
                    }
                ],
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_raw_response_optimize(self, client: PiClient) -> None:
        response = client.tune.prompt.with_raw_response.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_streaming_response_optimize(self, client: PiClient) -> None:
        with client.tune.prompt.with_streaming_response.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompt:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_detailed_messages(self, async_client: AsyncPiClient) -> None:
        prompt = await async_client.tune.prompt.get_detailed_messages(
            "job_id",
        )
        assert_matches_type(str, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_detailed_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.tune.prompt.with_raw_response.get_detailed_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(str, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_detailed_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.tune.prompt.with_streaming_response.get_detailed_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(str, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_detailed_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.tune.prompt.with_raw_response.get_detailed_messages(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncPiClient) -> None:
        prompt = await async_client.tune.prompt.get_status(
            "job_id",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncPiClient) -> None:
        response = await async_client.tune.prompt.with_raw_response.get_status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncPiClient) -> None:
        async with async_client.tune.prompt.with_streaming_response.get_status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.tune.prompt.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_optimize(self, async_client: AsyncPiClient) -> None:
        prompt = await async_client.tune.prompt.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_method_optimize_with_all_params(self, async_client: AsyncPiClient) -> None:
        prompt = await async_client.tune.prompt.optimize(
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
                                    "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                    "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                },
                                "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                                "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                                "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                                "weight": 1,
                            }
                        ],
                        "action_dimension": {
                            "description": "Is the response relevant to the prompt?",
                            "label": "Relevance to Prompt",
                            "scoring_type": "PI_SCORER",
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                        },
                        "weight": 1,
                    }
                ],
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_raw_response_optimize(self, async_client: AsyncPiClient) -> None:
        response = await async_client.tune.prompt.with_raw_response.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_optimize(self, async_client: AsyncPiClient) -> None:
        async with async_client.tune.prompt.with_streaming_response.optimize(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            tuning_algorithm="PI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
