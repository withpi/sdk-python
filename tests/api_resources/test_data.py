# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types import DataListQuestionAnswerJobsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_question_answer_jobs(self, client: PiClient) -> None:
        data = client.data.list_question_answer_jobs()
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    def test_method_list_question_answer_jobs_with_all_params(self, client: PiClient) -> None:
        data = client.data.list_question_answer_jobs(
            state="QUEUED",
        )
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    def test_raw_response_list_question_answer_jobs(self, client: PiClient) -> None:
        response = client.data.with_raw_response.list_question_answer_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    def test_streaming_response_list_question_answer_jobs(self, client: PiClient) -> None:
        with client.data.with_streaming_response.list_question_answer_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_question_answer_jobs(self, async_client: AsyncPiClient) -> None:
        data = await async_client.data.list_question_answer_jobs()
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    async def test_method_list_question_answer_jobs_with_all_params(self, async_client: AsyncPiClient) -> None:
        data = await async_client.data.list_question_answer_jobs(
            state="QUEUED",
        )
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    async def test_raw_response_list_question_answer_jobs(self, async_client: AsyncPiClient) -> None:
        response = await async_client.data.with_raw_response.list_question_answer_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

    @parametrize
    async def test_streaming_response_list_question_answer_jobs(self, async_client: AsyncPiClient) -> None:
        async with async_client.data.with_streaming_response.list_question_answer_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert_matches_type(DataListQuestionAnswerJobsResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True
