__cls_name__ = "Cure"

from src.classes.bob import Profession
from src.modules.core.base_module import BaseModule


class Cure(BaseModule):
    def __init__(self):
        super().__init__(name="Cure", priority=1)
        self.cure_progress = 0.0

    def run(self, bob):
        if bob.profession != Profession.SCIENTIST:
            return
        if self.cure_progress >= 100:
            return
        self.cure_progress += 0.1
