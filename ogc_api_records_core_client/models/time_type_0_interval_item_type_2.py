from enum import Enum


class TimeType0IntervalItemType2(str, Enum):
    VALUE_0 = ".."

    def __str__(self) -> str:
        return str(self.value)
