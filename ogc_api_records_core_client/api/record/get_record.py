from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.record_geo_json import RecordGeoJSON
from ...types import Response


def _get_kwargs(
    catalog_id: str,
    record_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections/{catalog_id}/items/{record_id}".format(
            catalog_id=catalog_id,
            record_id=record_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Exception_, RecordGeoJSON]]:
    if response.status_code == 200:
        response_200 = RecordGeoJSON.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Exception_.from_dict(response.json())

        return response_406

    if 400 <= response.status_code <= 499:
        response_4xx = Exception_.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = Exception_.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Exception_, RecordGeoJSON]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_id: str,
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Exception_, RecordGeoJSON]]:
    """fetch a single record

     Fetch the record with id `recordId` from the record collection
    with id `catalogId`.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, RecordGeoJSON]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        record_id=record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_id: str,
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Exception_, RecordGeoJSON]]:
    """fetch a single record

     Fetch the record with id `recordId` from the record collection
    with id `catalogId`.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, RecordGeoJSON]
    """

    return sync_detailed(
        catalog_id=catalog_id,
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    catalog_id: str,
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Exception_, RecordGeoJSON]]:
    """fetch a single record

     Fetch the record with id `recordId` from the record collection
    with id `catalogId`.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, RecordGeoJSON]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        record_id=record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_id: str,
    record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Exception_, RecordGeoJSON]]:
    """fetch a single record

     Fetch the record with id `recordId` from the record collection
    with id `catalogId`.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, RecordGeoJSON]
    """

    return (
        await asyncio_detailed(
            catalog_id=catalog_id,
            record_id=record_id,
            client=client,
        )
    ).parsed
