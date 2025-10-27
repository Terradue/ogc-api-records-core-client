from enum import Enum


class FeatureCollectionGeoJSONType(str, Enum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
