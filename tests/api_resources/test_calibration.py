# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types import CalibrationResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalibration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_calibrate(self, client: Twopir) -> None:
        calibration = client.calibration.calibrate(
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
        assert_matches_type(CalibrationResult, calibration, path=["response"])

    @parametrize
    def test_raw_response_calibrate(self, client: Twopir) -> None:
        response = client.calibration.with_raw_response.calibrate(
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
        calibration = response.parse()
        assert_matches_type(CalibrationResult, calibration, path=["response"])

    @parametrize
    def test_streaming_response_calibrate(self, client: Twopir) -> None:
        with client.calibration.with_streaming_response.calibrate(
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

            calibration = response.parse()
            assert_matches_type(CalibrationResult, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalibration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_calibrate(self, async_client: AsyncTwopir) -> None:
        calibration = await async_client.calibration.calibrate(
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
        assert_matches_type(CalibrationResult, calibration, path=["response"])

    @parametrize
    async def test_raw_response_calibrate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.calibration.with_raw_response.calibrate(
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
        calibration = await response.parse()
        assert_matches_type(CalibrationResult, calibration, path=["response"])

    @parametrize
    async def test_streaming_response_calibrate(self, async_client: AsyncTwopir) -> None:
        async with async_client.calibration.with_streaming_response.calibrate(
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

            calibration = await response.parse()
            assert_matches_type(CalibrationResult, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True
