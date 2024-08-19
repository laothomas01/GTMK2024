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
            self.company = Company(300,3)
            self.company.populate_available_jobs()
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
            while begin_game:
                # Handle game logic here 
                        
                if self.company.dead:
                    print("You are dead")
                    begin_game = False 
            
            
            
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
        
def main():
    # Instantiate and start the game
    game = Game()
    game.test_company_api()

    # game.start()
    

    
if __name__ == "__main__":
    main()
