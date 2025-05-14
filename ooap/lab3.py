# Lab 3 - Command* and chain of responsibility

from abc import ABC, abstractmethod

# === Receiver ===
class FastFoodOrder:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        print(f"➕ Додано: {item}")
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            print(f"➖ Видалено: {item}")
            self.items.remove(item)
        else:
            print(f"⚠️ Страву '{item}' не знайдено в замовленні!")

    def show_order(self):
        print("\n🧾 Поточне замовлення:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        if not self.items:
            print("🔹 Порожнє замовлення")

# === Command Interface ===
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# === Concrete Commands ===
class AddItemCommand(Command):
    def __init__(self, order: FastFoodOrder, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.add_item(self.item)

class RemoveItemCommand(Command):
    def __init__(self, order: FastFoodOrder, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.remove_item(self.item)

# === Invoker ===
class Waiter:
    def __init__(self):
        self.history = []

    def take_order(self, command: Command):
        self.history.append(command)
        command.execute()

# === Client code ===

order = FastFoodOrder()
waiter = Waiter()
# Клієнт формує замовлення:
waiter.take_order(AddItemCommand(order, "Бургер"))
waiter.take_order(AddItemCommand(order, "Картопля фрі"))
waiter.take_order(AddItemCommand(order, "Кока-Кола"))
waiter.take_order(RemoveItemCommand(order, "Картопля фрі"))
waiter.take_order(RemoveItemCommand(order, "Суші"))
order.show_order()
