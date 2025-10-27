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

from ..models.record_geo_json_type import RecordGeoJSONType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geometrycollection_geo_json import GeometrycollectionGeoJSON
    from ..models.linestring_geo_json import LinestringGeoJSON
    from ..models.link import Link
    from ..models.link_template import LinkTemplate
    from ..models.multilinestring_geo_json import MultilinestringGeoJSON
    from ..models.multipoint_geo_json import MultipointGeoJSON
    from ..models.multipolygon_geo_json import MultipolygonGeoJSON
    from ..models.point_geo_json import PointGeoJSON
    from ..models.polygon_geo_json import PolygonGeoJSON
    from ..models.record_geo_json_properties import RecordGeoJSONProperties
    from ..models.time_type_0 import TimeType0


T = TypeVar("T", bound="RecordGeoJSON")


@_attrs_define
class RecordGeoJSON:
    """
    Attributes:
        id (str): A unique identifier of the catalog record.
        type_ (RecordGeoJSONType):
        geometry (Union['GeometrycollectionGeoJSON', 'LinestringGeoJSON', 'MultilinestringGeoJSON', 'MultipointGeoJSON',
            'MultipolygonGeoJSON', 'PointGeoJSON', 'PolygonGeoJSON', None]):
        properties (RecordGeoJSONProperties):
        time (Union['TimeType0', None, Unset]):
        conforms_to (Union[Unset, list[str]]): The extensions/conformance classes used in this record.
        links (Union[Unset, list['Link']]):
        link_templates (Union[Unset, list['LinkTemplate']]):
    """

    id: str
    type_: RecordGeoJSONType
    geometry: Union[
        "GeometrycollectionGeoJSON",
        "LinestringGeoJSON",
        "MultilinestringGeoJSON",
        "MultipointGeoJSON",
        "MultipolygonGeoJSON",
        "PointGeoJSON",
        "PolygonGeoJSON",
        None,
    ]
    properties: "RecordGeoJSONProperties"
    time: Union["TimeType0", None, Unset] = UNSET
    conforms_to: Union[Unset, list[str]] = UNSET
    links: Union[Unset, list["Link"]] = UNSET
    link_templates: Union[Unset, list["LinkTemplate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.geometrycollection_geo_json import GeometrycollectionGeoJSON
        from ..models.linestring_geo_json import LinestringGeoJSON
        from ..models.multilinestring_geo_json import MultilinestringGeoJSON
        from ..models.multipoint_geo_json import MultipointGeoJSON
        from ..models.multipolygon_geo_json import MultipolygonGeoJSON
        from ..models.point_geo_json import PointGeoJSON
        from ..models.polygon_geo_json import PolygonGeoJSON
        from ..models.time_type_0 import TimeType0

        id = self.id

        type_ = self.type_.value

        geometry: Union[None, dict[str, Any]]
        if isinstance(self.geometry, PointGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, MultipointGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, LinestringGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, MultilinestringGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, PolygonGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, MultipolygonGeoJSON):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, GeometrycollectionGeoJSON):
            geometry = self.geometry.to_dict()
        else:
            geometry = self.geometry

        properties = self.properties.to_dict()

        time: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, TimeType0):
            time = self.time.to_dict()
        else:
            time = self.time

        conforms_to: Union[Unset, list[str]] = UNSET
        if not isinstance(self.conforms_to, Unset):
            conforms_to = self.conforms_to

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

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
                "id": id,
                "type": type_,
                "geometry": geometry,
                "properties": properties,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time
        if conforms_to is not UNSET:
            field_dict["conformsTo"] = conforms_to
        if links is not UNSET:
            field_dict["links"] = links
        if link_templates is not UNSET:
            field_dict["linkTemplates"] = link_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geometrycollection_geo_json import GeometrycollectionGeoJSON
        from ..models.linestring_geo_json import LinestringGeoJSON
        from ..models.link import Link
        from ..models.link_template import LinkTemplate
        from ..models.multilinestring_geo_json import MultilinestringGeoJSON
        from ..models.multipoint_geo_json import MultipointGeoJSON
        from ..models.multipolygon_geo_json import MultipolygonGeoJSON
        from ..models.point_geo_json import PointGeoJSON
        from ..models.polygon_geo_json import PolygonGeoJSON
        from ..models.record_geo_json_properties import RecordGeoJSONProperties
        from ..models.time_type_0 import TimeType0

        d = dict(src_dict)
        id = d.pop("id")

        type_ = RecordGeoJSONType(d.pop("type"))

        def _parse_geometry(
            data: object,
        ) -> Union[
            "GeometrycollectionGeoJSON",
            "LinestringGeoJSON",
            "MultilinestringGeoJSON",
            "MultipointGeoJSON",
            "MultipolygonGeoJSON",
            "PointGeoJSON",
            "PolygonGeoJSON",
            None,
        ]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasgeometry_geo_json_type_0 = PointGeoJSON.from_dict(data)

                return componentsschemasgeometry_geo_json_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasgeometry_geo_json_type_1 = MultipointGeoJSON.from_dict(
                    data
                )

                return componentsschemasgeometry_geo_json_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasgeometry_geo_json_type_2 = LinestringGeoJSON.from_dict(
                    data
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
                componentsschemasgeometry_geo_json_type_4 = PolygonGeoJSON.from_dict(
                    data
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasgeometry_geo_json_type_6 = (
                    GeometrycollectionGeoJSON.from_dict(data)
                )

                return componentsschemasgeometry_geo_json_type_6
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "GeometrycollectionGeoJSON",
                    "LinestringGeoJSON",
                    "MultilinestringGeoJSON",
                    "MultipointGeoJSON",
                    "MultipolygonGeoJSON",
                    "PointGeoJSON",
                    "PolygonGeoJSON",
                    None,
                ],
                data,
            )

        geometry = _parse_geometry(d.pop("geometry"))

        properties = RecordGeoJSONProperties.from_dict(d.pop("properties"))

        def _parse_time(data: object) -> Union["TimeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemastime_type_0 = TimeType0.from_dict(data)

                return componentsschemastime_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TimeType0", None, Unset], data)

        time = _parse_time(d.pop("time", UNSET))

        conforms_to = cast(list[str], d.pop("conformsTo", UNSET))

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        link_templates = []
        _link_templates = d.pop("linkTemplates", UNSET)
        for link_templates_item_data in _link_templates or []:
            link_templates_item = LinkTemplate.from_dict(link_templates_item_data)

            link_templates.append(link_templates_item)

        record_geo_json = cls(
            id=id,
            type_=type_,
            geometry=geometry,
            properties=properties,
            time=time,
            conforms_to=conforms_to,
            links=links,
            link_templates=link_templates,
        )

        record_geo_json.additional_properties = d
        return record_geo_json

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
