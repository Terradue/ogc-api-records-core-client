import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.extent_temporal_trs import ExtentTemporalTrs
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtentTemporal")


@_attrs_define
class ExtentTemporal:
    """The temporal extent of the features in the collection.

    Attributes:
        interval (Union[Unset, list[list[Union[None, datetime.datetime]]]]): One or more time intervals that describe
            the temporal extent of the dataset. In the Core only a single time interval is supported.
            Extensions may support multiple intervals. The first time interval describes the overall temporal extent of the
            data. All subsequent time intervals describe more precise time intervals, e.g., to identify clusters of data.
            Clients only interested in the overall temporal extent will only need to access the first time interval in the
            array (a pair of lower and upper bound instants).
        trs (Union[Unset, ExtentTemporalTrs]): Coordinate reference system of the coordinates in the temporal
            extent (property `interval`). The default reference system is
            the Gregorian calendar. In the Core this is the only supported
            temporal coordinate reference system. Extensions may support
            additional temporal coordinate reference systems and add
            additional enum values. Default: ExtentTemporalTrs.HTTPWWW_OPENGIS_NETDEFUOMISO_86010GREGORIAN.
    """

    interval: Union[Unset, list[list[Union[None, datetime.datetime]]]] = UNSET
    trs: Union[Unset, ExtentTemporalTrs] = (
        ExtentTemporalTrs.HTTPWWW_OPENGIS_NETDEFUOMISO_86010GREGORIAN
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval: Union[Unset, list[list[Union[None, str]]]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = []
            for interval_item_data in self.interval:
                interval_item = []
                for interval_item_item_data in interval_item_data:
                    interval_item_item: Union[None, str]
                    if isinstance(interval_item_item_data, datetime.datetime):
                        interval_item_item = interval_item_item_data.isoformat()
                    else:
                        interval_item_item = interval_item_item_data
                    interval_item.append(interval_item_item)

                interval.append(interval_item)

        trs: Union[Unset, str] = UNSET
        if not isinstance(self.trs, Unset):
            trs = self.trs.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if trs is not UNSET:
            field_dict["trs"] = trs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = []
        _interval = d.pop("interval", UNSET)
        for interval_item_data in _interval or []:
            interval_item = []
            _interval_item = interval_item_data
            for interval_item_item_data in _interval_item:

                def _parse_interval_item_item(
                    data: object,
                ) -> Union[None, datetime.datetime]:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, str):
                            raise TypeError()
                        interval_item_item_type_0 = isoparse(data)

                        return interval_item_item_type_0
                    except:  # noqa: E722
                        pass
                    return cast(Union[None, datetime.datetime], data)

                interval_item_item = _parse_interval_item_item(interval_item_item_data)

                interval_item.append(interval_item_item)

            interval.append(interval_item)

        _trs = d.pop("trs", UNSET)
        trs: Union[Unset, ExtentTemporalTrs]
        if isinstance(_trs, Unset):
            trs = UNSET
        else:
            trs = ExtentTemporalTrs(_trs)

        extent_temporal = cls(
            interval=interval,
            trs=trs,
        )

        extent_temporal.additional_properties = d
        return extent_temporal

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
