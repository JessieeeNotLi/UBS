from classes.params import Param
import numpy as np


# could be renamed to scenario
class Event:
    def __init__(self, date, params: dict[str, list[Param]],  description="") -> None:
        # perhaps an impact would help ?? idk, as this something to be evaluated by the evaluator
        self.date = date  # date
        self.params = params  # cpu -> [cpu_0, cpu_6, cpu_12, cpu_18, cpu_24]
        self.description = description  # can be empty for a scenario with no description

    def get_flat_data(self):
        # TODO only the RELATIVE params get flattened
        flat_data = []
        # for .... in ......:
        # flat_data = flat_data + [self.data[column.name][i + 1] / self.data[column.name][i] for i in range(len(self.data[column.name]) - 1)]
        return np.array(flat_data)
