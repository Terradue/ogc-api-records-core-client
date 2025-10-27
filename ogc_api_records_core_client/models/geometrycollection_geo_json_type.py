from enum import Enum


class GeometrycollectionGeoJSONType(str, Enum):
    GEOMETRYCOLLECTION = "GeometryCollection"

    def __str__(self) -> str:
        return str(self.value)
