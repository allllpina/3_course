# Lab5 - Memento, observer and state* 

from abc import ABC, abstractmethod

# ==== Абстрактний стан ====
class PlayerState(ABC):
    @abstractmethod
    def press_play(self, context): pass

    @abstractmethod
    def press_stop(self, context): pass

    @abstractmethod
    def press_pause(self, context): pass

    @abstractmethod
    def press_repeat(self, context): pass

# ==== Контекст ====
class PlayerContext:
    def __init__(self):
        self.state = LockedState()  # Стан за замовчуванням

    def set_state(self, state: PlayerState):
        print(f"📣 Перехід у стан: {state.__class__.__name__}")
        self.state = state

    # Дії
    def press_play(self):
        self.state.press_play(self)

    def press_stop(self):
        self.state.press_stop(self)

    def press_pause(self):
        self.state.press_pause(self)

    def press_repeat(self):
        self.state.press_repeat(self)

# ==== Стан: Розблоковано ====
class UnlockedState(PlayerState):
    def press_play(self, context):
        print("🎵 Відтворення радіо")

    def press_stop(self, context):
        print("⏹️ Зупинка відтворення")

    def press_pause(self, context):
        print("⏸️ Пауза")

    def press_repeat(self, context):
        print("🔁 Повтор потоку")

# ==== Стан: Заблоковано ====
class LockedState(PlayerState):
    def press_play(self, context):
        print("🔐 Плеєр заблоковано. Введіть PIN для розблокування.")
    
    def press_stop(self, context):
        print("🔐 Плеєр заблоковано. Введіть PIN для розблокування.")

    def press_pause(self, context):
        print("🔐 Плеєр заблоковано. Введіть PIN для розблокування.")
    
    def press_repeat(self, context):
        print("🔐 Плеєр заблоковано. Введіть PIN для розблокування.")

# ==== Стан: Розряджено ====
class LowBatteryState(PlayerState):
    def press_play(self, context):
        print("🔋 Батарея розряджена. Зарядіть плеєр!")

    def press_stop(self, context):
        print("🔋 Батарея розряджена. Зарядіть плеєр!")

    def press_pause(self, context):
        print("🔋 Батарея розряджена. Зарядіть плеєр!")

    def press_repeat(self, context):
        print("🔋 Батарея розряджена. Зарядіть плеєр!")


player = PlayerContext()

# Заблоковано (за замовчуванням)
player.press_play()

# Розблоковуємо
player.set_state(UnlockedState())
player.press_play()
player.press_pause()
player.press_repeat()

# Розряджено
player.set_state(LowBatteryState())
player.press_play()