# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from particle_sdk import ParticleSDK, AsyncParticleSDK
from particle_sdk.types.deltas import (
    LegacyReadResourceResponse,
    LegacySearchResourcesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegacy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_read_resource(self, client: ParticleSDK) -> None:
        legacy = client.deltas.legacy.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        )
        assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_read_resource(self, client: ParticleSDK) -> None:
        response = client.deltas.legacy.with_raw_response.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = response.parse()
        assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_read_resource(self, client: ParticleSDK) -> None:
        with client.deltas.legacy.with_streaming_response.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = response.parse()
            assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_read_resource(self, client: ParticleSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type` but received ''"):
            client.deltas.legacy.with_raw_response.read_resource(
                resource_id="resource_id",
                resource_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.deltas.legacy.with_raw_response.read_resource(
                resource_id="",
                resource_type="resource_type",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_search_resources(self, client: ParticleSDK) -> None:
        legacy = client.deltas.legacy.search_resources(
            resource_type="resource_type",
            person="person",
        )
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_resources_with_all_params(self, client: ParticleSDK) -> None:
        legacy = client.deltas.legacy.search_resources(
            resource_type="resource_type",
            person="person",
            _last_updated="_lastUpdated",
        )
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search_resources(self, client: ParticleSDK) -> None:
        response = client.deltas.legacy.with_raw_response.search_resources(
            resource_type="resource_type",
            person="person",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = response.parse()
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search_resources(self, client: ParticleSDK) -> None:
        with client.deltas.legacy.with_streaming_response.search_resources(
            resource_type="resource_type",
            person="person",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = response.parse()
            assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_search_resources(self, client: ParticleSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type` but received ''"):
            client.deltas.legacy.with_raw_response.search_resources(
                resource_type="",
                person="person",
            )


class TestAsyncLegacy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_read_resource(self, async_client: AsyncParticleSDK) -> None:
        legacy = await async_client.deltas.legacy.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        )
        assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_read_resource(self, async_client: AsyncParticleSDK) -> None:
        response = await async_client.deltas.legacy.with_raw_response.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = await response.parse()
        assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_read_resource(self, async_client: AsyncParticleSDK) -> None:
        async with async_client.deltas.legacy.with_streaming_response.read_resource(
            resource_id="resource_id",
            resource_type="resource_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = await response.parse()
            assert_matches_type(LegacyReadResourceResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_read_resource(self, async_client: AsyncParticleSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type` but received ''"):
            await async_client.deltas.legacy.with_raw_response.read_resource(
                resource_id="resource_id",
                resource_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.deltas.legacy.with_raw_response.read_resource(
                resource_id="",
                resource_type="resource_type",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_resources(self, async_client: AsyncParticleSDK) -> None:
        legacy = await async_client.deltas.legacy.search_resources(
            resource_type="resource_type",
            person="person",
        )
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_resources_with_all_params(self, async_client: AsyncParticleSDK) -> None:
        legacy = await async_client.deltas.legacy.search_resources(
            resource_type="resource_type",
            person="person",
            _last_updated="_lastUpdated",
        )
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search_resources(self, async_client: AsyncParticleSDK) -> None:
        response = await async_client.deltas.legacy.with_raw_response.search_resources(
            resource_type="resource_type",
            person="person",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = await response.parse()
        assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search_resources(self, async_client: AsyncParticleSDK) -> None:
        async with async_client.deltas.legacy.with_streaming_response.search_resources(
            resource_type="resource_type",
            person="person",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = await response.parse()
            assert_matches_type(LegacySearchResourcesResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_search_resources(self, async_client: AsyncParticleSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type` but received ''"):
            await async_client.deltas.legacy.with_raw_response.search_resources(
                resource_type="",
                person="person",
            )
