# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import DataGenerationStatus, InputEvaluationMetrics
from withpi.types.data import (
    InputClusterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cluster(self, client: PiClient) -> None:
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
    def test_raw_response_cluster(self, client: PiClient) -> None:
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
    def test_streaming_response_cluster(self, client: PiClient) -> None:
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
    def test_method_evaluate(self, client: PiClient) -> None:
        input = client.data.inputs.evaluate(
            contract_description="Write a haiku based on a topic description",
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: PiClient) -> None:
        response = client.data.inputs.with_raw_response.evaluate(
            contract_description="Write a haiku based on a topic description",
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
    def test_streaming_response_evaluate(self, client: PiClient) -> None:
        with client.data.inputs.with_streaming_response.evaluate(
            contract_description="Write a haiku based on a topic description",
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
    def test_method_generate_seeds(self, client: PiClient) -> None:
        input = client.data.inputs.generate_seeds(
            contract_description="Write a haiku based on a topic description",
            num_inputs=10,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_raw_response_generate_seeds(self, client: PiClient) -> None:
        response = client.data.inputs.with_raw_response.generate_seeds(
            contract_description="Write a haiku based on a topic description",
            num_inputs=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_streaming_response_generate_seeds(self, client: PiClient) -> None:
        with client.data.inputs.with_streaming_response.generate_seeds(
            contract_description="Write a haiku based on a topic description",
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
    async def test_method_cluster(self, async_client: AsyncPiClient) -> None:
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
    async def test_raw_response_cluster(self, async_client: AsyncPiClient) -> None:
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
    async def test_streaming_response_cluster(self, async_client: AsyncPiClient) -> None:
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
    async def test_method_evaluate(self, async_client: AsyncPiClient) -> None:
        input = await async_client.data.inputs.evaluate(
            contract_description="Write a haiku based on a topic description",
            llm_inputs=[
                "The quick brown fox jumped over the lazy dog",
                "The lazy dog was jumped over by the quick brown fox",
            ],
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.inputs.with_raw_response.evaluate(
            contract_description="Write a haiku based on a topic description",
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
    async def test_streaming_response_evaluate(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.inputs.with_streaming_response.evaluate(
            contract_description="Write a haiku based on a topic description",
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
    async def test_method_generate_seeds(self, async_client: AsyncPiClient) -> None:
        input = await async_client.data.inputs.generate_seeds(
            contract_description="Write a haiku based on a topic description",
            num_inputs=10,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_raw_response_generate_seeds(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.inputs.with_raw_response.generate_seeds(
            contract_description="Write a haiku based on a topic description",
            num_inputs=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_streaming_response_generate_seeds(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.inputs.with_streaming_response.generate_seeds(
            contract_description="Write a haiku based on a topic description",
            num_inputs=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True
