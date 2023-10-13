import json
from typing import List

import matplotlib.pyplot as plt

from src.classes.bob import Bob, BobStatus
from src.classes.result import Result
from src.classes.virus import Virus
from src.modules.core.module_loader import loaded_models


class Engine:
    def __init__(self, initial_params_path: str):
        self.params: dict = self.read_params(initial_params_path)

        self.bobs: List[Bob] = []
        self.viruses: List[Virus] = []

        self.prepare()

        self.results: List[Result] = []

    @staticmethod
    def read_params(initial_params_path: str):
        with open(initial_params_path) as f:
            return json.load(f)

    def prepare(self):
        print("[SIMULATION] Preparing...")
        for i in range(self.params["popCount"]):
            self.bobs.append(Bob(name=f"Bob #{i}", health=self.params["bob"]["initialHealth"]).spawn())
        self.viruses.append(Virus(**self.params["virus"]))

    def plot_graph(self):
        days = list(range(1, self.params["days"] + 1))
        plt.plot(days, [result.healthy for result in self.results], label='Healthy')
        plt.plot(days, [result.infected for result in self.results], label='Infected')
        plt.plot(days, [result.recovered for result in self.results], label='Recovered')
        plt.plot(days, [result.dead for result in self.results], label='Dead')
        plt.xlabel('Days')
        plt.ylabel('Number of Bobs')
        plt.legend()
        plt.title(f'Bob Status Over Days ({" ".join([virus.name for virus in self.viruses])})')
        plt.show()

    def run(self):
        print("[SIMULATION] Running...")
        for day in range(self.params["days"]):
            for bob in self.bobs:
                _virus = max(self.viruses, key=lambda virus: virus.infectiousness)
                bob.live(
                    infection_prob=_virus.infectionProb,
                    recovery_rate=self.params["bob"]["immuneSystem"][bob.immuneSystem.name]["recoveryRate"],
                    lethality=_virus.lethality,
                )
                for module in loaded_models:
                    module.run(bob)

            self.results.append(Result(
                day=day + 1,
                healthy=len([bob for bob in self.bobs if bob.status == BobStatus.HEALTHY]),
                infected=len([bob for bob in self.bobs if bob.status == BobStatus.INFECTED]),
                recovered=len([bob for bob in self.bobs if bob.status == BobStatus.RECOVERED]),
                dead=len([bob for bob in self.bobs if bob.status == BobStatus.DEAD]),
            ))

            print(f"Day {day + 1}")
            print(f"Healthy: {len([bob for bob in self.bobs if bob.status == BobStatus.HEALTHY])}")
            print(f"Infected: {len([bob for bob in self.bobs if bob.status == BobStatus.INFECTED])}")
            print(f"Recovered: {len([bob for bob in self.bobs if bob.status == BobStatus.RECOVERED])}")
            print()

        print("[SIMULATION] Finished!")

        print(loaded_models[0].__dict__)
