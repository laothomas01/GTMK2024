# what is an assignment? 
# quarter's project
class Assignment:
    def __init__(self, name, deadline, reward, employee_count, cost_amount, difficulty):
        self.name = name
        self.description = "The company needs to buy more coffee for its employees."
        self.deadline = deadline
        self.reward = reward
        self.employee_count = employee_count
        self.progress_count = 0  # Starts at 0
        self.difficulty = difficulty
        self.cost = cost_amount

    def remove_employees(self, count):
            self.employee_count -= count 
        # if count >= self.employee_count:
        #     print(f"Cannot remove {count} employees. Removing all employees instead.")
        #     self.employee_count = 0
        # else:
        #     self.employee_count -= count
        #     print(f"{count} employees removed. Employees left: {self.employee_count}")

    def add_employees(self, count):
            self.employee_count += count 
        # self.employee_count += count
        # print(f"{count} employees added. Total employees: {self.employee_count}")
    
    #need to scale progress increase 
    def increase_progress(self, amount):
            self.progress_count += amount 
        # self.progress_count += amount
        # print(f"Progress increased by {amount}. Current progress: {self.progress_count}")
    def decrease_progress(self,amount):
            self.progress_count -= amount 

    def is_done(self):
        if self.progress_count >= self.deadline:
            print(f"Assignment '{self.name}' is completed.")
            return True
        else:
            print(f"Assignment '{self.name}' is not yet completed.")
            return False

    # def print_description(self):
    #     print(f"Description: {self.description}")
    # def print_assignment_name(self):
    #     print(f"Assignment Name: {self.name}")
    # def print_attributes(self):
    #     print(f"Deadline: {self.deadline}")
    #     print(f"Reward: ${self.reward}")
    #     print(f"Employee Count: {self.employee_count}")
    #     print(f"Progress: {self.progress_count}/{self.deadline}")
    #     print(f"Difficulty: {self.difficulty}")
    #     print(f"Cost: ${self.cost}\n")
    


# Example usage:
# assignment = Assignment("Coffee Supply", 100, 500, 5, 500, "Easy")
# assignment.print_attributes()
