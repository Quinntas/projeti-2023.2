from abc import ABC, abstractmethod

from src.classes.bob import Bob


class BaseModule(ABC):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")
        self.priority = kwargs.get("priority")

    @abstractmethod
    def run(self, bob: Bob):
        pass
