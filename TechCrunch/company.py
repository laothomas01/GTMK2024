# # from assignment import Assignment
import random 
class Company:
    def __init__(self,starting_funds,starting_employee_count):
        self.current_funds = starting_funds
        self.max_employee_count = starting_employee_count
        self.current_available_employee_count = self.max_employee_count
        self.completed_jobs = 0
        self.failed_jobs = 0
        self.selected_jobs = []
        # will probably have to append these jobs from somewhere else 
        self.print_available_jobs = {}
        self.available_jobs = {}
        # self.available_jobs = {
        #         "Job A": {
        #             "name": "Job A",
        #             "cost": 10,
        #             "progress": 0,
        #             "max_progress": 2,
        #             "assigned_employee_count": 0,
        #             "deadline": 4,
        #             "reward" : 50,
        #             "difficulty": "Easy",
        #             "is_available:" : 1
        #         }
        #         ,
        #         "Job B": {
        #             "name": "Job B",
        #             "cost": 20,
        #             "progress": 0,
        #             "max_progress": 4,
        #             "assigned_employee_count": 0,
        #             "deadline": 8,
        #             "reward" : 100,
        #             "difficulty": "Medium",
        #             "is_available:" :1

        #             },
        #         "Job C": {
        #             "name": "Job C",
        #             "cost": 30,
        #             "progress": 0,
        #             "max_progress": 6,
        #             "assigned_employee_count": 0,
        #             "deadline": 12,
        #             "reward" : 200,
        #             "difficulty": "Hard",
        #             "is_available:" : 1
        #             }
        # }
    # def remove_available_job(self,job_name):
    #     if job_name in self.available_jobs:
    #         self.available_jobs[job_name]['is_available'] = 1

    def display_random_jobs(self, count=3):
        """Select and display a specified number of random jobs from available jobs."""
        if not self.available_jobs:
            print("No available jobs to display.")
            return
        
        # Get a list of job names
        job_names = list(self.available_jobs.keys())
        
        # Ensure there are enough jobs to sample
        if len(job_names) < count:
            count = len(job_names)
        
        # Select random job names
        selected_jobs = random.sample(job_names, count)
        
        # Display details for each selected job
        print(f"Displaying {count} random available jobs:")
        for job_name in selected_jobs:
            self.print_available_job(job_name)
            print()  # Adds a blank line between jobs

    def populate_available_jobs(self):
        for i in range(1,300):
            job_name = f"Job {chr(65 + (i // 26))}{chr(65 + (i % 26))}"
            self.available_jobs[job_name] = {
                "name": job_name,
                "cost": 10 + (i % 5) * 10,
                "progress": 0,
                "max_progress": 2 + (i % 5) * 2,
                "assigned_employee_count": 0,
                "deadline": 4 + (i % 5) * 4,
                "reward": 50 + (i % 5) * 50,
                "difficulty": ["Easy", "Medium", "Hard"][(i % 3)],
                "is_available": 1
            }

    def display_available_jobs(self):
         for job_name, job_details in self.available_jobs.items():
                print(f"Job Name: {job_name}")
                for key, value in job_details.items():
                    print(f"  {key}: {value}")
                print()  # Adds a blank line between jobs
    
    def print_available_job(self, job_name):
        if job_name in self.available_jobs:
            job_details = self.available_jobs[job_name]
            print(f"Job Name: {job_name}")
            for key, value in job_details.items():
                print(f"  {key}: {value}")
        else:
            print(f"Job '{job_name}' not found in available jobs.")
    

    def get_selected_jobs_size(self):
        return len(self.selected_jobs)
    
    def print_selected_jobs(self):
        if self.selected_jobs:
            for job in self.selected_jobs:
                print(f"Job Name: {job['name']}")
                for key, value in job.items():
                    print(f"  {key}: {value}")
                print()  # Adds a blank line between jobs
        else:
            print("No jobs have been selected.")
    
    # def add_available_job(self, job_name, job_details):
    #     """Add a job to the list of available jobs."""
    #     self.available_jobs[job_name] = job_details
    #     print(f"Job '{job_name}' has been added to available jobs.")
   
    def add_selected_job(self, job_name):
        """Add a job to the list of selected jobs if it exists in available jobs."""
        if job_name in self.available_jobs:
            self.available_jobs[job_name]['is_available'] = 0
            self.selected_jobs.append(self.available_jobs[job_name])
            self.decrease_current_funds(self.available_jobs[job_name]['cost'])
            print(f"Job '{job_name}' has been added to selected jobs.")
        else:
            print(f"Job '{job_name}' not found in available jobs.")

    def remove_selected_job(self, job_name):
        """Remove a job from the list of selected jobs if it exists."""
        for job in self.selected_jobs:
            if job['name'] == job_name:
                self.available_jobs[job_name]['is_available'] = 1
                self.selected_jobs.remove(job)
                print(f"Job '{job_name}' has been removed from selected jobs.")
                return
        print(f"Job '{job_name}' not found in selected jobs.")

    def update_selected_job_progress(self, job_name, progress_amount):
        for job in self.selected_jobs:
            if job['name'] == job_name:
                # Update the 'progress' key in the job dictionary
                job['progress'] += progress_amount
                
                # Ensure the progress does not exceed max progress
                if job['progress'] > job['max_progress']:
                    job['progress'] = job['max_progress']
                
                print(f"Updated progress for {job_name} to {job['progress']}.")
                return
        print(f"Job '{job_name}' not found in selected jobs.")
    
    def update_selected_assigned_employee_count(self, job_name, assigned_employee_count):
        for job in self.selected_jobs:
            if job['name'] == job_name:
                # # Update the 'progress' key in the job dictionary
                if assigned_employee_count >= self.current_available_employee_count:
                    assigned_employee_count = self.current_available_employee_count
                    job['assigned_employee_count'] += assigned_employee_count
                    self.decrease_max_employee_count(assigned_employee_count)
                elif assigned_employee_count > 0:
                     job['assigned_employee_count'] += assigned_employee_count
                     self.decrease_available_employee_count(assigned_employee_count)
                
                print(f"Updated assigned_employee_count for {job_name} to {job['assigned_employee_count']}.")
                return
        print(f"Job '{job_name}' not found in selected jobs.")

    def update_selected_job_deadline(self,job_name,deadline_update_amount):
        for job in self.selected_jobs:
            if job['name'] == job_name:
                job['deadline'] -= deadline_update_amount

                if job['deadline'] <= 0:
                    job['deadline'] = 0
                
    def increase_max_employee_count(self,amount):
        self.max_employee_count += amount 
    def increase_available_employee_count(self,amount):
        self.current_available_employee_count += amount 
    def decrease_max_employee_count(self,amount):
        self.max_employee_count -= amount 
    def decrease_available_employee_count(self,amount):
        self.current_available_employee_count += amount 
    
    def get_max_employee_count(self):
        return self.max_employee_count
    def get_current_employee_count(self):
        return self.current_available_employee_count
    
    def increase_current_funds(self,amount):
        self.current_funds += amount

    def decrease_current_funds(self,amount):
        self.current_funds -= amount 
    
    def update_current_funds(self,amount):
        self.current_funds = amount 
    
    def check_company_status(self):
        if self.selected_jobs:
            for job in self.selected_jobs:
                if job['assigned_employee_count']:
                    self.update_selected_job_progress(job['name'],job['assigned_employee_count'])
                if job['progress'] >= job['max_progress']:
                    self.increase_available_employee_count(job['assigned_employee_count'])
                    self.increase_current_funds(job['reward'])
                    self.completed_jobs += 1
                    self.remove_selected_job(job['name'])
                else:
                    # will need to replace this magic number 
                    self.update_selected_job_deadline(job['name'],1)
                if job['deadline'] <= 0:
                    print(f"Job '{job['name']}' has missed the deadline")
                    self.failed_jobs += 1
                    self.remove_selected_job(job['name'])
        else:
            print('Nothing to report')
    def print_status_report(self):
            
            # Print current funds
            print(f"Current Funds: ${self.current_funds}")

            print(f"Current Max Employee Count: {self.max_employee_count}")

            # Print current available employee count
            print(f"Current Available Employee Count: {self.current_available_employee_count}")

            # Print total number of jobs completed
            print(f"Total Number of Jobs Completed: {self.completed_jobs}")
            print(f"Total Number of Jobs Failed: {self.failed_jobs}")
            if len(self.selected_jobs):
                self.print_selected_jobs()
            else:
                print("No jobs currently selected")