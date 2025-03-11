# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.prompt import (
    OptimizeListResponse,
)
from withpi.types.shared import PromptOptimizationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptimize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.retrieve(
            "job_id",
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.prompt.optimize.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.prompt.optimize.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.prompt.optimize.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.list()
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.list(
            state="QUEUED",
        )
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.prompt.optimize.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.prompt.optimize.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(OptimizeListResponse, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.cancel(
            "job_id",
        )
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.prompt.optimize.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.prompt.optimize.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(str, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.prompt.optimize.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
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
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            use_chain_of_thought=False,
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.prompt.optimize.with_raw_response.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.prompt.optimize.with_streaming_response.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        optimize = client.prompt.optimize.stream_messages(
            "job_id",
        )
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.prompt.optimize.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.prompt.optimize.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(str, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.prompt.optimize.with_raw_response.stream_messages(
                "",
            )


class TestAsyncOptimize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.retrieve(
            "job_id",
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.prompt.optimize.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.prompt.optimize.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.prompt.optimize.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.list()
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.list(
            state="QUEUED",
        )
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.prompt.optimize.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(OptimizeListResponse, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.prompt.optimize.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(OptimizeListResponse, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.cancel(
            "job_id",
        )
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.prompt.optimize.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.prompt.optimize.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(str, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.prompt.optimize.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
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
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
            dspy_optimization_type="BOOTSTRAP_FEW_SHOT",
            use_chain_of_thought=False,
        )
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.prompt.optimize.with_raw_response.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.prompt.optimize.with_streaming_response.start_job(
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            initial_system_instruction="Write a great story around the given topic.",
            model_id="gpt-4o-mini",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
            tuning_algorithm="DSPY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(PromptOptimizationStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        optimize = await async_client.prompt.optimize.stream_messages(
            "job_id",
        )
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.prompt.optimize.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(str, optimize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.prompt.optimize.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(str, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.prompt.optimize.with_raw_response.stream_messages(
                "",
            )
