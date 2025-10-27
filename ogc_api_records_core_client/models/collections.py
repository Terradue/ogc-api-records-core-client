from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.link import Link


T = TypeVar("T", bound="Collections")


@_attrs_define
class Collections:
    """
    Attributes:
        links (list['Link']):
        collections (list['Collection']):
    """

    links: list["Link"]
    collections: list["Collection"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "collections": collections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.link import Link

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        collections = cls(
            links=links,
            collections=collections,
        )

        collections.additional_properties = d
        return collections

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
