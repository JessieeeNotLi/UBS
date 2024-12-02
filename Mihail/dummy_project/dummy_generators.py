from classes.generators import DescriptionGenerator, ParamsGenerator

# dummy class serving for testing and as an example


class DummyDescriptionGenerator(DescriptionGenerator):
    def __init__(self, ):
        super().__init__()

    def generate(self, **kwargs):
        # if params necessary for description generation
        # assert "params" in kwargs

        return "Dummy Description"


# simulated the requirement for data and a description, as does the RAG in the MVP
class DummyParamsGenerator(ParamsGenerator):
    def __init__(self, prev_events):
        super().__init__()
        self.prev_events = prev_events

    def generate(self, description):
        return [0.32, 0.34]
