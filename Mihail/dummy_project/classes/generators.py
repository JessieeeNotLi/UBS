class Generator:
    def __init__(self, ):
        # use this to pass data necessary for the run function
        pass

    def generate(self, **kwargs):
        print("Hey you, 'generate' should be overriten.")


class DescriptionGenerator(Generator):
    def __init__(self, ):
        super().__init__()


class ParamsGenerator(Generator):
    def __init__(self):
        super().__init__()
