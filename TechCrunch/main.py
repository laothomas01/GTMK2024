import shutil
from company import Company
import sys
"""
Features list:
[] event manager
[] assign employees to job
[] add check for how player loses 
[] tutorial section
[] update job names(game polishing)
[] connect events with how they affect the company
[] make sure core gameplay is down before any extra feature is created <--------
    [] make sure backend functionality function with front end 
[] add more interactable options 
[] allow the game to scale based on increasing difficulty
[] make sure the game progresses in difficulty
[] should there be an energy system? 
[] action pointer/energy system can add complexity to this game 
[] allow player to customize their name
[] should employees cost money? 

"""
import sys
import shutil

class Game:
    def __init__(self):
        self.company = None
    def test_hire_employees(self):
        company = Company(starting_funds=1000, starting_employee_count=5)
        
        while not company.is_dead():
            try:
                choice = int(input("Enter the number of employees to hire: "))
                company.hire_workers(choice)
            except ValueError:
                print("Please enter a valid number.")
            
            # Display company status after each hiring attempt
            print(f"Current Funds: ${company.get_funds()}")
            print(f"Current Max Employee Count: {company.max_employee_count}")
            # print(f"Current Available Employee Count: {company.available_employee_count}")
            
            if company.is_dead():
                print("Company has run out of funds. Game over!")
                break
    def test_assign_employees(self):
        pass       


    # Test script for Company class
    def small_game_test(self):
        # Initialize the Company
        company = Company(starting_funds=1000, starting_employee_count=5)

        # Populate initial jobs
        company.populate_jobs(num_easy=3, num_medium=2, num_hard=1)

        while not company.is_dead():
            # Display available jobs
            company.display_available_jobs()

            # User chooses to queue a job
            job_name = input("Enter the job name you want to queue (or type 'exit' to quit): ")
            if job_name.lower() == 'exit':
                break

            company.queue_job(job_name)
            company.display_queued_jobs()

            # User chooses to hire workers
            workers_to_hire = int(input("Enter the number of workers to hire: "))
            company.hire_workers(workers_to_hire)

            # User chooses to assign workers to a job
            job_to_assign = input("Enter the job name you want to assign workers to: ")
            workers_to_assign = int(input("Enter the number of workers to assign: "))
            company.assign_workers_to_job(job_to_assign, workers_to_assign)

            # Process the turn
            company.check_company_status()
            company.print_status_report()

            # Advance to next quarter
            company.advance_quarter()
            company.print_status_report()
    def run_tests(self):
        # Initialize Company with starting funds and employees
        company = Company(starting_funds=5000, starting_employee_count=10)
        
        # Display initial status
        print("Initial Company Status:")
        company.check_company_status()
        print("\n")
        
        # Advance to Quarter 2 and update job difficulties
        company.advance_quarter()
        print("Status after advancing to Quarter 2:")
        company.check_company_status()
        print("\n")
        
        # Advance to Quarter 4 and update job difficulties
        company.advance_quarter()
        company.advance_quarter()
        print("Status after advancing to Quarter 4:")
        company.check_company_status()
        print("\n")
        
        # Advance to Quarter 6 and update job difficulties
        company.advance_quarter()
        company.advance_quarter()
        print("Status after advancing to Quarter 6:")
        company.check_company_status()
        print("\n")
        
        # Test hiring workers
        print("Hiring 5 workers:")
        company.hire_workers(5)
        company.check_company_status()
        print("\n")
        
        # Test assigning workers to a job
        print("Assigning 3 workers to 'EasyJobA':")
        company.assign_workers_to_job("EasyJobA", 3)
        company.check_company_status()
        print("\n")
        
        # Test displaying random jobs
        print("Displaying 3 random jobs:")
        company.display_random_jobs(3)
        print("\n")
        
        # Test job queuing and processing
        print("Queueing 'EasyJobA':")
        company.queue_job("EasyJobA")
        company.process_queued_jobs()
        company.check_company_status()

    def test_company_api(self):
        # Initialize company
        company = Company(starting_funds=1000, starting_employee_count=10)
        
        # Populate available jobs
        company.populate_available_jobs()
        
        # Display and select easy jobs
        easy_jobs = company.find_easy_jobs()
        print("Easy Jobs Available:")
        for i, job in enumerate(easy_jobs, 1):
            print(f"{i}. {job}")
        selected_easy_jobs = [easy_jobs[int(input("Select an easy job by number: ")) - 1]]
        
        # Display and select medium jobs
        medium_jobs = company.find_medium_jobs()
        print("Medium Jobs Available:")
        for i, job in enumerate(medium_jobs, 1):
            print(f"{i}. {job}")
        selected_medium_jobs = [medium_jobs[int(input("Select a medium job by number: ")) - 1]]
        
        # Display and select hard jobs
        hard_jobs = company.find_hard_jobs()
        print("Hard Jobs Available:")
        for i, job in enumerate(hard_jobs, 1):
            print(f"{i}. {job}")
        selected_hard_jobs = [hard_jobs[int(input("Select a hard job by number: ")) - 1]]
        
        # Assign workers to selected jobs
        worker_count = int(input("Enter number of workers to assign to each selected job: "))
        
        for job_name in selected_easy_jobs + selected_medium_jobs + selected_hard_jobs:
            cost_per_worker = company.get_cost_per_worker(job_name)
            if cost_per_worker:
                company.assign_workers_to_job(job_name, worker_count)
        
        # Display queued jobs
        company.display_queued_jobs()
        
        # Call check company status
        company.check_company_status()
        
        # Print status
        company.print_status_report()

        # Test hiring of workers
        hire_count = int(input("Enter number of workers to hire: "))
        # hire_cost_per_worker = int(input("Enter cost per worker to hire: "))
        
        company.hire_workers(hire_count, hire_cost_per_worker)
        
        # Print status after hiring workers
        company.print_status_report()


    def greet_player(self):
        console_width = shutil.get_terminal_size().columns
        greeting = "Welcome to CEO Simulator 2024!"
        welcome_message = "It's your first day as CEO, and the company is looking forward to working with you."
        print(greeting.center(console_width))
        print(welcome_message.center(console_width))
        print()  # Adds a blank line for spacing

    def print_centered(self, text):
        console_width = shutil.get_terminal_size().columns
        return text.center(console_width)
    
    def start(self):
        run = True 
        while run:
            self.greet_player()
            press_start = False 
            begin_game = False 
            while not press_start:
                print(self.print_centered("You have unread messages. Press Enter to view them or Q to quit"))
                user_input = input()
                if user_input.lower() == "q":
                    print(self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!"))
                    sys.exit()
                elif user_input == "":
                    begin_game = True 
                    press_start = True 
                else:
                    print(self.print_centered("Invalid Input"))

            # Start initialization of data 
            self.company = Company(starting_funds=1000, starting_employee_count=3)
            self.company.populate_jobs(num_easy=1, num_medium=1, num_hard=1)
            print(self.print_centered(f"Beginning 1st Quarter"))
            print(self.print_centered("Available Jobs"))
            




            while begin_game:
                pass
                # Handle game logic here 
                

                # if self.company.dead:
                #     print("You are dead")
                #     begin_game = False 
                
                
            
            
            
            print(self.print_centered("Would you like to restart? (Y/N)"))
            restart_input = input().lower()
            restarting = True 
            while restarting:
                if restart_input == "n":
                    print(self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!"))
                    run = False
                    restarting = False 
                elif restart_input == "y":
                    press_start = False 
                    begin_game = False 
                    restarting = False 
                else:
                    print(self.print_centered("Invalid Input"))
        sys.exit()
    # # Example usage
    # def test_company_progression(self):
    #     company = Company(starting_funds=2000, starting_employee_count=10)
    #     company.populate_jobs(num_easy=1, num_medium=1, num_hard=1)
        
    #     # Display initial job list
    #     print("Initial Jobs:")
    #     company.display_available_jobs()
        
    #     # Simulate progression through quarters
    #     for _ in range(5):  # Example: 5 quarters
    #         print(f"\nQuarter {company.current_quarter}")
    #         company.advance_quarter()
    #         print("Jobs after advancement:")
    #         company.display_available_jobs()
            
    #         # Get random jobs
    #         random_easy_job = company.get_random_job("Easy")
    #         random_medium_job = company.get_random_job("Medium")
    #         random_hard_job = company.get_random_job("Hard")
            
    #         print(f"Random Easy Job: {random_easy_job}")
    #         print(f"Random Medium Job: {random_medium_job}")
    #         print(f"Random Hard Job: {random_hard_job}")       
def main():
    # Instantiate and start the game
    game = Game()
    game.test_hire_employees()
    # game.small_game_test()
    
    # game.run_tests()
    
if __name__ == "__main__":
    main()
