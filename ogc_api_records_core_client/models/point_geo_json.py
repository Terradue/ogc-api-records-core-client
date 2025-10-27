from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.point_geo_json_type import PointGeoJSONType

T = TypeVar("T", bound="PointGeoJSON")


@_attrs_define
class PointGeoJSON:
    """
    Attributes:
        type_ (PointGeoJSONType):
        coordinates (list[float]):
    """

    type_: PointGeoJSONType
    coordinates: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        coordinates = self.coordinates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "coordinates": coordinates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PointGeoJSONType(d.pop("type"))

        coordinates = cast(list[float], d.pop("coordinates"))

        point_geo_json = cls(
            type_=type_,
            coordinates=coordinates,
        )

        point_geo_json.additional_properties = d
        return point_geo_json

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
