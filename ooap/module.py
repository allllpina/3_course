from abc import ABC, abstractmethod
from collections import deque
import datetime


class Device:
    def __init__(self, name):
        self.name = name
        self.state = "викл"

    def on(self):
        if self.state == 'вкл':
            print(f"{self.name} вже було увімкнено.")
        else:
            self.state = "вкл"
            print(f"{self.name} увімкнено.")

    def off(self):
        if self.state == 'викл':
            print(f"{self.name} вже було вимкнено.")
        else:
            self.state = "викл"
            print(f"{self.name} вимкнено.")


class Command(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.on()

    def undo(self):
        self.device.off()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.off()

    def undo(self):
        self.device.on()


class RemoteControl:
    def __init__(self):
        self.history = deque()

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self, n=1):
        for _ in range(n):
            if self.history:
                cmd = self.history.pop()
                cmd.undo()
            else:
                print("Немає більше дій для скасування.")


def load_schedule(filename, devices):
    schedule = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, state, time_str = line.strip().split(',')
            time = datetime.datetime.strptime(time_str.strip(), "%H:%M").time()
            device = devices.get(name.strip().lower())
            if not device:
                continue
            if state.strip().lower() == 'вкл':
                cmd = TurnOnCommand(device)
            else:
                cmd = TurnOffCommand(device)
            schedule.append((time, cmd))
    return sorted(schedule, key=lambda x: x[0])


light = Device("Світло")
boiler = Device("Котел")
ac = Device("Кондиціонер")
devices = {
    "світло": light,
    "котел": boiler,
    "кондиціонер": ac
}

remote = RemoteControl()



schedule = load_schedule("./schedule.txt", devices)


 
now = datetime.datetime.now().time()
for time, command in schedule:
    if time <= now:
        remote.execute_command(command)


while True:
    cmd = input("Введіть команду (вкл/викл <прилад>, undo <N>, вийти): ").strip().lower()
    if cmd == "вийти":
        break
    elif cmd.startswith("вкл "):
        name = cmd[4:]
        if name in devices:
            remote.execute_command(TurnOnCommand(devices[name]))
        else:
            print("Невідомий прилад.")
    elif cmd.startswith("викл "):
        name = cmd[5:]
        if name in devices:
            remote.execute_command(TurnOffCommand(devices[name]))
        else:
            print("Невідомий прилад.")
    elif cmd.startswith("undo"):
        parts = cmd.split()
        n = int(parts[1]) if len(parts) > 1 else 1
        remote.undo_last(n)
    else:
        print("Невідома команда.")
