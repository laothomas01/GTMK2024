# event.py
class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def do_task(self):
        print(f"Task '{self.name}' has happened: {self.description}")
