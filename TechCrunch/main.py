# main.py
from company_riot import CompanyRiot
from blackout import Blackout
from tgi_friday import TGIFriday
from event_manager import EventManager
from company import Company
from assignment import Assignment


# class Tutorial:
#     def __init__(self):
#         self.cash = 10000  # Starting cash for the tutorial
#         self.assignments = [
#             Assignment("Coffee Supply", 100, 500, 5, 500, "Easy"),
#             Assignment("New Laptops", 300, 3000, 10, 3000, "Medium"),
#             Assignment("Office Renovation", 500, 5000, 15, 5000, "Hard")
#         ]
#     def start(self):
#         self.learn_to_view_assignments()

#     def learn_to_view_assignments(self):
#         print("Welcome to the game tutorial!\n")
#         print("You have 1 unread message.\n")
#         input("Press Enter to view the message...")

#         self.view_assignments()

#         assignment_index = int(input("Select an assignment number to view its details: ")) - 1
#         print(f"\nYou selected: {self.assignments[assignment_index].name}\n")

#         view_details = input("Would you like to view the assignment details? (yes/no):\n ").strip().lower()
#         if view_details == 'yes':
#             self.view_assignment_details(assignment_index)
#             print("Good. Now let's learn to select an assignment. \n")
#         else:
#             print("You chose not to view the assignment details.\n")

#     def view_assignments(self):
#         print("Here are the available assignments:")
#         for i, assignment in enumerate(self.assignments, start=1):
#             print(f"{i}.")
#             assignment.print_assignment_name()
#             assignment.print_attributes()
#         print("\n")

#     def view_assignment_details(self, index):
#         if 0 <= index < len(self.assignments):
#             assignment = self.assignments[index]
#             assignment.print_description()
#         else:
#             print("Invalid assignment selected.\n")



def main():
    company = Company(5000,4)
    
if __name__ == "__main__":
    main()
