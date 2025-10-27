from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.get_records_response_200 import GetRecordsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    catalog_id: str,
    *,
    bbox: Union[Unset, list[float]] = UNSET,
    datetime_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    q: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    external_id: Union[Unset, list[str]] = UNSET,
    ids: Union[Unset, list[str]] = UNSET,
    sortby: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_bbox: Union[Unset, list[float]]
    if isinstance(bbox, Unset):
        json_bbox = UNSET
    elif isinstance(bbox, list):
        json_bbox = bbox

    else:
        json_bbox = bbox

    params["bbox"] = json_bbox

    params["datetime"] = datetime_

    params["limit"] = limit

    json_q: Union[Unset, list[str]] = UNSET
    if not isinstance(q, Unset):
        json_q = q

    params["q"] = json_q

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_external_id: Union[Unset, list[str]] = UNSET
    if not isinstance(external_id, Unset):
        json_external_id = external_id

    params["externalId"] = json_external_id

    json_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    json_sortby: Union[Unset, list[str]] = UNSET
    if not isinstance(sortby, Unset):
        json_sortby = sortby

    params["sortby"] = json_sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections/{catalog_id}/items".format(
            catalog_id=catalog_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Exception_, GetRecordsResponse200]]:
    if response.status_code == 200:
        response_200 = GetRecordsResponse200.from_dict(response.json())

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
) -> Response[Union[Exception_, GetRecordsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    bbox: Union[Unset, list[float]] = UNSET,
    datetime_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    q: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    external_id: Union[Unset, list[str]] = UNSET,
    ids: Union[Unset, list[str]] = UNSET,
    sortby: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Exception_, GetRecordsResponse200]]:
    """fetch records

     Fetch records from the record collection with id `catalogId`.

    Every record in a dataset belongs to a collection. A dataset may
    consist of multiple record collections. A record collection is often a
    collection of records of a similar type, based on a common schema.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        bbox (Union[Unset, list[float]]):
        datetime_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        q (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        external_id (Union[Unset, list[str]]):
        ids (Union[Unset, list[str]]):
        sortby (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, GetRecordsResponse200]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        bbox=bbox,
        datetime_=datetime_,
        limit=limit,
        q=q,
        type_=type_,
        external_id=external_id,
        ids=ids,
        sortby=sortby,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    bbox: Union[Unset, list[float]] = UNSET,
    datetime_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    q: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    external_id: Union[Unset, list[str]] = UNSET,
    ids: Union[Unset, list[str]] = UNSET,
    sortby: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Exception_, GetRecordsResponse200]]:
    """fetch records

     Fetch records from the record collection with id `catalogId`.

    Every record in a dataset belongs to a collection. A dataset may
    consist of multiple record collections. A record collection is often a
    collection of records of a similar type, based on a common schema.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        bbox (Union[Unset, list[float]]):
        datetime_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        q (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        external_id (Union[Unset, list[str]]):
        ids (Union[Unset, list[str]]):
        sortby (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, GetRecordsResponse200]
    """

    return sync_detailed(
        catalog_id=catalog_id,
        client=client,
        bbox=bbox,
        datetime_=datetime_,
        limit=limit,
        q=q,
        type_=type_,
        external_id=external_id,
        ids=ids,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    bbox: Union[Unset, list[float]] = UNSET,
    datetime_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    q: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    external_id: Union[Unset, list[str]] = UNSET,
    ids: Union[Unset, list[str]] = UNSET,
    sortby: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Exception_, GetRecordsResponse200]]:
    """fetch records

     Fetch records from the record collection with id `catalogId`.

    Every record in a dataset belongs to a collection. A dataset may
    consist of multiple record collections. A record collection is often a
    collection of records of a similar type, based on a common schema.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        bbox (Union[Unset, list[float]]):
        datetime_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        q (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        external_id (Union[Unset, list[str]]):
        ids (Union[Unset, list[str]]):
        sortby (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, GetRecordsResponse200]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        bbox=bbox,
        datetime_=datetime_,
        limit=limit,
        q=q,
        type_=type_,
        external_id=external_id,
        ids=ids,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    bbox: Union[Unset, list[float]] = UNSET,
    datetime_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    q: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    external_id: Union[Unset, list[str]] = UNSET,
    ids: Union[Unset, list[str]] = UNSET,
    sortby: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Exception_, GetRecordsResponse200]]:
    """fetch records

     Fetch records from the record collection with id `catalogId`.

    Every record in a dataset belongs to a collection. A dataset may
    consist of multiple record collections. A record collection is often a
    collection of records of a similar type, based on a common schema.

    Use content negotiation to request HTML or GeoJSON.

    Args:
        catalog_id (str):
        bbox (Union[Unset, list[float]]):
        datetime_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10.
        q (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        external_id (Union[Unset, list[str]]):
        ids (Union[Unset, list[str]]):
        sortby (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, GetRecordsResponse200]
    """

    return (
        await asyncio_detailed(
            catalog_id=catalog_id,
            client=client,
            bbox=bbox,
            datetime_=datetime_,
            limit=limit,
            q=q,
            type_=type_,
            external_id=external_id,
            ids=ids,
            sortby=sortby,
        )
    ).parsed
