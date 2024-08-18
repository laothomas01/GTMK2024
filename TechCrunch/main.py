import shutil
from company import Company

class Game:
    def __init__(self):
        self.company = None

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
        self.greet_player()
        self.company = Company(300, 3)
        self.company.populate_available_jobs()
        
        run = True
        
        while run:
            # Display current status
            # Display available jobs
              
            # self.print_centered("Available Jobs:")
            # self.company.display_random_jobs(count=3)
            # print()
            
            # Display dialog message
            print(self.print_centered("You have unread messages. Press Enter to view them."))
            user_input = input()
            if user_input == "":
                # Call the display_random_jobs function again or perform another action
                self.print_centered("Displaying more random available jobs:")
                self.company.display_random_jobs(count=3)
                print()
                
                # Get player input
                action = input(self.print_centered("Choose an action:\n(1) Select a job\n(2) Hire more employees\n(3) View Selected Jobs\n(4) Do Nothing\n(5) Exit Game\n"))

                if action == "1":
                    job_name = input(self.print_centered("Enter the name of the job to select: "))
                    self.company.add_selected_job(job_name)
                elif action == "2":
                    number_of_employees = int(input(self.print_centered("Enter the number of employees to hire: ")))
                    self.company.increase_available_employee_count(number_of_employees)
                    self.print_centered(f"Hired {number_of_employees} new employees.")
                elif action == "3":
                    self.company.print_selected_jobs()
                elif action == "4":
                    self.print_centered("Doing nothing...")
                elif action == "5":
                    run = False
                    self.print_centered("Thank you for playing CEO Simulator 2024! Goodbye!")
                else:
                    self.print_centered("Invalid action. Please choose again.")
            else:
                print('You have unread messages. Press Enter to view them.')


        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
