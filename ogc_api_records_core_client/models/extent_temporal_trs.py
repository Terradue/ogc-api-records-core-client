from enum import Enum


class ExtentTemporalTrs(str, Enum):
    HTTPWWW_OPENGIS_NETDEFUOMISO_86010GREGORIAN = (
        "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
    )

    def __str__(self) -> str:
        return str(self.value)
