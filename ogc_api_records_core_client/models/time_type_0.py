from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_type_0_interval_item_type_2 import TimeType0IntervalItemType2
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeType0")


@_attrs_define
class TimeType0:
    """
    Attributes:
        date (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        interval (Union[Unset, list[Union[TimeType0IntervalItemType2, str]]]):
        resolution (Union[Unset, str]): Minimum time period resolvable in the dataset, as an ISO 8601 duration.
    """

    date: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    interval: Union[Unset, list[Union[TimeType0IntervalItemType2, str]]] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        timestamp = self.timestamp

        interval: Union[Unset, list[str]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = []
            for interval_item_data in self.interval:
                interval_item: str
                if isinstance(interval_item_data, TimeType0IntervalItemType2):
                    interval_item = interval_item_data.value
                else:
                    interval_item = interval_item_data
                interval.append(interval_item)

        resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if interval is not UNSET:
            field_dict["interval"] = interval
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        interval = []
        _interval = d.pop("interval", UNSET)
        for interval_item_data in _interval or []:

            def _parse_interval_item(
                data: object,
            ) -> Union[TimeType0IntervalItemType2, str]:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    interval_item_type_2 = TimeType0IntervalItemType2(data)

                    return interval_item_type_2
                except:  # noqa: E722
                    pass
                return cast(Union[TimeType0IntervalItemType2, str], data)

            interval_item = _parse_interval_item(interval_item_data)

            interval.append(interval_item)

        resolution = d.pop("resolution", UNSET)

        time_type_0 = cls(
            date=date,
            timestamp=timestamp,
            interval=interval,
            resolution=resolution,
        )

        time_type_0.additional_properties = d
        return time_type_0

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
