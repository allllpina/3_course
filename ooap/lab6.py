# Lab 6 - Visitor, template method* and strategy

from abc import ABC, abstractmethod

# ==== Базовий клас AI з шаблонним методом ====
class RaceAI(ABC):
    def run_ai(self):
        self.build_structures()
        self.train_units()
        self.attack_strategy()

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def train_units(self):
        pass

    @abstractmethod
    def attack_strategy(self):
        pass

# ==== Орки ====
class OrcAI(RaceAI):
    def build_structures(self):
        print("🏗️ Орки будують військові бараки та кузні")

    def train_units(self):
        print("🪖 Орки тренують воїнів з великими сокирами")

    def attack_strategy(self):
        print("⚔️ Орки йдуть у лобову атаку без страху!")

# ==== Люди ====
class HumanAI(RaceAI):
    def build_structures(self):
        print("🏰 Люди будують ферми та укріплення")

    def train_units(self):
        print("🏹 Люди тренують лучників і лицарів")

    def attack_strategy(self):
        print("🛡️ Люди спочатку обороняються, потім переходять у наступ")

# ==== Монстри ====
class MonsterAI(RaceAI):
    def build_structures(self):
        print("🚫 Монстри не будують")

    def train_units(self):
        print("👹 Монстри плодяться в печерах")

    def attack_strategy(self):
        print("🐾 Монстри нападають хаотично і дико")

# ==== Запуск ====
def play_race(ai: RaceAI):
    print("\n🎮 Початок гри за расу:")
    ai.run_ai()

# ==== Демонстрація ====

play_race(OrcAI())
play_race(HumanAI())
play_race(MonsterAI())
