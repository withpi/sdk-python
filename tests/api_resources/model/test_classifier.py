# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.model import (
    ClassifierListResponse,
    ClassifierCreateResponse,
    ClassifierRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassifier:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PiClient) -> None:
        classifier = client.model.classifier.create(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PiClient) -> None:
        classifier = client.model.classifier.create(
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
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.create(
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
        classifier = response.parse()
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.create(
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

            classifier = response.parse()
            assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PiClient) -> None:
        classifier = client.model.classifier.retrieve(
            "job_id",
        )
        assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = response.parse()
        assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = response.parse()
            assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.classifier.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: PiClient) -> None:
        classifier = client.model.classifier.list()
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PiClient) -> None:
        classifier = client.model.classifier.list(
            state="QUEUED",
        )
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = response.parse()
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = response.parse()
            assert_matches_type(ClassifierListResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: PiClient) -> None:
        classifier = client.model.classifier.cancel(
            "job_id",
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.classifier.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_download(self, client: PiClient) -> None:
        classifier = client.model.classifier.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.classifier.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @parametrize
    def test_method_messages(self, client: PiClient) -> None:
        classifier = client.model.classifier.messages(
            "job_id",
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_raw_response_messages(self, client: PiClient) -> None:
        response = client.model.classifier.with_raw_response.messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    def test_streaming_response_messages(self, client: PiClient) -> None:
        with client.model.classifier.with_streaming_response.messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_messages(self, client: PiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.model.classifier.with_raw_response.messages(
                "",
            )


class TestAsyncClassifier:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.create(
            base_model="MODERNBERT_BASE",
            examples=[
                {
                    "llm_input": "Tell me something different",
                    "llm_output": "The lazy dog was jumped over by the quick brown fox",
                }
            ],
        )
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.create(
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
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.create(
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
        classifier = await response.parse()
        assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.create(
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

            classifier = await response.parse()
            assert_matches_type(ClassifierCreateResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.retrieve(
            "job_id",
        )
        assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = await response.parse()
        assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = await response.parse()
            assert_matches_type(ClassifierRetrieveResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.classifier.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.list()
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.list(
            state="QUEUED",
        )
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = await response.parse()
        assert_matches_type(ClassifierListResponse, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = await response.parse()
            assert_matches_type(ClassifierListResponse, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.cancel(
            "job_id",
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.cancel(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = await response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.cancel(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = await response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.classifier.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_download(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.download(
            job_id="job_id",
            serving_id=0,
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.download(
            job_id="job_id",
            serving_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = await response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.download(
            job_id="job_id",
            serving_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = await response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.classifier.with_raw_response.download(
                job_id="",
                serving_id=0,
            )

    @parametrize
    async def test_method_messages(self, async_client: AsyncPiClient) -> None:
        classifier = await async_client.model.classifier.messages(
            "job_id",
        )
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_raw_response_messages(self, async_client: AsyncPiClient) -> None:
        response = await async_client.model.classifier.with_raw_response.messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classifier = await response.parse()
        assert_matches_type(str, classifier, path=["response"])

    @parametrize
    async def test_streaming_response_messages(self, async_client: AsyncPiClient) -> None:
        async with async_client.model.classifier.with_streaming_response.messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classifier = await response.parse()
            assert_matches_type(str, classifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_messages(self, async_client: AsyncPiClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.model.classifier.with_raw_response.messages(
                "",
            )
