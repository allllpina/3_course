# Lab 1 - Facade* and decorator*

# === Базовий клас персонажа ===
class BaseCharacter:
    def __init__(self, name):
        self.name = name
        self.base_power = 0
        self.base_defense = 0

    def get_power(self):
        return self.base_power

    def get_defense(self):
        return self.base_defense

    def __str__(self):
        return f"{self.name} (Сила: {self.get_power()}, Захист: {self.get_defense()})"

# === Класи персонажів ===
class Human(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.base_power = 10
        self.base_defense = 5

class Troll(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.base_power = 20
        self.base_defense = 10

class Orc(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.base_power = 30
        self.base_defense = 15

# === Декоратори ===
class CharacterDecorator(BaseCharacter):
    def __init__(self, character):
        self.character = character

    def get_power(self):
        return self.character.get_power()

    def get_defense(self):
        return self.character.get_defense()

    def __str__(self):
        return self.character.__str__()

# === Зброя ===
class Sword(CharacterDecorator):
    def get_power(self):
        return self.character.get_power() + 10

class Bow(CharacterDecorator):
    def get_power(self):
        return self.character.get_power() + 7

class Axe(CharacterDecorator):
    def get_power(self):
        return self.character.get_power() + 12

# === Обладунки ===
class MetalShield(CharacterDecorator):
    def get_defense(self):
        return self.character.get_defense() + 10

class WoodenShield(CharacterDecorator):
    def get_defense(self):
        return self.character.get_defense() + 5

# === Фасад гри ===
class GameFacade:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def stronger_than(self, character):
        return [c for c in self.characters if c.get_power() > character.get_power()]

    def beatable_within_hits(self, character, hits):
        attack_power = character.get_power() * hits
        return [c for c in self.characters if attack_power > c.get_defense() and c != character]

    def show_all(self):
        for c in self.characters:
            print(c)

# Ініціалізація гри
game = GameFacade()

# Створення персонажів
orc = Orc("Горг")
orc = Sword(orc)
orc = MetalShield(orc)

troll = Troll("Трог")
troll = Axe(troll)
troll = WoodenShield(troll)

human = Human("Людвіг")
human = Bow(human)
human = WoodenShield(human)

# Додавання до гри
game.add_character(orc)
game.add_character(troll)
game.add_character(human)

# Перевірка
game.show_all()

print("\nХто сильніший за Трога:")
for ch in game.stronger_than(troll):
    print(ch)

print("\nКого Людвіг може побити за 5 ударів:")
for ch in game.beatable_within_hits(human, 5):
    print(ch)


