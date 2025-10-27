from enum import Enum


class LanguageDir(str, Enum):
    BTT = "btt"
    LTR = "ltr"
    RTL = "rtl"
    TTB = "ttb"

    def __str__(self) -> str:
        return str(self.value)
