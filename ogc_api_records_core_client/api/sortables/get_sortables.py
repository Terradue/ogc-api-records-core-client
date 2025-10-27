from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.get_sortables_response_200 import GetSortablesResponse200
from ...types import Response


def _get_kwargs(
    catalog_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections/{catalog_id}/sortables".format(
            catalog_id=catalog_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Exception_, GetSortablesResponse200]]:
    if response.status_code == 200:
        response_200 = GetSortablesResponse200.from_dict(response.json())

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
) -> Response[Union[Exception_, GetSortablesResponse200]]:
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
) -> Response[Union[Exception_, GetSortablesResponse200]]:
    """get the list of sortable properties

     Fetch the list of properties which can be used to sort the getRecords
    response.

    Args:
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, GetSortablesResponse200]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Exception_, GetSortablesResponse200]]:
    """get the list of sortable properties

     Fetch the list of properties which can be used to sort the getRecords
    response.

    Args:
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, GetSortablesResponse200]
    """

    return sync_detailed(
        catalog_id=catalog_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Exception_, GetSortablesResponse200]]:
    """get the list of sortable properties

     Fetch the list of properties which can be used to sort the getRecords
    response.

    Args:
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Exception_, GetSortablesResponse200]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Exception_, GetSortablesResponse200]]:
    """get the list of sortable properties

     Fetch the list of properties which can be used to sort the getRecords
    response.

    Args:
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Exception_, GetSortablesResponse200]
    """

    return (
        await asyncio_detailed(
            catalog_id=catalog_id,
            client=client,
        )
    ).parsed
