# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import Withpi, AsyncWithpi
from tests.utils import assert_matches_type
from withpi.types.data import (
    SyntheticDataStatus,
    GenerateSyntheticDataListResponse,
    GenerateSyntheticDataStreamDataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerateSyntheticData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Withpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Withpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Withpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Withpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Withpi) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Withpi) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Withpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.list()
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Withpi) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Withpi) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: Withpi) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: Withpi) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: Withpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_data(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.stream_data(
            "job_id",
        )
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_data(self, client: Withpi) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_data(self, client: Withpi) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_data(self, client: Withpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.stream_data(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_messages(self, client: Withpi) -> None:
        generate_synthetic_data = client.data.generate_synthetic_data.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_messages(self, client: Withpi) -> None:
        response = client.data.generate_synthetic_data.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_messages(self, client: Withpi) -> None:
        with client.data.generate_synthetic_data.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_messages(self, client: Withpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.generate_synthetic_data.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGenerateSyntheticData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncWithpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWithpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWithpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWithpi) -> None:
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.retrieve(
            "job_id",
        )
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWithpi) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWithpi) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(SyntheticDataStatus, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWithpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.list()
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.list(
            state="QUEUED",
        )
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWithpi) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWithpi) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(GenerateSyntheticDataListResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.cancel(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncWithpi) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncWithpi) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncWithpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_data(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.stream_data(
            "job_id",
        )
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_data(self, async_client: AsyncWithpi) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.stream_data(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_data(self, async_client: AsyncWithpi) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.stream_data(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(GenerateSyntheticDataStreamDataResponse, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_data(self, async_client: AsyncWithpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.stream_data(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncWithpi) -> None:
        generate_synthetic_data = await async_client.data.generate_synthetic_data.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncWithpi) -> None:
        response = await async_client.data.generate_synthetic_data.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_synthetic_data = await response.parse()
        assert_matches_type(str, generate_synthetic_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncWithpi) -> None:
        async with async_client.data.generate_synthetic_data.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_synthetic_data = await response.parse()
            assert_matches_type(str, generate_synthetic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncWithpi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.generate_synthetic_data.with_raw_response.stream_messages(
                "",
            )
