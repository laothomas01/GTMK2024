# company_riot.py
from event import Event

class CompanyRiot(Event):
    def __init__(self, description):
        super().__init__("Company Riot", description)

    def do_task(self):
        print(f"Handling {self.name}: {self.description} - Employees are protesting!")
