import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        href (str):
        rel (Union[Unset, str]): The type or semantics of the relation.
        type_ (Union[Unset, str]): A hint indicating what the media type of the result of dereferencing the link should
            be.
        hreflang (Union[Unset, str]): A hint indicating what the language of the result of dereferencing the link should
            be.
        title (Union[Unset, str]): Used to label the destination of a link such that it can be used as a human-readable
            identifier.
        length (Union[Unset, int]):
        created (Union[Unset, datetime.datetime]): Date of creation of the resource pointed to by the link.
        updated (Union[Unset, datetime.datetime]): Most recent date on which the resource pointed to by the link was
            changed.
    """

    href: str
    rel: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    hreflang: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    length: Union[Unset, int] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        rel = self.rel

        type_ = self.type_

        hreflang = self.hreflang

        title = self.title

        length = self.length

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )
        if rel is not UNSET:
            field_dict["rel"] = rel
        if type_ is not UNSET:
            field_dict["type"] = type_
        if hreflang is not UNSET:
            field_dict["hreflang"] = hreflang
        if title is not UNSET:
            field_dict["title"] = title
        if length is not UNSET:
            field_dict["length"] = length
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        rel = d.pop("rel", UNSET)

        type_ = d.pop("type", UNSET)

        hreflang = d.pop("hreflang", UNSET)

        title = d.pop("title", UNSET)

        length = d.pop("length", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        link = cls(
            href=href,
            rel=rel,
            type_=type_,
            hreflang=hreflang,
            title=title,
            length=length,
            created=created,
            updated=updated,
        )

        link.additional_properties = d
        return link

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
