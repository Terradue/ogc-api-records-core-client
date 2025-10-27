from enum import Enum


class ExtentSpatialCrs(str, Enum):
    HTTPWWW_OPENGIS_NETDEFCRSOGC0CRS84H = "http://www.opengis.net/def/crs/OGC/0/CRS84h"
    HTTPWWW_OPENGIS_NETDEFCRSOGC1_3CRS84 = (
        "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    )

    def __str__(self) -> str:
        return str(self.value)
