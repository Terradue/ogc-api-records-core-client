import datetime
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
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language
    from ..models.record_common_properties_external_ids_item import (
        RecordCommonPropertiesExternalIdsItem,
    )
    from ..models.theme import Theme


T = TypeVar("T", bound="RecordGeoJSONProperties")


@_attrs_define
class RecordGeoJSONProperties:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]): The date this record was created in the server.
        updated (Union[Unset, datetime.datetime]): The most recent date on which the record was changed.
        type_ (Union[Unset, str]): The nature or genre of the resource. The value should be a code, convenient for
            filtering records. Where available, a link to the canonical URI of the record type resource will be added to the
            'links' property.
        title (Union[Unset, str]): A human-readable name given to the resource.
        description (Union[Unset, str]): A free-text account of the resource.
        keywords (Union[Unset, list[str]]): The topic or topics of the resource. Typically represented using free-form
            keywords, tags, key phrases, or classification codes.
        themes (Union[Unset, list['Theme']]): A knowledge organization system used to classify the resource.
        language (Union[Unset, Language]): The language used for textual values in this record.
        languages (Union[Unset, list['Language']]): This list of languages in which this record is available.
        resource_languages (Union[Unset, list['Language']]): The list of languages in which the resource described by
            this record is available.
        external_ids (Union[Unset, list['RecordCommonPropertiesExternalIdsItem']]): An identifier for the resource
            assigned by an external (to the catalog) entity.
        formats (Union[Unset, list[Any]]): A list of available distributions of the resource.
        contacts (Union[Unset, list[Any]]): A list of contacts qualified by their role(s) in association to the record
            or the resource described by the record.
        license_ (Union[Unset, str]): A legal document under which the resource is made available. If the resource is
            being made available under a common license then use an SPDX license id (https://spdx.org/licenses/). If the
            resource is being made available under multiple common licenses then use an SPDX license expression v2.3 string
            (https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) If the resource is being made available under
            one or more licenses that haven't been assigned an SPDX identifier or one or more custom licenses then use a
            string value of 'other' and include one or more links (rel="license") in the `link` section of the record to the
            file(s) that contains the text of the license(s). There is also the case of a resource that is private or
            unpublished and is thus unlicensed; in this case do not register such a resource in the catalog in the first
            place since there is no point in making such a resource discoverable.
        rights (Union[Unset, str]): A statement that concerns all rights not addressed by the license such as a
            copyright statement.
    """

    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    themes: Union[Unset, list["Theme"]] = UNSET
    language: Union[Unset, "Language"] = UNSET
    languages: Union[Unset, list["Language"]] = UNSET
    resource_languages: Union[Unset, list["Language"]] = UNSET
    external_ids: Union[Unset, list["RecordCommonPropertiesExternalIdsItem"]] = UNSET
    formats: Union[Unset, list[Any]] = UNSET
    contacts: Union[Unset, list[Any]] = UNSET
    license_: Union[Unset, str] = UNSET
    rights: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        type_ = self.type_

        title = self.title

        description = self.description

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        themes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.themes, Unset):
            themes = []
            for themes_item_data in self.themes:
                themes_item = themes_item_data.to_dict()
                themes.append(themes_item)

        language: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        languages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)

        resource_languages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resource_languages, Unset):
            resource_languages = []
            for resource_languages_item_data in self.resource_languages:
                resource_languages_item = resource_languages_item_data.to_dict()
                resource_languages.append(resource_languages_item)

        external_ids: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = []
            for external_ids_item_data in self.external_ids:
                external_ids_item = external_ids_item_data.to_dict()
                external_ids.append(external_ids_item)

        formats: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.formats, Unset):
            formats = []
            for formats_item_data in self.formats:
                formats_item: Any
                formats_item = formats_item_data
                formats.append(formats_item)

        contacts: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item: Any
                contacts_item = contacts_item_data
                contacts.append(contacts_item)

        license_ = self.license_

        rights = self.rights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if themes is not UNSET:
            field_dict["themes"] = themes
        if language is not UNSET:
            field_dict["language"] = language
        if languages is not UNSET:
            field_dict["languages"] = languages
        if resource_languages is not UNSET:
            field_dict["resourceLanguages"] = resource_languages
        if external_ids is not UNSET:
            field_dict["externalIds"] = external_ids
        if formats is not UNSET:
            field_dict["formats"] = formats
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if license_ is not UNSET:
            field_dict["license"] = license_
        if rights is not UNSET:
            field_dict["rights"] = rights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language import Language
        from ..models.record_common_properties_external_ids_item import (
            RecordCommonPropertiesExternalIdsItem,
        )
        from ..models.theme import Theme

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        themes = []
        _themes = d.pop("themes", UNSET)
        for themes_item_data in _themes or []:
            themes_item = Theme.from_dict(themes_item_data)

            themes.append(themes_item)

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language.from_dict(_language)

        languages = []
        _languages = d.pop("languages", UNSET)
        for languages_item_data in _languages or []:
            languages_item = Language.from_dict(languages_item_data)

            languages.append(languages_item)

        resource_languages = []
        _resource_languages = d.pop("resourceLanguages", UNSET)
        for resource_languages_item_data in _resource_languages or []:
            resource_languages_item = Language.from_dict(resource_languages_item_data)

            resource_languages.append(resource_languages_item)

        external_ids = []
        _external_ids = d.pop("externalIds", UNSET)
        for external_ids_item_data in _external_ids or []:
            external_ids_item = RecordCommonPropertiesExternalIdsItem.from_dict(
                external_ids_item_data
            )

            external_ids.append(external_ids_item)

        formats = []
        _formats = d.pop("formats", UNSET)
        for formats_item_data in _formats or []:

            def _parse_formats_item(data: object) -> Any:
                return cast(Any, data)

            formats_item = _parse_formats_item(formats_item_data)

            formats.append(formats_item)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:

            def _parse_contacts_item(data: object) -> Any:
                return cast(Any, data)

            contacts_item = _parse_contacts_item(contacts_item_data)

            contacts.append(contacts_item)

        license_ = d.pop("license", UNSET)

        rights = d.pop("rights", UNSET)

        record_geo_json_properties = cls(
            created=created,
            updated=updated,
            type_=type_,
            title=title,
            description=description,
            keywords=keywords,
            themes=themes,
            language=language,
            languages=languages,
            resource_languages=resource_languages,
            external_ids=external_ids,
            formats=formats,
            contacts=contacts,
            license_=license_,
            rights=rights,
        )

        record_geo_json_properties.additional_properties = d
        return record_geo_json_properties

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
