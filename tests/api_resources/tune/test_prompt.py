# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import OptimizationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Twopir) -> None:
        prompt = client.tune.prompt.get(
            "job_id",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Twopir) -> None:
        response = client.tune.prompt.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Twopir) -> None:
        with client.tune.prompt.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(OptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Twopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.tune.prompt.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_optimize(self, client: Twopir) -> None:
        prompt = client.tune.prompt.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_method_optimize_with_all_params(self, client: Twopir) -> None:
        prompt = client.tune.prompt.optimize(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                ],
                "scorer_ast": "string",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_raw_response_optimize(self, client: Twopir) -> None:
        response = client.tune.prompt.with_raw_response.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    def test_streaming_response_optimize(self, client: Twopir) -> None:
        with client.tune.prompt.with_streaming_response.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(OptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompt:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncTwopir) -> None:
        prompt = await async_client.tune.prompt.get(
            "job_id",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTwopir) -> None:
        response = await async_client.tune.prompt.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTwopir) -> None:
        async with async_client.tune.prompt.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(OptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTwopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.tune.prompt.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_optimize(self, async_client: AsyncTwopir) -> None:
        prompt = await async_client.tune.prompt.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_method_optimize_with_all_params(self, async_client: AsyncTwopir) -> None:
        prompt = await async_client.tune.prompt.optimize(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                    {
                        "id": "id",
                        "description": "description",
                        "sub_dimensions": [
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                            {
                                "id": "id",
                                "description": "description",
                            },
                        ],
                    },
                ],
                "scorer_ast": "string",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_raw_response_optimize(self, async_client: AsyncTwopir) -> None:
        response = await async_client.tune.prompt.with_raw_response.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(OptimizationStatus, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_optimize(self, async_client: AsyncTwopir) -> None:
        async with async_client.tune.prompt.with_streaming_response.optimize(
            contract={
                "description": "description",
                "name": "name",
            },
            examples=[
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
                {
                    "llm_input": "string",
                    "llm_output": "llm_output",
                },
            ],
            model_id="gpt-4o-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(OptimizationStatus, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
