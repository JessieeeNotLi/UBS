from enum import Enum


class ParamType(Enum):
    ABSOLUTE = 1
    RELATIVE = 2


class Param:
    def __init__(self, name: str, value: any, type: ParamType, months_after=0):
        self.name = name
        self.value = value
        self.type = type
        self.months_after = 6  # TODO change

    @property
    def full_name(self):
        months_after = 6
        return f"cpi_{self.months_after}m"
