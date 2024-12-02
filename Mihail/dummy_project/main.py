from dummy_evaluator import DummyEvaluator
from dummy_generators import DummyDescriptionGenerator, DummyParamsGenerator
from classes.event import Event
from datetime import date
# params[date] -> economic params for that date:
# - load data for timeline params, we need to have econParams[date] -> economic params
prev_params = []
# events = Event[]:
# - load data for timeline events, we need to have Event = {description, impact, date (can be used to get params)}
prev_events = []

# DescriptionGenerator: generate description (MVP: use LLM to generate description based on)
descriptionGenerator = DummyDescriptionGenerator()
description = descriptionGenerator.generate()

print(description)

# ParamsGenerator: generate parameters (MVP: use rag approximator)
paramsGenerator = DummyParamsGenerator(prev_events)
params = paramsGenerator.generate(description)
print(params)

# Evaluator:
scenario = Event(description=description, date=date(1900, 11, 11), params={})  # TODO complete
classifier = DummyEvaluator()
classifier.get_level(scenario)
