from enum import Enum


class MultilinestringGeoJSONType(str, Enum):
    MULTILINESTRING = "MultiLineString"

    def __str__(self) -> str:
        return str(self.value)
