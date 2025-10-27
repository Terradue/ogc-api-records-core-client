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
    from ..models.extent_spatial import ExtentSpatial
    from ..models.extent_temporal import ExtentTemporal


T = TypeVar("T", bound="Extent")


@_attrs_define
class Extent:
    """The extent of the features in the collection. In the Core only spatial and temporal extents are specified.
    Extensions may add additional members to represent other extents, for example, thermal or pressure ranges.
    An array of extents is provided for each extent type (spatial, temporal). The first item in the array describes the
    overall extent of the data. All subsequent items describe more precise extents, e.g., to identify clusters of data.
    Clients only interested in the overall extent will only need to access the first extent in the array.

        Attributes:
            spatial (Union[Unset, ExtentSpatial]): The spatial extent of the features in the collection.
            temporal (Union[Unset, ExtentTemporal]): The temporal extent of the features in the collection.
    """

    spatial: Union[Unset, "ExtentSpatial"] = UNSET
    temporal: Union[Unset, "ExtentTemporal"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spatial: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spatial, Unset):
            spatial = self.spatial.to_dict()

        temporal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal, Unset):
            temporal = self.temporal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spatial is not UNSET:
            field_dict["spatial"] = spatial
        if temporal is not UNSET:
            field_dict["temporal"] = temporal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extent_spatial import ExtentSpatial
        from ..models.extent_temporal import ExtentTemporal

        d = dict(src_dict)
        _spatial = d.pop("spatial", UNSET)
        spatial: Union[Unset, ExtentSpatial]
        if isinstance(_spatial, Unset):
            spatial = UNSET
        else:
            spatial = ExtentSpatial.from_dict(_spatial)

        _temporal = d.pop("temporal", UNSET)
        temporal: Union[Unset, ExtentTemporal]
        if isinstance(_temporal, Unset):
            temporal = UNSET
        else:
            temporal = ExtentTemporal.from_dict(_temporal)

        extent = cls(
            spatial=spatial,
            temporal=temporal,
        )

        extent.additional_properties = d
        return extent

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
