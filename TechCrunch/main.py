# main.py
from company_riot import CompanyRiot
from blackout import Blackout
from tgi_friday import TGIFriday
from event_manager import EventManager
from company import Company

def main():
    # Create an event manager
    event_manager = EventManager()

    # Populate event manager with events
    event1 = CompanyRiot("A riot broke out among employees.")
    event2 = Blackout("The office lost power for several hours.")
    event3 = TGIFriday("An unexpected company-wide celebration event.")

    event_manager.add_event("riot", event1)
    event_manager.add_event("blackout", event2)
    event_manager.add_event("celebration", event3)

    # Create and initialize a company object
    company = Company(overall_funding=100000, employee_count=50)

    # Example game loop (simple simulation)
    running = True
    while running:
        print("\n--- Main Game Loop ---")
        print("1. Perform all tasks")
        print("2. Perform a specific task")
        print("3. Show company status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            event_manager.perform_all_tasks()
        elif choice == "2":
            task_name = input("Enter the task name (e.g., 'blackout'): ")
            event_manager.perform_task(task_name)
        elif choice == "3":
            print(f"Company Status:\nFunding: ${company.overall_funding}\nEmployees: {company.employee_count}")
        elif choice == "4":
            print("Exiting game...")
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
