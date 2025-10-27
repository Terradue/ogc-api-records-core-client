from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.theme_concepts_item import ThemeConceptsItem


T = TypeVar("T", bound="Theme")


@_attrs_define
class Theme:
    """
    Attributes:
        concepts (list['ThemeConceptsItem']): One or more entity/concept identifiers from this knowledge system. it is
            recommended that a resolvable URI be used for each entity/concept identifier.
        scheme (str): An identifier for the knowledge organization system used to classify the resource.  It is
            recommended that the identifier be a resolvable URI.  The list of schemes used in a searchable catalog can be
            determined by inspecting the server's OpenAPI document or, if the server implements CQL2, by exposing a
            queryable (e.g. named `scheme`) and enumerating the list of schemes in the queryable's schema definition.
    """

    concepts: list["ThemeConceptsItem"]
    scheme: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concepts = []
        for concepts_item_data in self.concepts:
            concepts_item = concepts_item_data.to_dict()
            concepts.append(concepts_item)

        scheme = self.scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "concepts": concepts,
                "scheme": scheme,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_concepts_item import ThemeConceptsItem

        d = dict(src_dict)
        concepts = []
        _concepts = d.pop("concepts")
        for concepts_item_data in _concepts:
            concepts_item = ThemeConceptsItem.from_dict(concepts_item_data)

            concepts.append(concepts_item)

        scheme = d.pop("scheme")

        theme = cls(
            concepts=concepts,
            scheme=scheme,
        )

        theme.additional_properties = d
        return theme

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
