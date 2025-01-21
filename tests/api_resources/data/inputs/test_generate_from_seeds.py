# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twopir import Twopir, AsyncTwopir
from tests.utils import assert_matches_type
from twopir.types.data.inputs import (
    GenerateFromSeedGenerateResponse,
    GenerateFromSeedRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerateFromSeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Twopir) -> None:
        generate_from_seed = client.data.inputs.generate_from_seeds.retrieve(
            "job_id",
        )
        assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Twopir) -> None:
        response = client.data.inputs.generate_from_seeds.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = response.parse()
        assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Twopir) -> None:
        with client.data.inputs.generate_from_seeds.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = response.parse()
            assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Twopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.inputs.generate_from_seeds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_generate(self, client: Twopir) -> None:
        generate_from_seed = client.data.inputs.generate_from_seeds.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        )
        assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Twopir) -> None:
        response = client.data.inputs.generate_from_seeds.with_raw_response.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = response.parse()
        assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Twopir) -> None:
        with client.data.inputs.generate_from_seeds.with_streaming_response.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = response.parse()
            assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream_messages(self, client: Twopir) -> None:
        generate_from_seed = client.data.inputs.generate_from_seeds.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_from_seed, path=["response"])

    @parametrize
    def test_raw_response_stream_messages(self, client: Twopir) -> None:
        response = client.data.inputs.generate_from_seeds.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = response.parse()
        assert_matches_type(str, generate_from_seed, path=["response"])

    @parametrize
    def test_streaming_response_stream_messages(self, client: Twopir) -> None:
        with client.data.inputs.generate_from_seeds.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = response.parse()
            assert_matches_type(str, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream_messages(self, client: Twopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.data.inputs.generate_from_seeds.with_raw_response.stream_messages(
                "",
            )


class TestAsyncGenerateFromSeeds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwopir) -> None:
        generate_from_seed = await async_client.data.inputs.generate_from_seeds.retrieve(
            "job_id",
        )
        assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.generate_from_seeds.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = await response.parse()
        assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.generate_from_seeds.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = await response.parse()
            assert_matches_type(GenerateFromSeedRetrieveResponse, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.inputs.generate_from_seeds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_generate(self, async_client: AsyncTwopir) -> None:
        generate_from_seed = await async_client.data.inputs.generate_from_seeds.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        )
        assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.generate_from_seeds.with_raw_response.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = await response.parse()
        assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.generate_from_seeds.with_streaming_response.generate(
            seeds={
                "contract_description": "contract_description",
                "num_inputs": 0,
                "seeds": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = await response.parse()
            assert_matches_type(GenerateFromSeedGenerateResponse, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream_messages(self, async_client: AsyncTwopir) -> None:
        generate_from_seed = await async_client.data.inputs.generate_from_seeds.stream_messages(
            "job_id",
        )
        assert_matches_type(str, generate_from_seed, path=["response"])

    @parametrize
    async def test_raw_response_stream_messages(self, async_client: AsyncTwopir) -> None:
        response = await async_client.data.inputs.generate_from_seeds.with_raw_response.stream_messages(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_from_seed = await response.parse()
        assert_matches_type(str, generate_from_seed, path=["response"])

    @parametrize
    async def test_streaming_response_stream_messages(self, async_client: AsyncTwopir) -> None:
        async with async_client.data.inputs.generate_from_seeds.with_streaming_response.stream_messages(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_from_seed = await response.parse()
            assert_matches_type(str, generate_from_seed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream_messages(self, async_client: AsyncTwopir) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.data.inputs.generate_from_seeds.with_raw_response.stream_messages(
                "",
            )
