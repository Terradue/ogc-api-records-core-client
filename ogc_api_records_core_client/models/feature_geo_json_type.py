from enum import Enum


class FeatureGeoJSONType(str, Enum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
