from src.classes.base_class import BaseClass


class Virus(BaseClass):
    name: str

    infectiousness: int
    infectionProb: int
    infectionRadius: int
    lethality: int

    mutationProb: int
    mutationFactor: int
