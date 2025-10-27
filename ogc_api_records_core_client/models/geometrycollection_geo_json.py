from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geometrycollection_geo_json_type import GeometrycollectionGeoJSONType

if TYPE_CHECKING:
    from ..models.linestring_geo_json import LinestringGeoJSON
    from ..models.multilinestring_geo_json import MultilinestringGeoJSON
    from ..models.multipoint_geo_json import MultipointGeoJSON
    from ..models.multipolygon_geo_json import MultipolygonGeoJSON
    from ..models.point_geo_json import PointGeoJSON
    from ..models.polygon_geo_json import PolygonGeoJSON


T = TypeVar("T", bound="GeometrycollectionGeoJSON")


@_attrs_define
class GeometrycollectionGeoJSON:
    """
    Attributes:
        type_ (GeometrycollectionGeoJSONType):
        geometries (list[Union['GeometrycollectionGeoJSON', 'LinestringGeoJSON', 'MultilinestringGeoJSON',
            'MultipointGeoJSON', 'MultipolygonGeoJSON', 'PointGeoJSON', 'PolygonGeoJSON']]):
    """

    type_: GeometrycollectionGeoJSONType
    geometries: list[
        Union[
            "GeometrycollectionGeoJSON",
            "LinestringGeoJSON",
            "MultilinestringGeoJSON",
            "MultipointGeoJSON",
            "MultipolygonGeoJSON",
            "PointGeoJSON",
            "PolygonGeoJSON",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.linestring_geo_json import LinestringGeoJSON
        from ..models.multilinestring_geo_json import MultilinestringGeoJSON
        from ..models.multipoint_geo_json import MultipointGeoJSON
        from ..models.multipolygon_geo_json import MultipolygonGeoJSON
        from ..models.point_geo_json import PointGeoJSON
        from ..models.polygon_geo_json import PolygonGeoJSON

        type_ = self.type_.value

        geometries = []
        for geometries_item_data in self.geometries:
            geometries_item: dict[str, Any]
            if isinstance(geometries_item_data, PointGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            elif isinstance(geometries_item_data, MultipointGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            elif isinstance(geometries_item_data, LinestringGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            elif isinstance(geometries_item_data, MultilinestringGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            elif isinstance(geometries_item_data, PolygonGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            elif isinstance(geometries_item_data, MultipolygonGeoJSON):
                geometries_item = geometries_item_data.to_dict()
            else:
                geometries_item = geometries_item_data.to_dict()

            geometries.append(geometries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "geometries": geometries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linestring_geo_json import LinestringGeoJSON
        from ..models.multilinestring_geo_json import MultilinestringGeoJSON
        from ..models.multipoint_geo_json import MultipointGeoJSON
        from ..models.multipolygon_geo_json import MultipolygonGeoJSON
        from ..models.point_geo_json import PointGeoJSON
        from ..models.polygon_geo_json import PolygonGeoJSON

        d = dict(src_dict)
        type_ = GeometrycollectionGeoJSONType(d.pop("type"))

        geometries = []
        _geometries = d.pop("geometries")
        for geometries_item_data in _geometries:

            def _parse_geometries_item(
                data: object,
            ) -> Union[
                "GeometrycollectionGeoJSON",
                "LinestringGeoJSON",
                "MultilinestringGeoJSON",
                "MultipointGeoJSON",
                "MultipolygonGeoJSON",
                "PointGeoJSON",
                "PolygonGeoJSON",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_0 = PointGeoJSON.from_dict(
                        data
                    )

                    return componentsschemasgeometry_geo_json_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_1 = (
                        MultipointGeoJSON.from_dict(data)
                    )

                    return componentsschemasgeometry_geo_json_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_2 = (
                        LinestringGeoJSON.from_dict(data)
                    )

                    return componentsschemasgeometry_geo_json_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_3 = (
                        MultilinestringGeoJSON.from_dict(data)
                    )

                    return componentsschemasgeometry_geo_json_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_4 = (
                        PolygonGeoJSON.from_dict(data)
                    )

                    return componentsschemasgeometry_geo_json_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasgeometry_geo_json_type_5 = (
                        MultipolygonGeoJSON.from_dict(data)
                    )

                    return componentsschemasgeometry_geo_json_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasgeometry_geo_json_type_6 = (
                    GeometrycollectionGeoJSON.from_dict(data)
                )

                return componentsschemasgeometry_geo_json_type_6

            geometries_item = _parse_geometries_item(geometries_item_data)

            geometries.append(geometries_item)

        geometrycollection_geo_json = cls(
            type_=type_,
            geometries=geometries,
        )

        geometrycollection_geo_json.additional_properties = d
        return geometrycollection_geo_json

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
