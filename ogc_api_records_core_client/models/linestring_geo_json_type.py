from enum import Enum


class LinestringGeoJSONType(str, Enum):
    LINESTRING = "LineString"

    def __str__(self) -> str:
        return str(self.value)
