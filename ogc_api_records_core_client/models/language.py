from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.language_dir import LanguageDir
from ..types import UNSET, Unset

T = TypeVar("T", bound="Language")


@_attrs_define
class Language:
    """The language used for textual values in this record.

    Attributes:
        code (str): The language tag as per RFC-5646.
        name (Union[Unset, str]): The untranslated name of the language.
        alternate (Union[Unset, str]): The name of the language in another well-understood language, usually English.
        dir_ (Union[Unset, LanguageDir]): The direction for text in this language. The default, `ltr` (left-to-right),
            represents the most common situation. However, care should be taken to set the value of `dir` appropriately if
            the language direction is not `ltr`. Other values supported are `rtl` (right-to-left), `ttb` (top-to-bottom),
            and `btt` (bottom-to-top). Default: LanguageDir.LTR.
    """

    code: str
    name: Union[Unset, str] = UNSET
    alternate: Union[Unset, str] = UNSET
    dir_: Union[Unset, LanguageDir] = LanguageDir.LTR
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        alternate = self.alternate

        dir_: Union[Unset, str] = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if alternate is not UNSET:
            field_dict["alternate"] = alternate
        if dir_ is not UNSET:
            field_dict["dir"] = dir_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name", UNSET)

        alternate = d.pop("alternate", UNSET)

        _dir_ = d.pop("dir", UNSET)
        dir_: Union[Unset, LanguageDir]
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = LanguageDir(_dir_)

        language = cls(
            code=code,
            name=name,
            alternate=alternate,
            dir_=dir_,
        )

        language.additional_properties = d
        return language

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
