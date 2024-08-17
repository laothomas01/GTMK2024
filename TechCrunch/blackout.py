# blackout.py
from event import Event

class Blackout(Event):
    def __init__(self, description):
        super().__init__("Blackout", description)

    def do_task(self):
        print(f"Handling {self.name}: {self.description} - Power outage affecting operations!")
