# import shutil
# from company import Company
# import sys
# import os
# """
# Features list:
# [] event manager
# [] assign employees to job
# [] add check for how player loses 
# [] tutorial section
# [] update job names(game polishing)
# [] connect events with how they affect the company
# [] make sure core gameplay is down before any extra feature is created <--------
#     [] make sure backend functionality function with front end 
# [] add more interactable options 
# [] allow the game to scale based on increasing difficulty
# [] make sure the game progresses in difficulty
# [] should there be an energy system? 
# [] action pointer/energy system can add complexity to this game 
# [] allow player to customize their name
# [] should employees cost money? 

# """


import sys
import shutil
import platform
import os
from company import Company
def clear_screen():
    """Clears the terminal screen based on the operating system."""
    os_type = platform.system()
    if os_type == "Windows":
        os.system('cls')
    elif os_type in ["Linux", "Darwin"]:  # Darwin is macOS
        os.system('clear')
    else:
        print("Unsupported OS.")
def print_centered(text):
    console_width = shutil.get_terminal_size().columns
    return text.center(console_width)

def print_centered_2(text, width):
    """Print text centered within the given width."""
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def print_with_border(text_lines, width=50):
    """Prints text lines with a border around them."""
    # Create the top and bottom border
    border_line = '+' + '-' * (width - 2) + '+'
    
    # Print the top border
    print(print_centered(border_line))
    
    for line in text_lines:
        # Print each line with side borders
        print(print_centered('|' + line.center(width - 2) + '|'))
    
    # Print the bottom border
    print(print_centered(border_line))

# class Game:
#     def __init__(self):
#         self.company = None 
#     def test(self):
#         self.company = Company(1200,10,5)

# class Game:
#     def __init__(self):
#         self.company = None
    
#     def test_hire_employees(self):
#         company = Company(starting_funds=1000, starting_employee_count=5)
        
#         while not company.is_dead():
#             try:
#                 # Corrected the print statement for user input
#                 choice = int(input(f"Enter the number of employees to hire (1 employee = ${company.get_worker_cost()}): "))
#                 company.hire_workers(choice)
#             except ValueError:
#                 print("Please enter a valid number.")
            
#             # Display company status after each hiring attempt
#             print(f"Current Funds: ${company.get_funds()}")
#             print(f"Current Max Employee Count: {company.get_max_employee_count()}")
#             print(f"Current Available Employee Count: {company.get_available_employee_count()}")
            
#             if company.is_dead():
#                 print("Company has run out of funds. Game over!")
#                 break
        
#     def test_assign_employees(self):
#         company = Company(starting_funds=1000, starting_employee_count=100)
#         company.populate_jobs(3, 2, 1)
        
#         while not company.is_dead():
#             job_names = company.display_available_jobs()  # Display jobs and get job names
            
#             try:
#                 # Prompt the user to select a job number (1-based indexing)
#                 job_number = int(input("Enter a number to select a job: "))
#                 clear_screen()
#                 # Validate job number
#                 if 1 <= job_number <= len(job_names):
#                     # Get job name based on 1-based index (convert to 0-based for list access)
#                     job_name = job_names[job_number - 1]
#                     num_employees = int(input(f"Enter the number of employees to assign"))
#                     clear_screen()

#                     # # num_employees = int(input(f"Enter the number of employees to assign (1 employee = ${company.get_worker_cost()}): "))
                    
#                     # Assign workers to the selected job
#                     company.assign_workers_to_job(job_name, num_employees)
                    
#                     # Check company status after assignment
#                     company.check_company_status()
                    
#                     # # Display company and job status
#                     # company.print_status_report()
                    
#                     if company.is_dead():
#                         print("Company has run out of funds. Game over!")
#                         break

#                     # # Optional: Advance to the next quarter
#                     # if input("Advance to next quarter? (y/n): ").lower() == 'y':
#                     #     company.advance_quarter()
#                     #     clear_screen()

                    
#                 else:
#                     print("Invalid job number. Please enter a number corresponding to an available job.")
            
#             except ValueError:
#                 print("Please enter a valid number.")

#         # while not company.is_dead():
#         #     company.display_available_jobs()
            
#         #     try:
#         #         # Prompt the user to select a job and the number of employees to assign
#         #         job_name = input("Enter the name of the job to assign employees to: ")
#         #         num_employees = int(input(f"Enter the number of employees to assign (1 employee = ${company.get_worker_cost()}): "))
                
#         #         company.assign_workers_to_job(job_name, num_employees)
#         #     except ValueError:
#         #         print("Please enter a valid number.")
#         #     except KeyError:
#         #         print("Invalid job name. Please choose a correct job name.")
            
#         #     # Check company status after assignment
#         #     company.check_company_status()
            
#         #     # Display company and job status
#         #     company.print_status_report()
            
#         #     if company.is_dead():
#         #         print("Company has run out of funds. Game over!")
#         #         break

#         #     # Optional: Advance to the next quarter
#         #     if input("Advance to next quarter? (y/n): ").lower() == 'y':
#         #         company.advance_quarter()


        
        


#     # Test script for Company class
#     def small_game_test(self):
#         # Initialize the Company
#         company = Company(starting_funds=1000, starting_employee_count=5)

#         # Populate initial jobs
#         company.populate_jobs(num_easy=3, num_medium=2, num_hard=1)

#         while not company.is_dead():
#             # Display available jobs
#             company.display_available_jobs()

#             # User chooses to queue a job
#             job_name = input("Enter the job name you want to queue (or type 'exit' to quit): ")
#             if job_name.lower() == 'exit':
#                 break

#             company.queue_job(job_name)
#             company.display_queued_jobs()

#             # User chooses to hire workers
#             workers_to_hire = int(input("Enter the number of workers to hire: "))
#             company.hire_workers(workers_to_hire)

#             # User chooses to assign workers to a job
#             job_to_assign = input("Enter the job name you want to assign workers to: ")
#             workers_to_assign = int(input("Enter the number of workers to assign: "))
#             company.assign_workers_to_job(job_to_assign, workers_to_assign)

#             # Process the turn
#             company.check_company_status()
#             company.print_status_report()

#             # Advance to next quarter
#             company.advance_quarter()
#             company.print_status_report()
#     def run_tests(self):
#         # Initialize Company with starting funds and employees
#         company = Company(starting_funds=5000, starting_employee_count=10)
        
#         # Display initial status
#         print("Initial Company Status:")
#         company.check_company_status()
#         print("\n")
        
#         # Advance to Quarter 2 and update job difficulties
#         company.advance_quarter()
#         print("Status after advancing to Quarter 2:")
#         company.check_company_status()
#         print("\n")
        
#         # Advance to Quarter 4 and update job difficulties
#         company.advance_quarter()
#         company.advance_quarter()
#         print("Status after advancing to Quarter 4:")
#         company.check_company_status()
#         print("\n")
        
#         # Advance to Quarter 6 and update job difficulties
#         company.advance_quarter()
#         company.advance_quarter()
#         print("Status after advancing to Quarter 6:")
#         company.check_company_status()
#         print("\n")
        
#         # Test hiring workers
#         print("Hiring 5 workers:")
#         company.hire_workers(5)
#         company.check_company_status()
#         print("\n")
        
#         # Test assigning workers to a job
#         print("Assigning 3 workers to 'EasyJobA':")
#         company.assign_workers_to_job("EasyJobA", 3)
#         company.check_company_status()
#         print("\n")
        
#         # Test displaying random jobs
#         print("Displaying 3 random jobs:")
#         company.display_random_jobs(3)
#         print("\n")
        
#         # Test job queuing and processing
#         print("Queueing 'EasyJobA':")
#         company.queue_job("EasyJobA")
#         company.process_queued_jobs()
#         company.check_company_status()

#     def test_company_api(self):
#         # Initialize company
#         company = Company(starting_funds=1000, starting_employee_count=10)
        
#         # Populate available jobs
#         company.populate_available_jobs()
        
#         # Display and select easy jobs
#         easy_jobs = company.find_easy_jobs()
#         print("Easy Jobs Available:")
#         for i, job in enumerate(easy_jobs, 1):
#             print(f"{i}. {job}")
#         selected_easy_jobs = [easy_jobs[int(input("Select an easy job by number: ")) - 1]]
        
#         # Display and select medium jobs
#         medium_jobs = company.find_medium_jobs()
#         print("Medium Jobs Available:")
#         for i, job in enumerate(medium_jobs, 1):
#             print(f"{i}. {job}")
#         selected_medium_jobs = [medium_jobs[int(input("Select a medium job by number: ")) - 1]]
        
#         # Display and select hard jobs
#         hard_jobs = company.find_hard_jobs()
#         print("Hard Jobs Available:")
#         for i, job in enumerate(hard_jobs, 1):
#             print(f"{i}. {job}")
#         selected_hard_jobs = [hard_jobs[int(input("Select a hard job by number: ")) - 1]]
        
#         # Assign workers to selected jobs
#         worker_count = int(input("Enter number of workers to assign to each selected job: "))
        
#         for job_name in selected_easy_jobs + selected_medium_jobs + selected_hard_jobs:
#             cost_per_worker = company.get_cost_per_worker(job_name)
#             if cost_per_worker:
#                 company.assign_workers_to_job(job_name, worker_count)
        
#         # Display queued jobs
#         company.display_queued_jobs()
        
#         # Call check company status
#         company.check_company_status()
        
#         # Print status
#         company.print_status_report()

#         # Test hiring of workers
#         hire_count = int(input("Enter number of workers to hire: "))
#         # hire_cost_per_worker = int(input("Enter cost per worker to hire: "))
        
#         company.hire_workers(hire_count, hire_cost_per_worker)
        
#         # Print status after hiring workers
#         company.print_status_report()


#     def greet_player(self):
#         console_width = shutil.get_terminal_size().columns
#         greeting = "Welcome to CEO Simulator 2024!"
#         welcome_message = "It's your first day as CEO, and the company is looking forward to working with you."
#         print(greeting.center(console_width))
#         print(welcome_message.center(console_width))
#         print()  # Adds a blank line for spacing


    
#     def start(self):
#         run = True 
#         while run:
#             self.greet_player()
#             press_start = False 
#             begin_game = False 
#             while not press_start:
#                 print(self.print_centered("You have unread messages. Press Enter to view them or Q to quit"))
#                 user_input = input()
#                 if user_input.lower() == "q":
#                     print(self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!"))
#                     sys.exit()
#                 elif user_input == "":
#                     begin_game = True 
#                     press_start = True 
#                 else:
#                     print(self.print_centered("Invalid Input"))

#             # Start initialization of data 
#             self.company = Company(starting_funds=1000, starting_employee_count=3)
#             # self.company.populate_jobs(num_easy=1, num_medium=1, num_hard=1)    def start(self):
#         run = True 
#         while run:
#             self.greet_player()
#             press_start = False 
#             begin_game = False 
#             while not press_start:
#                 print(self.print_centered("You have unread messages. Press Enter to view them or Q to quit"))
#                 user_input = input()
#                 if user_input.lower() == "q":
#                     print(self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!"))
#                     sys.exit()
#                 elif user_input == "":
#                     begin_game = True 
#                     press_start = True 
#                 else:
#                     print(self.print_centered("Invalid Input"))

#             # Start initialization of data 
#             self.company = Company(starting_funds=1000, starting_employee_count=3)
#             # self.company.populate_jobs(num_easy=3, num_medium=0, num_hard=0)
#             # self.company.display_available_jobs()
#                 # print(self.print_centered(f"Beginning 1st Quarter"))
#                 # print(self.print_centered("Available Jobs"))
            
#                 # print(self.print_centered(f"Beginning 1st Quarter"))
#                 # print(self.print_centered("Available Jobs"))
            




#             while begin_game:
#                 pass
#                 # pass
#                 # Handle game logic here 
                

#                 # if self.company.dead:
#                 #     print("You are dead")
#                 #     begin_game = False 
                
                
            
            
            
#             print(self.print_centered("Would you like to restart? (Y/N)"))
#             restart_input = input().lower()
#             restarting = True 
#             while restarting:
#                 if restart_input == "n":
#                     print(self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!"))
#                     run = False
#                     restarting = False 
#                 elif restart_input == "y":
#                     press_start = False 
#                     begin_game = False 
#                     restarting = False 
#                 else:
#                     print(self.print_centered("Invalid Input"))
#         sys.exit()
#     # # Example usage
#     # def test_company_progression(self):
#     #     company = Company(starting_funds=2000, starting_employee_count=10)
#     #     company.populate_jobs(num_easy=1, num_medium=1, num_hard=1)
        
#     #     # Display initial job list
#     #     print("Initial Jobs:")
#     #     company.display_available_jobs()
        
#     #     # Simulate progression through quarters
#     #     for _ in range(5):  # Example: 5 quarters
#     #         print(f"\nQuarter {company.current_quarter}")
#     #         company.advance_quarter()
#     #         print("Jobs after advancement:")
#     #         company.display_available_jobs()
            
#     #         # Get random jobs
#     #         random_easy_job = company.get_random_job("Easy")
#     #         random_medium_job = company.get_random_job("Medium")
#     #         random_hard_job = company.get_random_job("Hard")
            
#     #         print(f"Random Easy Job: {random_easy_job}")
#     #         print(f"Random Medium Job: {random_medium_job}")
#     #         print(f"Random Hard Job: {random_hard_job}") 
# 
def display_message():
    # Define the message
    message = """
Oh, hey, um, you’re going to that random planet thing. I’m here in my office, surrounded by... well, everything. I think I’ve got a coffee stain on my new shirt, I'm cheating on my wife, but whatever.

Oh, and my dog, Rex, chewed up, like, half the paperwork we needed. I’m trying to get him to focus, but he’s more interested in this squeaky toy. If you find something valuable on that planet, great. If not, I guess that’s... fine?

Anyway, try not to die, I guess? Or do. It’s not really my problem. I’ve got a meeting, a dog, and a coffee mug that needs more attention than my wife. Well you know...Good luck, or… whatever… REX GO PEE OUTSIDE!.
    """

    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Define border width (you can adjust this as needed)
    border_width = terminal_width - 4  # 2 spaces padding on each side

    # Create border
    border = "*" * terminal_width

    # Center the message
    centered_message = print_centered_2(message, border_width)

    # Print the bordered and centered message
    print()
    print(border)
    print(f" {centered_message} ")
    print(border)
    print()
def get_user_action():
    while True:
        action = input(print_centered("You've got an unread message. Press Enter to continue or Q to quit: ")).strip().upper()

        if action == "":
            clear_screen()
            # Handle the case where Enter is pressed
            break  # Exit the loop and continue with the rest of the program

        elif action == "Q":
            # Handle the case where 'Q' is pressed
            print(print_centered("Quitting..."))
            sys.exit()
        else:
            # Handle invalid input
            print(print_centered("Invalid input. Please press Enter to continue or Q to quit."))
            clear_screen()
def print_with_border(lines, width=50, funding=None, population=None):
    border = '+' + '-' * (width - 2) + '+'
    
    # Print funding and population
    print(print_centered(border))
    
    if funding is not None and population is not None:
        top_line = f"Funding: ${funding:<20} Population: {population:>10}"
    else:
        top_line = " " * width
        
    print(print_centered(f"|{top_line.center(width - 2)}|"))
    
    # Print menu options with border
    for line in lines:
        print(print_centered(f"|{line.center(width - 2)}|"))
    
    print(print_centered(border))

def display_status(funding, population_ratio, width=80):
    """Print funding and population ratio at the top of the screen."""
    top_line = f"Funding: ${funding:<20} Population: {population_ratio:>10}"
    print(print_centered(top_line))

def HUD_Display(company):
            # Prepare the menu options
        menu_options = [
            "Main Menu:",
            "1) Hire Workers",
            "2) Assign Work",
            "3) Expand Company",
            "5) Exit"
        ]
        # Display the menu options
        
        # Update funding and population values
        funding = company.get_current_funds()  # Ensure this method exists
        population = company.get_population_ratio()  # Ensure this method exists
        display_status(funding,population,width=50)
        # Display the menu with a border and funding/population

        print_with_border(menu_options, width=50)

def main():
    # Create an instance of the Company with starting funds and employees
    company = Company(starting_funds=1200, starting_employee_count=3,max_population=5)
    company.populate_jobs(2,1,0)

    # start menu: "You've got an unread message. Press Enter or Q to quits"

    get_user_action()
    
    display_message()

    while True:
        action = input(print_centered("Press Enter to continue or Q to quit: ")).strip().upper()
        if action == "":
            clear_screen()
            break
        elif action == "Q":
            # Handle the case where 'Q' is pressed
            print(print_centered("Quitting..."))
            sys.exit()
        else:
            # Handle invalid input
            print(print_centered("Invalid input. Please press Enter to continue or Q to quit."))
            clear_screen()

    
    # just press enter to continue "
    HUD_Display(company)

    while True:

        action = int(input("Choose an option(1-5):\n"))
        clear_screen()
        if action == 1: 
            worker_count = int(input("Enter the number of workers:\n"))
            company.hire_workers(worker_count)
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 5:
            print("Exiting game.")
            break
        HUD_Display(company)
        
if __name__ == "__main__":
    main()

