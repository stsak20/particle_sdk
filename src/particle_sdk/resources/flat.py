# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import flat_create_params, flat_collect_data_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.query import Query
from .._base_client import make_request_options
from ..types.deltas.datasets import Datasets

__all__ = ["FlatResource", "AsyncFlatResource"]


class FlatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/particle_sdk-python#accessing-raw-response-data-eg-headers
        """
        return FlatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/particle_sdk-python#with_streaming_response
        """
        return FlatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        date_of_birth: str,
        family_name: str,
        gender: str,
        given_name: str,
        purpose_of_use: str,
        address_city: str | NotGiven = NOT_GIVEN,
        address_lines: List[str] | NotGiven = NOT_GIVEN,
        address_state: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        encounter_date: str | NotGiven = NOT_GIVEN,
        encounter_type: str | NotGiven = NOT_GIVEN,
        hints: List[str] | NotGiven = NOT_GIVEN,
        npi: str | NotGiven = NOT_GIVEN,
        patient_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        specialties: List[str] | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        telephone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Query:
        """
        Submit Flat Patient

        Args:
          date_of_birth: The patient's date of birth, this field is required and must be of the format
              YYYY-MM-DD.

          family_name: The patient's family name (last name), this field is required.

          gender: The patient's gender, must be either Female or Female.

          given_name: The patient's given name (first name), this field is required.

          purpose_of_use: The purpose of use for which this request is being made

          address_city: The patient's home city.

          address_lines: The patient's home street address. This should not include the patient's city,
              state, or zip code.

          address_state: The patient's home state.

          email: The patient's email, must be a valid email address.

          encounter_date: Encounter Date for which this query is being made

          encounter_type: Encounter Type for which this query is being made

          hints: Postal codes hinting at the believed location of records.

          npi: The National Provider Identifier of the provider that this request is being made
              by.

          patient_id: The unique patient id in an external system

          postal_code: The patient's home postal (zip) code.

          specialties: The list of specialty searches requested for this patient

          ssn: The patient's social security number, must be a valid US social security number.

          telephone: The patient's telephone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/flat",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "family_name": family_name,
                    "gender": gender,
                    "given_name": given_name,
                    "purpose_of_use": purpose_of_use,
                    "address_city": address_city,
                    "address_lines": address_lines,
                    "address_state": address_state,
                    "email": email,
                    "encounter_date": encounter_date,
                    "encounter_type": encounter_type,
                    "hints": hints,
                    "npi": npi,
                    "patient_id": patient_id,
                    "postal_code": postal_code,
                    "specialties": specialties,
                    "ssn": ssn,
                    "telephone": telephone,
                },
                flat_create_params.FlatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Query,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Query:
        """
        Get Flat Patient

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/flat/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Query,
        )

    def collect_data(
        self,
        id: str,
        *,
        allergies: str | NotGiven = NOT_GIVEN,
        compositions: str | NotGiven = NOT_GIVEN,
        coverages: str | NotGiven = NOT_GIVEN,
        document_references: str | NotGiven = NOT_GIVEN,
        encounters: str | NotGiven = NOT_GIVEN,
        family_member_histories: str | NotGiven = NOT_GIVEN,
        immunizations: str | NotGiven = NOT_GIVEN,
        labs: str | NotGiven = NOT_GIVEN,
        locations: str | NotGiven = NOT_GIVEN,
        medications: str | NotGiven = NOT_GIVEN,
        medrecs: str | NotGiven = NOT_GIVEN,
        organizations: str | NotGiven = NOT_GIVEN,
        patients: str | NotGiven = NOT_GIVEN,
        practitioners: str | NotGiven = NOT_GIVEN,
        problems: str | NotGiven = NOT_GIVEN,
        procedures: str | NotGiven = NOT_GIVEN,
        provenances: str | NotGiven = NOT_GIVEN,
        related_persons: str | NotGiven = NOT_GIVEN,
        social_histories: str | NotGiven = NOT_GIVEN,
        vital_signs: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasets:
        """Query parameter filtering is not included by default.

        If you require access,
        please contact support@particlehealth.com.

        Args:
          allergies: Optional query parameter for filtering ALLERGIES dataset. Does not require a
              value.

          compositions: Optional query parameter for filtering COMPOSITIONS dataset. Does not require a
              value.

          coverages: Optional query parameter for filtering COVERAGES dataset. Does not require a
              value.

          document_references: Optional query parameter for filtering DOCUMENT_REFERENCES dataset. Does not
              require a value.

          encounters: Optional query parameter for filtering ENCOUNTERS dataset. Does not require a
              value.

          family_member_histories: Optional query parameter for filtering FAMILY_MEMBER_HISTORIES dataset. Does not
              require a value.

          immunizations: Optional query parameter for filtering IMMUNIZATIONS dataset. Does not require a
              value.

          labs: Optional query parameter for filtering LABS dataset. Does not require a value.

          locations: Optional query parameter for filtering LOCATIONS dataset. Does not require a
              value.

          medications: Optional query parameter for filtering MEDICATIONS dataset. Does not require a
              value.

          medrecs: Optional query parameter for filtering MEDRECS dataset. Does not require a
              value.

          organizations: Optional query parameter for filtering ORGANIZATIONS dataset. Does not require a
              value.

          patients: Optional query parameter for filtering PATIENTS dataset. Does not require a
              value.

          practitioners: Optional query parameter for filtering PRACTITIONERS dataset. Does not require a
              value.

          problems: Optional query parameter for filtering PROBLEMS dataset. Does not require a
              value.

          procedures: Optional query parameter for filtering PROCEDURES dataset. Does not require a
              value.

          provenances: Optional query parameter for filtering PROVENANCES dataset. Does not require a
              value.

          related_persons: Optional query parameter for filtering RELATED_PERSONS dataset. Does not require
              a value.

          social_histories: Optional query parameter for filtering SOCIAL_HISTORIES dataset. Does not
              require a value.

          vital_signs: Optional query parameter for filtering VITAL_SIGNS dataset. Does not require a
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/flat/{id}/collect-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "allergies": allergies,
                        "compositions": compositions,
                        "coverages": coverages,
                        "document_references": document_references,
                        "encounters": encounters,
                        "family_member_histories": family_member_histories,
                        "immunizations": immunizations,
                        "labs": labs,
                        "locations": locations,
                        "medications": medications,
                        "medrecs": medrecs,
                        "organizations": organizations,
                        "patients": patients,
                        "practitioners": practitioners,
                        "problems": problems,
                        "procedures": procedures,
                        "provenances": provenances,
                        "related_persons": related_persons,
                        "social_histories": social_histories,
                        "vital_signs": vital_signs,
                    },
                    flat_collect_data_params.FlatCollectDataParams,
                ),
            ),
            cast_to=Datasets,
        )

    def retrieve_resource(
        self,
        resource_id: str,
        *,
        patient_id: str,
        resource_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasets:
        """
        Get Flat Resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not patient_id:
            raise ValueError(f"Expected a non-empty value for `patient_id` but received {patient_id!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            f"/flat/{patient_id}/{resource_type}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasets,
        )


class AsyncFlatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/particle_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/particle_sdk-python#with_streaming_response
        """
        return AsyncFlatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        date_of_birth: str,
        family_name: str,
        gender: str,
        given_name: str,
        purpose_of_use: str,
        address_city: str | NotGiven = NOT_GIVEN,
        address_lines: List[str] | NotGiven = NOT_GIVEN,
        address_state: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        encounter_date: str | NotGiven = NOT_GIVEN,
        encounter_type: str | NotGiven = NOT_GIVEN,
        hints: List[str] | NotGiven = NOT_GIVEN,
        npi: str | NotGiven = NOT_GIVEN,
        patient_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        specialties: List[str] | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        telephone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Query:
        """
        Submit Flat Patient

        Args:
          date_of_birth: The patient's date of birth, this field is required and must be of the format
              YYYY-MM-DD.

          family_name: The patient's family name (last name), this field is required.

          gender: The patient's gender, must be either Female or Female.

          given_name: The patient's given name (first name), this field is required.

          purpose_of_use: The purpose of use for which this request is being made

          address_city: The patient's home city.

          address_lines: The patient's home street address. This should not include the patient's city,
              state, or zip code.

          address_state: The patient's home state.

          email: The patient's email, must be a valid email address.

          encounter_date: Encounter Date for which this query is being made

          encounter_type: Encounter Type for which this query is being made

          hints: Postal codes hinting at the believed location of records.

          npi: The National Provider Identifier of the provider that this request is being made
              by.

          patient_id: The unique patient id in an external system

          postal_code: The patient's home postal (zip) code.

          specialties: The list of specialty searches requested for this patient

          ssn: The patient's social security number, must be a valid US social security number.

          telephone: The patient's telephone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/flat",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "family_name": family_name,
                    "gender": gender,
                    "given_name": given_name,
                    "purpose_of_use": purpose_of_use,
                    "address_city": address_city,
                    "address_lines": address_lines,
                    "address_state": address_state,
                    "email": email,
                    "encounter_date": encounter_date,
                    "encounter_type": encounter_type,
                    "hints": hints,
                    "npi": npi,
                    "patient_id": patient_id,
                    "postal_code": postal_code,
                    "specialties": specialties,
                    "ssn": ssn,
                    "telephone": telephone,
                },
                flat_create_params.FlatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Query,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Query:
        """
        Get Flat Patient

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/flat/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Query,
        )

    async def collect_data(
        self,
        id: str,
        *,
        allergies: str | NotGiven = NOT_GIVEN,
        compositions: str | NotGiven = NOT_GIVEN,
        coverages: str | NotGiven = NOT_GIVEN,
        document_references: str | NotGiven = NOT_GIVEN,
        encounters: str | NotGiven = NOT_GIVEN,
        family_member_histories: str | NotGiven = NOT_GIVEN,
        immunizations: str | NotGiven = NOT_GIVEN,
        labs: str | NotGiven = NOT_GIVEN,
        locations: str | NotGiven = NOT_GIVEN,
        medications: str | NotGiven = NOT_GIVEN,
        medrecs: str | NotGiven = NOT_GIVEN,
        organizations: str | NotGiven = NOT_GIVEN,
        patients: str | NotGiven = NOT_GIVEN,
        practitioners: str | NotGiven = NOT_GIVEN,
        problems: str | NotGiven = NOT_GIVEN,
        procedures: str | NotGiven = NOT_GIVEN,
        provenances: str | NotGiven = NOT_GIVEN,
        related_persons: str | NotGiven = NOT_GIVEN,
        social_histories: str | NotGiven = NOT_GIVEN,
        vital_signs: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasets:
        """Query parameter filtering is not included by default.

        If you require access,
        please contact support@particlehealth.com.

        Args:
          allergies: Optional query parameter for filtering ALLERGIES dataset. Does not require a
              value.

          compositions: Optional query parameter for filtering COMPOSITIONS dataset. Does not require a
              value.

          coverages: Optional query parameter for filtering COVERAGES dataset. Does not require a
              value.

          document_references: Optional query parameter for filtering DOCUMENT_REFERENCES dataset. Does not
              require a value.

          encounters: Optional query parameter for filtering ENCOUNTERS dataset. Does not require a
              value.

          family_member_histories: Optional query parameter for filtering FAMILY_MEMBER_HISTORIES dataset. Does not
              require a value.

          immunizations: Optional query parameter for filtering IMMUNIZATIONS dataset. Does not require a
              value.

          labs: Optional query parameter for filtering LABS dataset. Does not require a value.

          locations: Optional query parameter for filtering LOCATIONS dataset. Does not require a
              value.

          medications: Optional query parameter for filtering MEDICATIONS dataset. Does not require a
              value.

          medrecs: Optional query parameter for filtering MEDRECS dataset. Does not require a
              value.

          organizations: Optional query parameter for filtering ORGANIZATIONS dataset. Does not require a
              value.

          patients: Optional query parameter for filtering PATIENTS dataset. Does not require a
              value.

          practitioners: Optional query parameter for filtering PRACTITIONERS dataset. Does not require a
              value.

          problems: Optional query parameter for filtering PROBLEMS dataset. Does not require a
              value.

          procedures: Optional query parameter for filtering PROCEDURES dataset. Does not require a
              value.

          provenances: Optional query parameter for filtering PROVENANCES dataset. Does not require a
              value.

          related_persons: Optional query parameter for filtering RELATED_PERSONS dataset. Does not require
              a value.

          social_histories: Optional query parameter for filtering SOCIAL_HISTORIES dataset. Does not
              require a value.

          vital_signs: Optional query parameter for filtering VITAL_SIGNS dataset. Does not require a
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/flat/{id}/collect-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "allergies": allergies,
                        "compositions": compositions,
                        "coverages": coverages,
                        "document_references": document_references,
                        "encounters": encounters,
                        "family_member_histories": family_member_histories,
                        "immunizations": immunizations,
                        "labs": labs,
                        "locations": locations,
                        "medications": medications,
                        "medrecs": medrecs,
                        "organizations": organizations,
                        "patients": patients,
                        "practitioners": practitioners,
                        "problems": problems,
                        "procedures": procedures,
                        "provenances": provenances,
                        "related_persons": related_persons,
                        "social_histories": social_histories,
                        "vital_signs": vital_signs,
                    },
                    flat_collect_data_params.FlatCollectDataParams,
                ),
            ),
            cast_to=Datasets,
        )

    async def retrieve_resource(
        self,
        resource_id: str,
        *,
        patient_id: str,
        resource_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Datasets:
        """
        Get Flat Resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not patient_id:
            raise ValueError(f"Expected a non-empty value for `patient_id` but received {patient_id!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            f"/flat/{patient_id}/{resource_type}/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Datasets,
        )


class FlatResourceWithRawResponse:
    def __init__(self, flat: FlatResource) -> None:
        self._flat = flat

        self.create = to_raw_response_wrapper(
            flat.create,
        )
        self.retrieve = to_raw_response_wrapper(
            flat.retrieve,
        )
        self.collect_data = to_raw_response_wrapper(
            flat.collect_data,
        )
        self.retrieve_resource = to_raw_response_wrapper(
            flat.retrieve_resource,
        )


class AsyncFlatResourceWithRawResponse:
    def __init__(self, flat: AsyncFlatResource) -> None:
        self._flat = flat

        self.create = async_to_raw_response_wrapper(
            flat.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            flat.retrieve,
        )
        self.collect_data = async_to_raw_response_wrapper(
            flat.collect_data,
        )
        self.retrieve_resource = async_to_raw_response_wrapper(
            flat.retrieve_resource,
        )


class FlatResourceWithStreamingResponse:
    def __init__(self, flat: FlatResource) -> None:
        self._flat = flat

        self.create = to_streamed_response_wrapper(
            flat.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            flat.retrieve,
        )
        self.collect_data = to_streamed_response_wrapper(
            flat.collect_data,
        )
        self.retrieve_resource = to_streamed_response_wrapper(
            flat.retrieve_resource,
        )


class AsyncFlatResourceWithStreamingResponse:
    def __init__(self, flat: AsyncFlatResource) -> None:
        self._flat = flat

        self.create = async_to_streamed_response_wrapper(
            flat.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            flat.retrieve,
        )
        self.collect_data = async_to_streamed_response_wrapper(
            flat.collect_data,
        )
        self.retrieve_resource = async_to_streamed_response_wrapper(
            flat.retrieve_resource,
        )
