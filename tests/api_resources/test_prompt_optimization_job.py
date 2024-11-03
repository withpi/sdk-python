# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import PromptOptimizationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptOptimizationJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Twopir) -> None:
        prompt_optimization_job = client.prompt_optimization_job.get(
            job_id=0,
            optimizer_id=0,
        )
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Twopir) -> None:
        response = client.prompt_optimization_job.with_raw_response.get(
            job_id=0,
            optimizer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization_job = response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Twopir) -> None:
        with client.prompt_optimization_job.with_streaming_response.get(
            job_id=0,
            optimizer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization_job = response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_optimize(self, client: Twopir) -> None:
        prompt_optimization_job = client.prompt_optimization_job.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        )
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    def test_raw_response_optimize(self, client: Twopir) -> None:
        response = client.prompt_optimization_job.with_raw_response.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization_job = response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    def test_streaming_response_optimize(self, client: Twopir) -> None:
        with client.prompt_optimization_job.with_streaming_response.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization_job = response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPromptOptimizationJob:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncTwopir) -> None:
        prompt_optimization_job = await async_client.prompt_optimization_job.get(
            job_id=0,
            optimizer_id=0,
        )
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTwopir) -> None:
        response = await async_client.prompt_optimization_job.with_raw_response.get(
            job_id=0,
            optimizer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization_job = await response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTwopir) -> None:
        async with async_client.prompt_optimization_job.with_streaming_response.get(
            job_id=0,
            optimizer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization_job = await response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_optimize(self, async_client: AsyncTwopir) -> None:
        prompt_optimization_job = await async_client.prompt_optimization_job.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        )
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    async def test_raw_response_optimize(self, async_client: AsyncTwopir) -> None:
        response = await async_client.prompt_optimization_job.with_raw_response.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization_job = await response.parse()
        assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

    @parametrize
    async def test_streaming_response_optimize(self, async_client: AsyncTwopir) -> None:
        async with async_client.prompt_optimization_job.with_streaming_response.optimize(
            optimizer_id=0,
            contract={
                "description": "You are a helpful AI assistant",
                "dimensions": [
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                    {
                        "description": "Test whether the LLM follows instructions.",
                        "label": "Instruction Following",
                    },
                ],
                "name": "My application",
            },
            experiment_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization_job = await response.parse()
            assert_matches_type(PromptOptimizationStatus, prompt_optimization_job, path=["response"])

        assert cast(Any, response.is_closed) is True
