from enum import Enum


class ScenarioTypes(Enum):
    # PERHAPS THIS IS NOT USEFUL
    PLAUSIBLE = 1
    IMPROBABLE = 2
    COVID_LIKE = 3


class Evaluator:
    def __init__(self):
        pass

    def get_level(self, scenario) -> ScenarioTypes:
        # for example, we could consider an event with ratio 1e-50 as one with level 50,
        pass

    def change_level(self, new_level):
        # find delta such that we change the params with delta % the level goes to the new_level
        pass
