# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.shared import ClassificationStatus
from withpi.types.search.query_classifier import (
    DistillListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDistill:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.retrieve(
            "job_id",
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(ClassificationStatus, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.search.query_classifier.distill.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.list()
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.list(
            state="QUEUED",
        )
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(DistillListResponse, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.cancel(
            "job_id",
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.search.query_classifier.distill.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_download(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_download(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_download(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_download(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.search.query_classifier.distill.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_start_job(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_start_job_with_all_params(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            learning_rate=0.000005,
            num_train_epochs=5,
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start_job(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start_job(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(ClassificationStatus, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_messages(self, client: PiClient) -> None:
        distill = client.search.query_classifier.distill.stream_messages(
            "job_id",
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_messages(self, client: PiClient) -> None:
        response = client.search.query_classifier.distill.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_messages(self, client: PiClient) -> None:
        with client.search.query_classifier.distill.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.search.query_classifier.distill.with_raw_response.stream_messages(
                "",
            )


class TestAsyncDistill:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.retrieve(
            "job_id",
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(ClassificationStatus, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.search.query_classifier.distill.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.list()
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.list(
            state="QUEUED",
        )
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(DistillListResponse, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(DistillListResponse, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.cancel(
            "job_id",
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.search.query_classifier.distill.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_download(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_download(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.search.query_classifier.distill.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_job(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_job_with_all_params(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
            learning_rate=0.000005,
            num_train_epochs=5,
        )
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start_job(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(ClassificationStatus, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start_job(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.start_job(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(ClassificationStatus, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncPiClient) -> None:
        distill = await async_client.search.query_classifier.distill.stream_messages(
            "job_id",
        )
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.search.query_classifier.distill.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        distill = await response.parse()
        assert_matches_type(str, distill, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.search.query_classifier.distill.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            distill = await response.parse()
            assert_matches_type(str, distill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.search.query_classifier.distill.with_raw_response.stream_messages(
                "",
            )
