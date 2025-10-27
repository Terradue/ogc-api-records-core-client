import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.feature_collection_geo_json_type import FeatureCollectionGeoJSONType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_geo_json import FeatureGeoJSON
    from ..models.link import Link
    from ..models.link_template import LinkTemplate


T = TypeVar("T", bound="GetRecordsResponse200")


@_attrs_define
class GetRecordsResponse200:
    """
    Attributes:
        type_ (FeatureCollectionGeoJSONType):
        features (list['FeatureGeoJSON']):
        links (Union[Unset, list['Link']]):
        link_templates (Union[Unset, list['LinkTemplate']]):
        time_stamp (Union[Unset, datetime.datetime]):
        number_matched (Union[Unset, int]):
        number_returned (Union[Unset, int]):
    """

    type_: FeatureCollectionGeoJSONType
    features: list["FeatureGeoJSON"]
    links: Union[Unset, list["Link"]] = UNSET
    link_templates: Union[Unset, list["LinkTemplate"]] = UNSET
    time_stamp: Union[Unset, datetime.datetime] = UNSET
    number_matched: Union[Unset, int] = UNSET
    number_returned: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        features = []
        for features_item_data in self.features:
            features_item = features_item_data.to_dict()
            features.append(features_item)

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

        time_stamp: Union[Unset, str] = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        number_matched = self.number_matched

        number_returned = self.number_returned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "features": features,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if link_templates is not UNSET:
            field_dict["linkTemplates"] = link_templates
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if number_matched is not UNSET:
            field_dict["numberMatched"] = number_matched
        if number_returned is not UNSET:
            field_dict["numberReturned"] = number_returned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_geo_json import FeatureGeoJSON
        from ..models.link import Link
        from ..models.link_template import LinkTemplate

        d = dict(src_dict)
        type_ = FeatureCollectionGeoJSONType(d.pop("type"))

        features = []
        _features = d.pop("features")
        for features_item_data in _features:
            features_item = FeatureGeoJSON.from_dict(features_item_data)

            features.append(features_item)

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

        _time_stamp = d.pop("timeStamp", UNSET)
        time_stamp: Union[Unset, datetime.datetime]
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = isoparse(_time_stamp)

        number_matched = d.pop("numberMatched", UNSET)

        number_returned = d.pop("numberReturned", UNSET)

        get_records_response_200 = cls(
            type_=type_,
            features=features,
            links=links,
            link_templates=link_templates,
            time_stamp=time_stamp,
            number_matched=number_matched,
            number_returned=number_returned,
        )

        get_records_response_200.additional_properties = d
        return get_records_response_200

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
