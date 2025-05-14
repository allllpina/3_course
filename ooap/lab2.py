# Lab 2 - Composite*, flyweight and proxy

from abc import ABC, abstractmethod

# === Інтерфейс (Component) ===
class CommandUnit(ABC):
    @abstractmethod
    def execute_command(self, command):
        pass

# === Солдат (Leaf) ===
class Soldier(CommandUnit):
    def __init__(self, name):
        self.name = name

    def execute_command(self, command):
        print(f"Солдат {self.name} виконує команду: {command}")

# === Відділення/Група (Composite) ===
class Squad(CommandUnit):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, unit: CommandUnit):
        self.members.append(unit)

    def remove(self, unit: CommandUnit):
        self.members.remove(unit)

    def execute_command(self, command):
        print(f"🔊 Віддається команда '{command}' взводу {self.name}:")
        for member in self.members:
            member.execute_command(command)


# Солдати
s1 = Soldier("Іван")
s2 = Soldier("Петро")
s3 = Soldier("Олег")
s4 = Soldier("Сергій")

# Відділення 1
squad1 = Squad("1-е відділення")
squad1.add(s1)
squad1.add(s2)

# Відділення 2
squad2 = Squad("2-е відділення")
squad2.add(s3)
squad2.add(s4)

# Взвод
platoon = Squad("взвод 101")
platoon.add(squad1)
platoon.add(squad2)

# Віддаємо команду
platoon.execute_command("Кроком руш!")
print()
s1.execute_command("Стій!")
