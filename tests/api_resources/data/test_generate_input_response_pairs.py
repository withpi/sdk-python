# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.data import (
    GenerateInputResponsePairListResponse,
    GenerateInputResponsePairStreamDataResponse,
)
from withpi.types.shared import SyntheticDataStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerateInputResponsePairs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_input_response_pairs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.list()
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(str, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_input_response_pairs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            application_description="AI application for writing a children's story given topics.",
            batch_size=10,
            exploration_mode="CONSERVATIVE",
            num_shots=5,
            run_parallel_batches=True,
            system_prompt="Write a children's story given a topic from the user.",
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_data(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.stream_data(
            "job_id",
        )
        assert_matches_type(
            GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_data(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(
            GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_data(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(
                GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_data(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_input_response_pairs.with_raw_response.stream_data(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        generate_input_response_pair = client.data.generate_input_response_pairs.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.data.generate_input_response_pairs.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = response.parse()
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.data.generate_input_response_pairs.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = response.parse()
            assert_matches_type(str, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_input_response_pairs.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGenerateInputResponsePairs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_input_response_pairs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.list()
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(GenerateInputResponsePairListResponse, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(str, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_input_response_pairs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            application_description="AI application for writing a children's story given topics.",
            batch_size=10,
            exploration_mode="CONSERVATIVE",
            num_shots=5,
            run_parallel_batches=True,
            system_prompt="Write a children's story given a topic from the user.",
        )
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.start_job(
            num_pairs_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(SyntheticDataStatus, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_data(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.stream_data(
            "job_id",
        )
        assert_matches_type(
            GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_data(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(
            GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_data(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(
                GenerateInputResponsePairStreamDataResponse, generate_input_response_pair, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_data(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_input_response_pairs.with_raw_response.stream_data(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        generate_input_response_pair = await async_client.data.generate_input_response_pairs.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_input_response_pairs.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_input_response_pair = await response.parse()
        assert_matches_type(str, generate_input_response_pair, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_input_response_pairs.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_input_response_pair = await response.parse()
            assert_matches_type(str, generate_input_response_pair, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_input_response_pairs.with_raw_response.stream_messages(
                "",
            )
