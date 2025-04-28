# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FlatCollectDataParams"]


class FlatCollectDataParams(TypedDict, total=False):
    allergies: Annotated[str, PropertyInfo(alias="ALLERGIES")]
    """Optional query parameter for filtering ALLERGIES dataset.

    Does not require a value.
    """

    compositions: Annotated[str, PropertyInfo(alias="COMPOSITIONS")]
    """Optional query parameter for filtering COMPOSITIONS dataset.

    Does not require a value.
    """

    coverages: Annotated[str, PropertyInfo(alias="COVERAGES")]
    """Optional query parameter for filtering COVERAGES dataset.

    Does not require a value.
    """

    document_references: Annotated[str, PropertyInfo(alias="DOCUMENT_REFERENCES")]
    """Optional query parameter for filtering DOCUMENT_REFERENCES dataset.

    Does not require a value.
    """

    encounters: Annotated[str, PropertyInfo(alias="ENCOUNTERS")]
    """Optional query parameter for filtering ENCOUNTERS dataset.

    Does not require a value.
    """

    family_member_histories: Annotated[str, PropertyInfo(alias="FAMILY_MEMBER_HISTORIES")]
    """Optional query parameter for filtering FAMILY_MEMBER_HISTORIES dataset.

    Does not require a value.
    """

    immunizations: Annotated[str, PropertyInfo(alias="IMMUNIZATIONS")]
    """Optional query parameter for filtering IMMUNIZATIONS dataset.

    Does not require a value.
    """

    labs: Annotated[str, PropertyInfo(alias="LABS")]
    """Optional query parameter for filtering LABS dataset. Does not require a value."""

    locations: Annotated[str, PropertyInfo(alias="LOCATIONS")]
    """Optional query parameter for filtering LOCATIONS dataset.

    Does not require a value.
    """

    medications: Annotated[str, PropertyInfo(alias="MEDICATIONS")]
    """Optional query parameter for filtering MEDICATIONS dataset.

    Does not require a value.
    """

    medrecs: Annotated[str, PropertyInfo(alias="MEDRECS")]
    """Optional query parameter for filtering MEDRECS dataset.

    Does not require a value.
    """

    organizations: Annotated[str, PropertyInfo(alias="ORGANIZATIONS")]
    """Optional query parameter for filtering ORGANIZATIONS dataset.

    Does not require a value.
    """

    patients: Annotated[str, PropertyInfo(alias="PATIENTS")]
    """Optional query parameter for filtering PATIENTS dataset.

    Does not require a value.
    """

    practitioners: Annotated[str, PropertyInfo(alias="PRACTITIONERS")]
    """Optional query parameter for filtering PRACTITIONERS dataset.

    Does not require a value.
    """

    problems: Annotated[str, PropertyInfo(alias="PROBLEMS")]
    """Optional query parameter for filtering PROBLEMS dataset.

    Does not require a value.
    """

    procedures: Annotated[str, PropertyInfo(alias="PROCEDURES")]
    """Optional query parameter for filtering PROCEDURES dataset.

    Does not require a value.
    """

    provenances: Annotated[str, PropertyInfo(alias="PROVENANCES")]
    """Optional query parameter for filtering PROVENANCES dataset.

    Does not require a value.
    """

    related_persons: Annotated[str, PropertyInfo(alias="RELATED_PERSONS")]
    """Optional query parameter for filtering RELATED_PERSONS dataset.

    Does not require a value.
    """

    social_histories: Annotated[str, PropertyInfo(alias="SOCIAL_HISTORIES")]
    """Optional query parameter for filtering SOCIAL_HISTORIES dataset.

    Does not require a value.
    """

    vital_signs: Annotated[str, PropertyInfo(alias="VITAL_SIGNS")]
    """Optional query parameter for filtering VITAL_SIGNS dataset.

    Does not require a value.
    """
