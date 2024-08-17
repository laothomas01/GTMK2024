class Assignment:
    def __init__(self, name, deadline, reward, employee_count, difficulty):
        self.name = name
        self.deadline = deadline
        self.reward = reward
        self.employee_count = employee_count
        self.progress_count = 0  # Starts at 0
        self.difficulty = difficulty

    def remove_employees(self, count):
        if count >= self.employee_count:
            print(f"Cannot remove {count} employees. Removing all employees instead.")
            self.employee_count = 0
        else:
            self.employee_count -= count
            print(f"{count} employees removed. Employees left: {self.employee_count}")

    def add_employees(self, count):
        self.employee_count += count
        print(f"{count} employees added. Total employees: {self.employee_count}")

    def increase_progress(self, amount):
        self.progress_count += amount
        print(f"Progress increased by {amount}. Current progress: {self.progress_count}")

    def is_done(self):
        if self.progress_count >= self.deadline:
            print(f"Assignment '{self.name}' is completed.")
            return True
        else:
            print(f"Assignment '{self.name}' is not yet completed.")
            return False
