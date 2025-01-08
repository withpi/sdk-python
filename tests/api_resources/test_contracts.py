# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import ContractsScoreMetrics
from twopir.types.shared import Contract

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_dimensions(self, client: Twopir) -> None:
        contract = client.contracts.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_method_generate_dimensions_with_all_params(self, client: Twopir) -> None:
        contract = client.contracts.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                        "sub_dimensions": [
                            {
                                "description": "description",
                                "label": "label",
                                "scoring_type": "PI_SCORER",
                                "action_dimension": None,
                                "action_on_low_score": True,
                                "huggingface_url": "huggingface_url",
                                "parameters": [0],
                                "python_code": "python_code",
                                "weight": 0,
                            }
                        ],
                        "action_dimension": {
                            "description": "description",
                            "label": "label",
                            "scoring_type": "PI_SCORER",
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "huggingface_url",
                            "parameters": [0],
                            "python_code": "python_code",
                            "weight": 0,
                        },
                        "action_on_low_score": True,
                        "weight": 0,
                    }
                ],
            },
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_raw_response_generate_dimensions(self, client: Twopir) -> None:
        response = client.contracts.with_raw_response.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_streaming_response_generate_dimensions(self, client: Twopir) -> None:
        with client.contracts.with_streaming_response.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_score(self, client: Twopir) -> None:
        contract = client.contracts.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    def test_method_score_with_all_params(self, client: Twopir) -> None:
        contract = client.contracts.score(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                        "sub_dimensions": [
                            {
                                "description": "description",
                                "label": "label",
                                "scoring_type": "PI_SCORER",
                                "action_dimension": None,
                                "action_on_low_score": True,
                                "huggingface_url": "huggingface_url",
                                "parameters": [0],
                                "python_code": "python_code",
                                "weight": 0,
                            }
                        ],
                        "action_dimension": {
                            "description": "description",
                            "label": "label",
                            "scoring_type": "PI_SCORER",
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "huggingface_url",
                            "parameters": [0],
                            "python_code": "python_code",
                            "weight": 0,
                        },
                        "action_on_low_score": True,
                        "weight": 0,
                    }
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Twopir) -> None:
        response = client.contracts.with_raw_response.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Twopir) -> None:
        with client.contracts.with_streaming_response.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contracts.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_method_generate_dimensions_with_all_params(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contracts.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                        "sub_dimensions": [
                            {
                                "description": "description",
                                "label": "label",
                                "scoring_type": "PI_SCORER",
                                "action_dimension": None,
                                "action_on_low_score": True,
                                "huggingface_url": "huggingface_url",
                                "parameters": [0],
                                "python_code": "python_code",
                                "weight": 0,
                            }
                        ],
                        "action_dimension": {
                            "description": "description",
                            "label": "label",
                            "scoring_type": "PI_SCORER",
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "huggingface_url",
                            "parameters": [0],
                            "python_code": "python_code",
                            "weight": 0,
                        },
                        "action_on_low_score": True,
                        "weight": 0,
                    }
                ],
            },
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_raw_response_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contracts.with_raw_response.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_streaming_response_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        async with async_client.contracts.with_streaming_response.generate_dimensions(
            contract={
                "description": "description",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_score(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contracts.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contracts.score(
            contract={
                "description": "description",
                "name": "name",
                "dimensions": [
                    {
                        "description": "description",
                        "label": "label",
                        "sub_dimensions": [
                            {
                                "description": "description",
                                "label": "label",
                                "scoring_type": "PI_SCORER",
                                "action_dimension": None,
                                "action_on_low_score": True,
                                "huggingface_url": "huggingface_url",
                                "parameters": [0],
                                "python_code": "python_code",
                                "weight": 0,
                            }
                        ],
                        "action_dimension": {
                            "description": "description",
                            "label": "label",
                            "scoring_type": "PI_SCORER",
                            "action_dimension": None,
                            "action_on_low_score": True,
                            "huggingface_url": "huggingface_url",
                            "parameters": [0],
                            "python_code": "python_code",
                            "weight": 0,
                        },
                        "action_on_low_score": True,
                        "weight": 0,
                    }
                ],
            },
            llm_input="string",
            llm_output="llm_output",
        )
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contracts.with_raw_response.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncTwopir) -> None:
        async with async_client.contracts.with_streaming_response.score(
            contract={
                "description": "description",
                "name": "name",
            },
            llm_input="string",
            llm_output="llm_output",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractsScoreMetrics, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
