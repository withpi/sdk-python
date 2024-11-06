# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types.shared import Contract, ResponseMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_calibrate(self, client: Twopir) -> None:
        contract = client.contract.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_raw_response_calibrate(self, client: Twopir) -> None:
        response = client.contract.with_raw_response.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_streaming_response_calibrate(self, client: Twopir) -> None:
        with client.contract.with_streaming_response.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_dimensions(self, client: Twopir) -> None:
        contract = client.contract.generate_dimensions(
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
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_raw_response_generate_dimensions(self, client: Twopir) -> None:
        response = client.contract.with_raw_response.generate_dimensions(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    def test_streaming_response_generate_dimensions(self, client: Twopir) -> None:
        with client.contract.with_streaming_response.generate_dimensions(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_score(self, client: Twopir) -> None:
        contract = client.contract.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )
        assert_matches_type(ResponseMetrics, contract, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Twopir) -> None:
        response = client.contract.with_raw_response.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ResponseMetrics, contract, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Twopir) -> None:
        with client.contract.with_streaming_response.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ResponseMetrics, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContract:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_calibrate(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contract.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_raw_response_calibrate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contract.with_raw_response.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_streaming_response_calibrate(self, async_client: AsyncTwopir) -> None:
        async with async_client.contract.with_streaming_response.calibrate(
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
            feedbacks=[
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
                {
                    "labels": {"foo": 0},
                    "llm_input": {"query": "Help me with my problem"},
                    "llm_response": {"text": "I am happy to help you with that."},
                    "scores": {"foo": 0},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contract.generate_dimensions(
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
        )
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_raw_response_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contract.with_raw_response.generate_dimensions(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(Contract, contract, path=["response"])

    @parametrize
    async def test_streaming_response_generate_dimensions(self, async_client: AsyncTwopir) -> None:
        async with async_client.contract.with_streaming_response.generate_dimensions(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(Contract, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_score(self, async_client: AsyncTwopir) -> None:
        contract = await async_client.contract.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )
        assert_matches_type(ResponseMetrics, contract, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncTwopir) -> None:
        response = await async_client.contract.with_raw_response.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ResponseMetrics, contract, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncTwopir) -> None:
        async with async_client.contract.with_streaming_response.score(
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
            llm_input={"query": "Help me with my problem"},
            llm_response={"text": "I am happy to help you with that."},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ResponseMetrics, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
