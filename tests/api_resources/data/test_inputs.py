# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import DataGenerationStatus, InputEvaluationMetrics
from twopir.types.data import (
    InputClusterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cluster(self, client: Twopir) -> None:
        input = client.data.inputs.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        )
        assert_matches_type(InputClusterResponse, input, path=["response"])

    @parametrize
    def test_raw_response_cluster(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(InputClusterResponse, input, path=["response"])

    @parametrize
    def test_streaming_response_cluster(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(InputClusterResponse, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_evaluate(self, client: Twopir) -> None:
        input = client.data.inputs.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: Twopir) -> None:
        input = client.data.inputs.evaluate(
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
                                "action_dimension": None,
                                "action_on_low_score": True,
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
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                            "weight": 1,
                        },
                        "action_on_low_score": True,
                        "weight": 1,
                    }
                ],
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(InputEvaluationMetrics, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_seeds(self, client: Twopir) -> None:
        input = client.data.inputs.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_method_generate_seeds_with_all_params(self, client: Twopir) -> None:
        input = client.data.inputs.generate_seeds(
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
                                "action_dimension": None,
                                "action_on_low_score": True,
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
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                            "weight": 1,
                        },
                        "action_on_low_score": True,
                        "weight": 1,
                    }
                ],
            },
            num_inputs=10,
            context_types=["none"],
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_raw_response_generate_seeds(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_streaming_response_generate_seeds(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cluster(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        )
        assert_matches_type(InputClusterResponse, input, path=["response"])

    @parametrize
    async def test_raw_response_cluster(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(InputClusterResponse, input, path=["response"])

    @parametrize
    async def test_streaming_response_cluster(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "Tell me something different",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(InputClusterResponse, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.evaluate(
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
                                "action_dimension": None,
                                "action_on_low_score": True,
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
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                            "weight": 1,
                        },
                        "action_on_low_score": True,
                        "weight": 1,
                    }
                ],
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.evaluate(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(InputEvaluationMetrics, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_seeds(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_method_generate_seeds_with_all_params(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.generate_seeds(
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
                                "action_dimension": None,
                                "action_on_low_score": True,
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
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "https://yourmodelid.us-east-1.aws.endpoints.huggingface.cloud",
                            "parameters": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
                            "python_code": '\ndef score(response_text, input_text, input_args, kwargs):\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                            "weight": 1,
                        },
                        "action_on_low_score": True,
                        "weight": 1,
                    }
                ],
            },
            num_inputs=10,
            context_types=["none"],
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_raw_response_generate_seeds(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_streaming_response_generate_seeds(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.generate_seeds(
            contract={
                "description": "Write a children's story communicating a simple life lesson.",
                "name": "Sample Contract",
            },
            num_inputs=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True
