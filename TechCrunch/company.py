from assignment import Assignment


class Company:
    def __init__(self, overall_funding, employee_count):
        self.assignments = {}  # Dictionary with string keys and Assignment values
        self.overall_funding = overall_funding
        self.employee_count = employee_count
        self.available_employee_count = employee_count

    def hire_employee(self):
        self.employee_count += 1
        print(f"Employee hired. Total employees: {self.employee_count}")

    def fire_employee(self):
        if self.employee_count > 0:
            self.employee_count -= 1
            print(f"Employee fired. Total employees: {self.employee_count}")
        else:
            print("No employees to fire.")

    def increase_funds(self, amount):
        self.overall_funding += amount
        print(f"Funds increased by {amount}. Total funds: {self.overall_funding}")

    def decrease_funds(self, amount):
        if self.overall_funding >= amount:
            self.overall_funding -= amount
            print(f"Funds decreased by {amount}. Total funds: {self.overall_funding}")
        else:
            print("Insufficient funds to decrease.")

    def add_assignment(self, key, assignment):
        if key not in self.assignments:
            self.assignments[key] = assignment
            print(f"Assignment '{key}' added.")
        else:
            print(f"Assignment '{key}' already exists.")

    def increase_available_employee_count(self,amount):
        if(amount >= self.employee_count):
            self.available_employee_count = self.employee_count
        else:
            self.available_employee_count += amount
    
    def decrease_available_employee_count(self,amount):
        if(amount >= self.employee_count):
            self.available_employee_count = 0
        else:
            self.available_employee_count -= amount
    
        