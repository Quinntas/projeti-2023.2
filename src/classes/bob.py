import enum
import random

from src.classes.base_class import BaseClass


class BobStatus(enum.Enum):
    HEALTHY = 0
    INFECTED = 1
    RECOVERED = 2


class Bob(BaseClass):
    name: str
    status: BobStatus = BobStatus.HEALTHY
    recoveryProgress: int = 0

    def live(self, infection_prob: int, recovery_rate: int):
        match self.status:
            case BobStatus.INFECTED:
                self.recoveryProgress += recovery_rate
                if self.recoveryProgress >= 100:
                    self.status = BobStatus.RECOVERED

            case BobStatus.HEALTHY:
                if infection_prob > 0:
                    result = random.randint(0, 100)
                    if result <= infection_prob:
                        self.status = BobStatus.INFECTED

            case BobStatus.RECOVERED:
                pass
