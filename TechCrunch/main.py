# # # # main.py
# # # from company_riot import CompanyRiot
# # # from blackout import Blackout
# # # from tgi_friday import TGIFriday
# # # from event_manager import EventManager
# # # from company import Company
# # # from assignment import Assignment

# # import random

# # # # class Tutorial:
# # # #     def __init__(self):
# # # #         self.cash = 10000  # Starting cash for the tutorial
# # # #         self.assignments = [
# # # #             Assignment("Coffee Supply", 100, 500, 5, 500, "Easy"),
# # # #             Assignment("New Laptops", 300, 3000, 10, 3000, "Medium"),
# # # #             Assignment("Office Renovation", 500, 5000, 15, 5000, "Hard")
# # # #         ]
# # # #     def start(self):
# # # #         self.learn_to_view_assignments()

# # # #     def learn_to_view_assignments(self):
# # # #         print("Welcome to the game tutorial!\n")
# # # #         print("You have 1 unread message.\n")
# # # #         input("Press Enter to view the message...")

# # # #         self.view_assignments()

# # # #         assignment_index = int(input("Select an assignment number to view its details: ")) - 1
# # # #         print(f"\nYou selected: {self.assignments[assignment_index].name}\n")

# # # #         view_details = input("Would you like to view the assignment details? (yes/no):\n ").strip().lower()
# # # #         if view_details == 'yes':
# # # #             self.view_assignment_details(assignment_index)
# # # #             print("Good. Now let's learn to select an assignment. \n")
# # # #         else:
# # # #             print("You chose not to view the assignment details.\n")

# # # #     def view_assignments(self):
# # # #         print("Here are the available assignments:")
# # # #         for i, assignment in enumerate(self.assignments, start=1):
# # # #             print(f"{i}.")
# # # #             assignment.print_assignment_name()
# # # #             assignment.print_attributes()
# # # #         print("\n")

# # # #     def view_assignment_details(self, index):
# # # #         if 0 <= index < len(self.assignments):
# # # #             assignment = self.assignments[index]
# # # #             assignment.print_description()
# # # #         else:
# # # #             print("Invalid assignment selected.\n")



# # # class Game:
# # #     def __init__(self,starting_money,starting_employee_count):
# # #         self.initial_money = starting_money
# # #         self.initial_employee_count = starting_employee_count
    
# # #     def start_game(self):
# # #         print("Game started!")
# # #         run = True
# # #         company = Company(self.initial_money,self.initial_employee_count)

# # #         while(run):
# # #             print("\nWhat do you want to do?")
# # #             print("1. Allocate funds")
# # #             print("2. Wait")

# # # def main():

# # # if __name__ == "__main__":
# # #     main()


# # class Game:
# #     def __init__(self,start_money,employee_count):
# #         self.current_money = start_money
# #         self.employee_count = employee_count
# #         self.projects = []
# #         self.project_database = {
# #             "Easy" : {
# #                 {
# #                     "name" : "There is an octopus in the bathroom",
# #                     "cost" : 0.01 * self.current_money,
# #                     "progress" : 3,
# #                     "assigned_employees" : 0,
# #                     "deadline" : 5,
# #                     "reward": random.randrange(50,100)
# #                 },
# #                 {
# #                     "name": "Assist a gnome with organizing their enchanted garden",
# #                     "cost": 0.02 * self.current_money,
# #                     "progress": 3,
# #                     "assigned_employees" : 0,
# #                     "deadline" : 5,
# #                     "reward": random.randrange(50,100)  # Cash reward for completing the task
# #                 },
# #                 {
# #                     "name": "Reprogram a malfunctioning magical light bulb",
# #                     "cost": 0.03 * self.current_money,
# #                     "progress": 3,
# #                     "assigned_employees" : 0,
# #                     "deadline" : 5,
# #                     "reward": random.randrange(50,100)  # Cash reward for completing the task

# #                 },
# #                 {
# #                     "name": "Locate a lost dragon egg in the office",
# #                     "cost": 0.04 * self.current_money,
# #                     "progress": 3,
# #                     "assigned_employees" : 0,
# #                     "deadline" : 5,
# #                     "reward": random.randrange(50,100)  # Cash reward for completing the task

# #                 },
# #                 {
# #                     "name": "Clean up after a mischievous pixie party",
# #                     "cost": 0.05 * self.current_money,
# #                     "progress": 3,
# #                     "assigned_employees" : 0,
# #                     "deadline" : 5,
# #                     "reward": random.randrange(50,100)  # Cash reward for completing the task

# #                 }
# #             },
# #             "Medium" : {
# #                        {
# #             "name": "Negotiate with a fairy who claims the office is on their land",
# #             "cost": 0.1 * self.current_money,
# #             "progress": 6,
# #             "assigned_employees" : 0,
# #                     "deadline" : 10,
# #                     "reward": random.randrange(150,200)  # Cash reward for completing the task

# #         },
# #         {
# #             "name": "Help a time traveler repair their malfunctioning chronometer",
# #             "cost": 0.15 * self.current_money,
# #             "progress": 6,
# #             "assigned_employees" : 0,
# #                     "deadline" : 10,
# #                     "reward": random.randrange(150,200)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Resolve a dispute between a mermaid and a sea dragon over office supplies",
# #             "cost": 0.2 * self.current_money,
# #             "progress": 6,
# #             "assigned_employees" : 0,
# #                     "deadline" : 10,
# #                     "reward": random.randrange(150,200)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Assist an alien ambassador with translating a mystical document",
# #             "cost": 0.25 * self.current_money,
# #             "progress": 6,
# #             "assigned_employees" : 0,
# #                     "deadline" : 10,
# #                     "reward": random.randrange(150,200)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Fix the enchanted vending machine that dispenses magical artifacts",
# #             "cost": 0.3 * self.current_money,
# #             "progress": 6,
# #             "assigned_employees" : 0,
# #                     "deadline" : 10,
# #                     "reward": random.randrange(150,200)  # Cash reward for completing the task


# #         }
# #             },
# #             "Hard" : {
# #                         {
# #             "name": "Contain an interdimensional portal that has opened in the conference room",
# #             "cost": 0.5 * self.current_money,
# #             "progress": 12,
# #             "assigned_employees" : 0,
# #                     "deadline" : 15,
# #                     "reward": random.randrange(300,500)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Stop a rogue wizard from summoning a dark army in the office",
# #             "cost": 0.6 * self.current_money,
# #             "progress": 12,
# #             "assigned_employees" : 0,
# #                     "deadline" : 15,
# #                     "reward": random.randrange(300,500)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Negotiate peace between warring factions of mythical creatures invading the office",
# #             "cost": 0.7 * self.current_money,
# #             "progress": 12,
# #             "assigned_employees" : 0,
# #                     "deadline" : 15,
# #                     "reward": random.randrange(300,500)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Repair a magical artifact that is causing the office to experience time distortions",
# #             "cost": 0.8 * self.current_money,
# #             "progress": 12,
# #             "assigned_employees" : 0,
# #                     "deadline" : 15,
# #                     "reward": random.randrange(300,500)  # Cash reward for completing the task


# #         },
# #         {
# #             "name": "Prevent the office from being absorbed into a magical black hole",
# #             "cost": 0.9 * self.current_money,
# #             "progress": 12,
# #             "assigned_employees" : 0,
# #                     "deadline" : 15,
# #                     "reward": random.randrange(300,500)  # Cash reward for completing the task
# #         }
# #             }
# #         } 

# #     def wait(self):
# #         for i in range(len(self.projects)):
# #             self.projects[i]["deadline"] -= 1
# #             if(self.projects[i]["assigned_employees"]):
# #                 self.projects[i]["progress"] += 1
# #     def check_status(self):
# #         for i in range(len(self.projects)):
# #             if(self.projects[i]["deadline"] <= 0):
# #                 self.projects.pop(i)

            
# #             # for project in projects:
# #             #     projects[project] += 1
            
        


# ######################
# # load quest database 
# from company import Company

# def main():
#     company = Company(total_funding=1000, employee_count=50)
# # Call the main function
# if __name__ == "__main__":
#     main()
#     # game = Game(100,3)

#     # game.print_job("Easy","Job A")

#     # game.update_easy_difficulty_job_progress("Job A",10)

#     # game.print_job("Easy","Job A")
    

#     # company.select_job("Easy","Job A")
#     # print(company.get_available_job("Easy","Job A"))

#     # print("Selected Jobs")
#     # company.print_selected_jobs()

    

# #     pass


        
from company import Company 

def main():
    company = Company(300,3)
    company.print_available_jobs()
    company.print_available_job("Job A")
    company.add_selected_job("Job A")
    print(company.get_selected_jobs_size())
    company.print_selected_jobs()
    company.remove_selected_job("Job A")
    print(company.get_selected_jobs_size())

if __name__ == "__main__":
    main()