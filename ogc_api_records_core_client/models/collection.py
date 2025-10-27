from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extent import Extent
    from ..models.link import Link


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """
    Attributes:
        id (str): identifier of the collection used, for example, in URIs
        links (list['Link']):
        title (Union[Unset, str]): human readable title of the collection
        description (Union[Unset, str]): a description of the features in the collection
        extent (Union[Unset, Extent]): The extent of the features in the collection. In the Core only spatial and
            temporal extents are specified. Extensions may add additional members to represent other extents, for example,
            thermal or pressure ranges.
            An array of extents is provided for each extent type (spatial, temporal). The first item in the array describes
            the overall extent of the data. All subsequent items describe more precise extents, e.g., to identify clusters
            of data. Clients only interested in the overall extent will only need to access the first extent in the array.
        item_type (Union[Unset, str]): indicator about the type of the items in the collection (the default value is
            'feature'). Default: 'feature'.
        crs (Union[Unset, list[str]]): the list of coordinate reference systems supported by the service
    """

    id: str
    links: list["Link"]
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    extent: Union[Unset, "Extent"] = UNSET
    item_type: Union[Unset, str] = "feature"
    crs: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        title = self.title

        description = self.description

        extent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extent, Unset):
            extent = self.extent.to_dict()

        item_type = self.item_type

        crs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.crs, Unset):
            crs = self.crs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "links": links,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if extent is not UNSET:
            field_dict["extent"] = extent
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if crs is not UNSET:
            field_dict["crs"] = crs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extent import Extent
        from ..models.link import Link

        d = dict(src_dict)
        id = d.pop("id")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _extent = d.pop("extent", UNSET)
        extent: Union[Unset, Extent]
        if isinstance(_extent, Unset):
            extent = UNSET
        else:
            extent = Extent.from_dict(_extent)

        item_type = d.pop("itemType", UNSET)

        crs = cast(list[str], d.pop("crs", UNSET))

        collection = cls(
            id=id,
            links=links,
            title=title,
            description=description,
            extent=extent,
            item_type=item_type,
            crs=crs,
        )

        collection.additional_properties = d
        return collection

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
