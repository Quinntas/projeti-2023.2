import json
from typing import List

import matplotlib.pyplot as plt

from src.classes.bob import Bob, BobStatus
from src.classes.params import Params
from src.classes.result import Result


class Engine:
    def __init__(self, initial_params_path: str):
        self.params: Params = self.read_params(initial_params_path)

        self.bobs: List[Bob] = []

        self.prepare()

        self.results: List[Result] = []

    @staticmethod
    def read_params(initial_params_path: str) -> Params:
        with open(initial_params_path) as f:
            return Params(**json.load(f))

    def prepare(self):
        for i in range(self.params.popCount):
            self.bobs.append(Bob(name=f"Bob #{i}"))

    def plot_graph(self):
        days = list(range(1, self.params.days + 1))
        plt.plot(days, [result.healthy for result in self.results], label='Healthy')
        plt.plot(days, [result.infected for result in self.results], label='Infected')
        plt.plot(days, [result.recovered for result in self.results], label='Recovered')
        plt.xlabel('Days')
        plt.ylabel('Number of Bobs')
        plt.legend()
        plt.title('Bob Status Over Days')
        plt.show()

    def run(self):
        for day in range(self.params.days):
            for bob in self.bobs:
                bob.live(self.params.infectionProb, self.params.recoveryRate)

            self.results.append(Result(
                day=day + 1,
                healthy=len([bob for bob in self.bobs if bob.status == BobStatus.HEALTHY]),
                infected=len([bob for bob in self.bobs if bob.status == BobStatus.INFECTED]),
                recovered=len([bob for bob in self.bobs if bob.status == BobStatus.RECOVERED]),
            ))

            print(f"Day {day + 1}")
            print(f"Healthy: {len([bob for bob in self.bobs if bob.status == BobStatus.HEALTHY])}")
            print(f"Infected: {len([bob for bob in self.bobs if bob.status == BobStatus.INFECTED])}")
            print(f"Recovered: {len([bob for bob in self.bobs if bob.status == BobStatus.RECOVERED])}")
            print()
