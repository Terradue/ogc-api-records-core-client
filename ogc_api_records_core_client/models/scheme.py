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
    from ..models.scheme_resolver import SchemeResolver


T = TypeVar("T", bound="Scheme")


@_attrs_define
class Scheme:
    """
    Attributes:
        scheme_id (str): An identifier for this namespace.  The identifier can be used as a short-form for the
            namespace.
        namespace (str): A declarative region that provides a scope to the identifiers inside it. It is recommended that
            the value of namespace be a URI.
        resolver (Union[Unset, SchemeResolver]): An extensible description of a mechanism that resolves a scheme
            identifier (scheme-id) to its namespace.
    """

    scheme_id: str
    namespace: str
    resolver: Union[Unset, "SchemeResolver"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheme_id = self.scheme_id

        namespace = self.namespace

        resolver: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resolver, Unset):
            resolver = self.resolver.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheme-id": scheme_id,
                "namespace": namespace,
            }
        )
        if resolver is not UNSET:
            field_dict["resolver"] = resolver

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheme_resolver import SchemeResolver

        d = dict(src_dict)
        scheme_id = d.pop("scheme-id")

        namespace = d.pop("namespace")

        _resolver = d.pop("resolver", UNSET)
        resolver: Union[Unset, SchemeResolver]
        if isinstance(_resolver, Unset):
            resolver = UNSET
        else:
            resolver = SchemeResolver.from_dict(_resolver)

        scheme = cls(
            scheme_id=scheme_id,
            namespace=namespace,
            resolver=resolver,
        )

        scheme.additional_properties = d
        return scheme

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
