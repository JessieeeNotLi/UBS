from classes.evaluator import Evaluator, ScenarioTypes


# for the MVP, this is the gaussian
class DummyEvaluator(Evaluator):
    def __init__(self):
        super().__init__()

    def get_level(self, scenario):
        return ScenarioTypes.PLAUSIBLE  # or just a number tbh

    # TODO also add change level
