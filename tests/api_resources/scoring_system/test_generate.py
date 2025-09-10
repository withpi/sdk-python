# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.scoring_system import (
    GenerateListResponse,
    GenerateRetrieveResponse,
    GenerateStartJobResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.retrieve(
            "job_id",
        )
        assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.scoring_system.generate.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.scoring_system.generate.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.scoring_system.generate.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.list()
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.scoring_system.generate.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.scoring_system.generate.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateListResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.cancel(
            "job_id",
        )
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.scoring_system.generate.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.scoring_system.generate.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(str, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.scoring_system.generate.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        )
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                    "rating": "Disagree",
                    "score": 0.9,
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                    "rating": "Disagree",
                    "score": 0.5,
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
            batch_size=0,
            existing_questions=[
                {
                    "question": "Is the output relevant to input?",
                    "custom_model_id": "your-model-id",
                    "label": "some input",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                }
            ],
            num_questions=0,
            retain_existing_questions=False,
            try_auto_generating_python_code=False,
        )
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.scoring_system.generate.with_raw_response.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.scoring_system.generate.with_streaming_response.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        generate = client.scoring_system.generate.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.scoring_system.generate.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.scoring_system.generate.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(str, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.scoring_system.generate.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.retrieve(
            "job_id",
        )
        assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.generate.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.generate.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateRetrieveResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.scoring_system.generate.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.list()
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.generate.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateListResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.generate.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateListResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.cancel(
            "job_id",
        )
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.generate.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.generate.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(str, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.scoring_system.generate.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        )
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                    "rating": "Disagree",
                    "score": 0.9,
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                    "rating": "Disagree",
                    "score": 0.5,
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
            batch_size=0,
            existing_questions=[
                {
                    "question": "Is the output relevant to input?",
                    "custom_model_id": "your-model-id",
                    "label": "some input",
                    "parameters": [
                        0.14285714285714285,
                        0.2857142857142857,
                        0.42857142857142855,
                        0.5714285714285714,
                        0.7142857142857143,
                        0.8571428571428571,
                    ],
                    "python_code": '\ndef score(response_text: str, input_text: str, kwargs: dict) -> dict:\n    word_count = len(response_text.split())\n    if word_count > 10:\n        return {"score": 0.2, "explanation": "Response has more than 10 words"}\n    elif word_count > 5:\n        return{"score": 0.6, "explanation": "Response has more than 5 words"}\n    else:\n        return {"score": 1, "explanation": "Response has 5 or fewer words"}\n',
                    "scoring_type": "PI_SCORER",
                    "tag": "Legal Formatting",
                    "weight": 1,
                }
            ],
            num_questions=0,
            retain_existing_questions=False,
            try_auto_generating_python_code=False,
        )
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.generate.with_raw_response.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.generate.with_streaming_response.start_job(
            application_description="Write a children's story communicating a simple life lesson.",
            examples=[
                {
                    "llm_input": "good input",
                    "llm_output": "good response",
                },
                {
                    "llm_input": "neutral input",
                    "llm_output": "neutral response",
                },
            ],
            preference_examples=[
                {
                    "chosen": "chosen response",
                    "llm_input": "some input",
                    "rejected": "rejected response",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateStartJobResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        generate = await async_client.scoring_system.generate.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.generate.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(str, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.generate.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(str, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.scoring_system.generate.with_raw_response.stream_messages(
                "",
            )
