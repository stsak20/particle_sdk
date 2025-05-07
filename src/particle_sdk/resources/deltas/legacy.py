# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.deltas import legacy_search_resources_params
from ...types.deltas.legacy_read_resource_response import LegacyReadResourceResponse
from ...types.deltas.legacy_search_resources_response import LegacySearchResourcesResponse

__all__ = ["LegacyResource", "AsyncLegacyResource"]


class LegacyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stsak20/particle_sdk#accessing-raw-response-data-eg-headers
        """
        return LegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stsak20/particle_sdk#with_streaming_response
        """
        return LegacyResourceWithStreamingResponse(self)

    def read_resource(
        self,
        resource_id: str,
        *,
        resource_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegacyReadResourceResponse:
        """
        Read a specified FHIR resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            f"/deltas/R4/{resource_type}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyReadResourceResponse,
        )

    def search_resources(
        self,
        resource_type: str,
        *,
        person: str,
        _last_updated: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegacySearchResourcesResponse:
        """
        Search for FHIR resources.

        Args:
          person: Particle Patient ID

          _last_updated: Resources updated after this time will be included

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        return self._get(
            f"/deltas/R4/{resource_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "person": person,
                        "_last_updated": _last_updated,
                    },
                    legacy_search_resources_params.LegacySearchResourcesParams,
                ),
            ),
            cast_to=LegacySearchResourcesResponse,
        )


class AsyncLegacyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stsak20/particle_sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stsak20/particle_sdk#with_streaming_response
        """
        return AsyncLegacyResourceWithStreamingResponse(self)

    async def read_resource(
        self,
        resource_id: str,
        *,
        resource_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegacyReadResourceResponse:
        """
        Read a specified FHIR resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            f"/deltas/R4/{resource_type}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyReadResourceResponse,
        )

    async def search_resources(
        self,
        resource_type: str,
        *,
        person: str,
        _last_updated: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegacySearchResourcesResponse:
        """
        Search for FHIR resources.

        Args:
          person: Particle Patient ID

          _last_updated: Resources updated after this time will be included

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        return await self._get(
            f"/deltas/R4/{resource_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "person": person,
                        "_last_updated": _last_updated,
                    },
                    legacy_search_resources_params.LegacySearchResourcesParams,
                ),
            ),
            cast_to=LegacySearchResourcesResponse,
        )


class LegacyResourceWithRawResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

        self.read_resource = to_raw_response_wrapper(
            legacy.read_resource,
        )
        self.search_resources = to_raw_response_wrapper(
            legacy.search_resources,
        )


class AsyncLegacyResourceWithRawResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

        self.read_resource = async_to_raw_response_wrapper(
            legacy.read_resource,
        )
        self.search_resources = async_to_raw_response_wrapper(
            legacy.search_resources,
        )


class LegacyResourceWithStreamingResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

        self.read_resource = to_streamed_response_wrapper(
            legacy.read_resource,
        )
        self.search_resources = to_streamed_response_wrapper(
            legacy.search_resources,
        )


class AsyncLegacyResourceWithStreamingResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

        self.read_resource = async_to_streamed_response_wrapper(
            legacy.read_resource,
        )
        self.search_resources = async_to_streamed_response_wrapper(
            legacy.search_resources,
        )
