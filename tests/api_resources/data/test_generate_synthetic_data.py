# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.data import (
    GenerateSyntheticDataListJobsResponse,
    GenerateSyntheticDataStreamDataResponse,
)
from withpi.types.shared import SyntheticDataStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerateSyntheticData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            application_description="AI application for writing a children's story given topics.",
            batch_size=5,
            exploration_mode="CONSERVATIVE",
            num_shots=5,
            system_prompt="Write a children's story given a topic from the user.",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_list_jobs(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.list_jobs()
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    def test_method_list_jobs_with_all_params(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.list_jobs(
            state="QUEUED",
        )
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_list_jobs(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_list_jobs(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream_data(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.stream_data(
            "job_id",
        )
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_stream_data(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_stream_data(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream_data(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.stream_data(
                "",
            )

    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGenerateSyntheticData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            application_description="AI application for writing a children's story given topics.",
            batch_size=5,
            exploration_mode="CONSERVATIVE",
            num_shots=5,
            system_prompt="Write a children's story given a topic from the user.",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.create(
            num_examples_to_generate=50,
            seeds=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_list_jobs(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.list_jobs()
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_method_list_jobs_with_all_params(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.list_jobs(
            state="QUEUED",
        )
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_list_jobs(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.list_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_list_jobs(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.list_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(GenerateSyntheticDataListJobsResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream_data(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.stream_data(
            "job_id",
        )
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_stream_data(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_stream_data(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream_data(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.stream_data(
                "",
            )

    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.stream_messages(
                "",
            )
