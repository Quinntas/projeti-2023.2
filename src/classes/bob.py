import enum
import random

from src.classes.base_class import BaseClass


class BobStatus(enum.Enum):
    HEALTHY = 0
    INFECTED = 1
    RECOVERED = 2
    DEAD = 3


class Mood(enum.Enum):
    HAPPY = 0
    SAD = 1
    ANGRY = 2
    CONFUSED = 3
    EXCITED = 4
    SCARED = 5
    SURPRISED = 6
    DISGUSTED = 7


class Gender(enum.Enum):
    MALE = 0
    FEMALE = 1


class Profession(enum.Enum):
    SCIENTIST = 0
    DOCTOR = 1
    TEACHER = 2
    UNEMPLOYED = 3


class ImmuneSystem(enum.Enum):
    STRONG = 0
    AVG = 1
    WEAK = 1


def get_random_age() -> int:
    return random.randint(10, 60)


def get_random_profession(age: int) -> Profession:
    if age >= 40 or age <= 20:
        return Profession.UNEMPLOYED

    return random.choice(list(Profession))


def get_random_immune_system(age: int) -> ImmuneSystem:
    if age >= 40:
        return ImmuneSystem.WEAK
    elif age <= 25:
        return ImmuneSystem.STRONG

    return random.choice(list(ImmuneSystem))


def get_random_mood() -> Mood:
    return random.choice(list(Mood))


def get_random_gender() -> Gender:
    return random.choice(list(Gender))


class Bob(BaseClass):
    name: str

    health: int
    age: int = 0

    profession: Profession = Profession.UNEMPLOYED
    immuneSystem: ImmuneSystem = ImmuneSystem.AVG
    gender: Gender = Gender.MALE
    mood: Mood = Mood.HAPPY
    status: BobStatus = BobStatus.HEALTHY

    recoveryProgress: int = 0

    def spawn(self):
        self.age = get_random_age()
        self.profession = get_random_profession(self.age)
        self.immuneSystem = get_random_immune_system(self.age)
        self.gender = get_random_gender()
        self.mood = get_random_mood()
        return self

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            self.status = BobStatus.DEAD

    def live(self, **kwargs):
        lethality = kwargs.get("lethality")
        recovery_rate = kwargs.get("recovery_rate")
        infection_prob = kwargs.get("infection_prob")

        match self.status:
            case BobStatus.DEAD:
                pass

            case BobStatus.RECOVERED:
                pass

            case BobStatus.INFECTED:
                self.take_damage(lethality)
                self.recoveryProgress += recovery_rate
                if self.recoveryProgress >= 100:
                    self.status = BobStatus.RECOVERED

            case BobStatus.HEALTHY:
                if infection_prob > 0:
                    result = random.randint(0, 100)
                    if result <= infection_prob:
                        self.status = BobStatus.INFECTED
