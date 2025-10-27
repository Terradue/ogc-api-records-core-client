from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.link_template import LinkTemplate


T = TypeVar("T", bound="LandingPage")


@_attrs_define
class LandingPage:
    """
    Attributes:
        links (list['Link']):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        link_templates (Union[Unset, list['LinkTemplate']]):
    """

    links: list["Link"]
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    link_templates: Union[Unset, list["LinkTemplate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        title = self.title

        description = self.description

        link_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.link_templates, Unset):
            link_templates = []
            for link_templates_item_data in self.link_templates:
                link_templates_item = link_templates_item_data.to_dict()
                link_templates.append(link_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if link_templates is not UNSET:
            field_dict["linkTemplates"] = link_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link
        from ..models.link_template import LinkTemplate

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        link_templates = []
        _link_templates = d.pop("linkTemplates", UNSET)
        for link_templates_item_data in _link_templates or []:
            link_templates_item = LinkTemplate.from_dict(link_templates_item_data)

            link_templates.append(link_templates_item)

        landing_page = cls(
            links=links,
            title=title,
            description=description,
            link_templates=link_templates,
        )

        landing_page.additional_properties = d
        return landing_page

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
