# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import DataGenerationStatus, InputEvaluationMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @parametrize
    def test_method_generate(self, client: Twopir) -> None:
        input = client.data.inputs.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Twopir) -> None:
        input = client.data.inputs.get(
            0,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Twopir) -> None:
        response = client.data.inputs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Twopir) -> None:
        with client.data.inputs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @parametrize
    async def test_method_generate(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.generate(
            contract={
                "description": "description",
                "name": "name",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncTwopir) -> None:
        input = await async_client.data.inputs.get(
            0,
        )
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(DataGenerationStatus, input, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(DataGenerationStatus, input, path=["response"])

        assert cast(Any, response.is_closed) is True
