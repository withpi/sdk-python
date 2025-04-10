# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from withpi import PiClient, AsyncPiClient
from tests.utils import assert_matches_type
from withpi.types.shared import ScoringSpec, ScoringSystemMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoringSystem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_with_all_params(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.generate(
            application_description="Write a children's story communicating a simple life lesson.",
            try_auto_generating_python_code=False,
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(ScoringSpec, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_import_spec(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_import_spec_with_all_params(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
            source="HUGGINGFACE",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_import_spec(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_import_spec(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(ScoringSpec, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_score(self, client: PiClient) -> None:
        scoring_system = client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_score(self, client: PiClient) -> None:
        response = client.scoring_system.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = response.parse()
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_score(self, client: PiClient) -> None:
        with client.scoring_system.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = response.parse()
            assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScoringSystem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.generate(
            application_description="Write a children's story communicating a simple life lesson.",
            try_auto_generating_python_code=False,
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.generate(
            application_description="Write a children's story communicating a simple life lesson.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(ScoringSpec, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_import_spec(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_import_spec_with_all_params(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
            hf_token="hf_token",
            source="HUGGINGFACE",
        )
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_import_spec(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(ScoringSpec, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_import_spec(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.import_spec(
            hf_scoring_spec_name="withpi/tldr_scoring_system",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(ScoringSpec, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_score(self, async_client: AsyncPiClient) -> None:
        scoring_system = await async_client.scoring_system.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        )
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_score(self, async_client: AsyncPiClient) -> None:
        response = await async_client.scoring_system.with_raw_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_system = await response.parse()
        assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncPiClient) -> None:
        async with async_client.scoring_system.with_streaming_response.score(
            llm_input="Tell me something different",
            llm_output="The lazy dog was jumped over by the quick brown fox",
            scoring_spec={
                "description": "Write a children's story communicating a simple life lesson.",
                "dimensions": [
                    {
                        "description": "dimension1 description",
                        "label": "dimension1",
                        "sub_dimensions": [
                            {
                                "description": "subdimension1 description",
                                "label": "subdimension1",
                                "scoring_type": "PI_SCORER",
                            }
                        ],
                    }
                ],
                "name": "Sample Scoring Spec",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_system = await response.parse()
            assert_matches_type(ScoringSystemMetrics, scoring_system, path=["response"])

        assert cast(Any, response.is_closed) is True
