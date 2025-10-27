from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extent_spatial_crs import ExtentSpatialCrs
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtentSpatial")


@_attrs_define
class ExtentSpatial:
    """The spatial extent of the features in the collection.

    Attributes:
        bbox (Union[Unset, list[Any]]): One or more bounding boxes that describe the spatial extent
            of the dataset.  In the Core only a single bounding box is
            supported.

            Extensions may support additional areas.
            The first bounding box describes the overall spatial
            extent of the data. All subsequent bounding boxes describe
            more precise bounding boxes, e.g., to identify clusters of data.
            Clients only interested in the overall spatial extent will
            only need to access the first bounding box in the array.
        crs (Union[Unset, ExtentSpatialCrs]): Coordinate reference system of the coordinates in the spatial extent
            (property `bbox`). The default reference system is WGS 84 longitude/latitude. In the Core the only other
            supported coordinate reference system is WGS 84 longitude/latitude/ ellipsoidal height for coordinates with
            height. Extensions may support additional coordinate reference systems and add additional enum values. Default:
            ExtentSpatialCrs.HTTPWWW_OPENGIS_NETDEFCRSOGC1_3CRS84.
    """

    bbox: Union[Unset, list[Any]] = UNSET
    crs: Union[Unset, ExtentSpatialCrs] = (
        ExtentSpatialCrs.HTTPWWW_OPENGIS_NETDEFCRSOGC1_3CRS84
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbox: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = []
            for bbox_item_data in self.bbox:
                bbox_item: Any
                bbox_item = bbox_item_data
                bbox.append(bbox_item)

        crs: Union[Unset, str] = UNSET
        if not isinstance(self.crs, Unset):
            crs = self.crs.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if crs is not UNSET:
            field_dict["crs"] = crs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bbox = []
        _bbox = d.pop("bbox", UNSET)
        for bbox_item_data in _bbox or []:

            def _parse_bbox_item(data: object) -> Any:
                return cast(Any, data)

            bbox_item = _parse_bbox_item(bbox_item_data)

            bbox.append(bbox_item)

        _crs = d.pop("crs", UNSET)
        crs: Union[Unset, ExtentSpatialCrs]
        if isinstance(_crs, Unset):
            crs = UNSET
        else:
            crs = ExtentSpatialCrs(_crs)

        extent_spatial = cls(
            bbox=bbox,
            crs=crs,
        )

        extent_spatial.additional_properties = d
        return extent_spatial

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
