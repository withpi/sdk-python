# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import InputEvaluationMetrics
from twopir.types.data import InputClusterResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cluster(self, client: Twopir) -> None:
        input = client.data.inputs.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "string",
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
                    "llm_input": "string",
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
                    "llm_input": "string",
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
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: Twopir) -> None:
        input = client.data.inputs.evaluate(
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
                                "parameters": [0],
                                "scoring_method": "twopir_judge",
                                "scoring_type": "llm_as_a_judge",
                                "weight": 0,
                            }
                        ],
                        "weight": 0,
                    }
                ],
            },
            llm_input="string",
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.evaluate(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.evaluate(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(InputEvaluationMetrics, input, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cluster(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.cluster(
            inputs=[
                {
                    "identifier": "identifier",
                    "llm_input": "string",
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
                    "llm_input": "string",
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
                    "llm_input": "string",
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
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.evaluate(
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
                                "parameters": [0],
                                "scoring_method": "twopir_judge",
                                "scoring_type": "llm_as_a_judge",
                                "weight": 0,
                            }
                        ],
                        "weight": 0,
                    }
                ],
            },
            llm_input="string",
        )
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.evaluate(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(InputEvaluationMetrics, input, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.evaluate(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(InputEvaluationMetrics, input, path=["response"])

        assert cast(Any, response.is_closed) is True
