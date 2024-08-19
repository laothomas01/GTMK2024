# # # # from assignment import Assignment
# # import random 
# # class Company:
# #     def __init__(self,starting_funds,starting_employee_count):
# #         self.current_funds = starting_funds
# #         self.max_employee_count = starting_employee_count
# #         self.current_available_employee_count = self.max_employee_count
# #         self.completed_jobs = 0
# #         self.failed_jobs = 0
# #         # will probably have to append these jobs from somewhere else 
# #         self.available_jobs = {}
# #         self.dead = False

# #     def display_random_jobs(self, count=3):
# #         """Select and display a specified number of random jobs from available jobs."""
# #         if not self.available_jobs:
# #             print("No available jobs to display.")
# #             return
        
# #         # Get a list of job names
# #         job_names = list(self.available_jobs.keys())
        
# #         # Ensure there are enough jobs to sample
# #         if len(job_names) < count:
# #             count = len(job_names)
        
# #         # Select random job names
# #         selected_jobs = random.sample(job_names, count)
        
# #         # Display details for each selected job
# #         print(f"Displaying {count} random available jobs:")
# #         for job_name in selected_jobs:
# #             self.print_available_job(job_name)
# #             print()  # Adds a blank line between jobs

# #     def populate_available_jobs(self):
# #         for i in range(1,300):
# #             job_name = f"Job {chr(65 + (i // 26))}{chr(65 + (i % 26))}"
# #             self.available_jobs[job_name] = {
# #                 "name": job_name,
# #                 "cost_per_worker": 10 + (i % 5) * 10,
# #                 "progress": 0,
# #                 "max_progress": 2 + (i % 5) * 2,
# #                 "assigned_employee_count": 0,
# #                 "deadline": 4 + (i % 5) * 4,
# #                 "reward": 50 + (i % 5) * 50,
# #                 "difficulty": ["Easy", "Medium", "Hard"][(i % 3)],
# #             }

# #     def display_available_jobs(self):
# #          for job_name, job_details in self.available_jobs.items():
# #                 print(f"Job Name: {job_name}")
# #                 for key, value in job_details.items():
# #                     print(f"  {key}: {value}")
# #                 print()  # Adds a blank line between jobs
    
# #     def print_available_job(self, job_name):
# #         if job_name in self.available_jobs:
# #             job_details = self.available_jobs[job_name]
# #             print(f"Job Name: {job_name}")
# #             for key, value in job_details.items():
# #                 print(f"  {key}: {value}")
# #         else:
# #             print(f"Job '{job_name}' not found in available jobs.")
    

# #     # def get_selected_jobs_size(self):
# #     #     return len(self.selected_jobs)
    
# #     # def print_selected_jobs(self):
# #     #     if self.selected_jobs:
# #     #         for job in self.selected_jobs:
# #     #             print(f"Job Name: {job['name']}")
# #     #             for key, value in job.items():
# #     #                 print(f"  {key}: {value}")
# #     #             print()  # Adds a blank line between jobs
# #     #     else:
# #     #         print("No jobs have been selected.")
    
# #     # def add_available_job(self, job_name, job_details):
# #     #     """Add a job to the list of available jobs."""
# #     #     self.available_jobs[job_name] = job_details
# #     #     print(f"Job '{job_name}' has been added to available jobs.")
   
# #     # def add_selected_job(self, job_name):
# #     #     """Add a job to the list of selected jobs if it exists in available jobs."""
# #     #     if job_name in self.available_jobs:
# #     #         self.available_jobs[job_name]['is_available'] = 0
# #     #         self.selected_jobs.append(self.available_jobs[job_name])
# #     #         self.decrease_current_funds(self.available_jobs[job_name]['cost'])
# #     #         print(f"Job '{job_name}' has been added to selected jobs.")
# #     #     else:
# #     #         print(f"Job '{job_name}' not found in available jobs.")

# #     # def remove_selected_job(self, job_name):
# #     #     """Remove a job from the list of selected jobs if it exists."""
# #     #     for job in self.selected_jobs:
# #     #         if job['name'] == job_name:
# #     #             self.available_jobs[job_name]['is_available'] = 1
# #     #             self.selected_jobs.remove(job)
# #     #             print(f"Job '{job_name}' has been removed from selected jobs.")
# #     #             return
# #     #     print(f"Job '{job_name}' not found in selected jobs.")

# #     def update_selected_job_progress(self, job_name, progress_amount):
# #         for job in self.selected_jobs:
# #             if job['name'] == job_name:
# #                 # Update the 'progress' key in the job dictionary
# #                 job['progress'] += progress_amount
                
# #                 # Ensure the progress does not exceed max progress
# #                 if job['progress'] > job['max_progress']:
# #                     job['progress'] = job['max_progress']
                
# #                 print(f"Updated progress for {job_name} to {job['progress']}.")
# #                 return
# #         print(f"Job '{job_name}' not found in selected jobs.")
    
# #     def update_selected_assigned_employee_count(self, job_name, assigned_employee_count):
# #         for job in self.selected_jobs:
# #             if job['name'] == job_name:
# #                 # # Update the 'progress' key in the job dictionary
# #                 if assigned_employee_count >= self.current_available_employee_count:
# #                     assigned_employee_count = self.current_available_employee_count
# #                     job['assigned_employee_count'] += assigned_employee_count
# #                     self.decrease_max_employee_count(assigned_employee_count)
# #                 elif assigned_employee_count > 0:
# #                      job['assigned_employee_count'] += assigned_employee_count
# #                      self.decrease_available_employee_count(assigned_employee_count)
                
# #                 print(f"Updated assigned_employee_count for {job_name} to {job['assigned_employee_count']}.")
# #                 return
# #         print(f"Job '{job_name}' not found in selected jobs.")

# #     def update_selected_job_deadline(self,job_name,deadline_update_amount):
# #         for job in self.selected_jobs:
# #             if job['name'] == job_name:
# #                 job['deadline'] -= deadline_update_amount

# #                 if job['deadline'] <= 0:
# #                     job['deadline'] = 0

# #     def assign_workers_to_job(self, job_name, worker_count, cost_per_worker):
# #         total_cost = worker_count * cost_per_worker
# #         if total_cost > self.funds:
# #             print("Not enough funds to assign that many workers.")
# #         elif worker_count > self.current_available_employee_count:
# #             print("Not enough available workers.")
# #         else:
# #             if len(self.selected_jobs):
# #                 self.update_selected_assigned_employee_count(job_name,worker_count)
# #             else:
# #                 print("No jobs to assign employees")

# #     # core mechanic of game 
# #     def hire_workers(self,count,cost_per_worker):
# #         total_cost = count * cost_per_worker 
# #         if total_cost > self.current_funds:
# #             print("Not enough funds to hire that many workers.")
# #         else:
# #             self.increase_max_employee_count(count)
# #             self.increase_available_employee_count(count)
# #         self.decrease_current_funds(total_cost)

# #     def increase_max_employee_count(self,amount):
# #         self.max_employee_count += amount 
        
# #     def increase_available_employee_count(self,amount):
# #         self.current_available_employee_count += amount 
# #     def decrease_max_employee_count(self,amount):
# #         self.max_employee_count -= amount 
# #     def decrease_available_employee_count(self,amount):
# #         self.current_available_employee_count += amount 
    
# #     def get_max_employee_count(self):
# #         return self.max_employee_count
# #     def get_current_employee_count(self):
# #         return self.current_available_employee_count
    
# #     def increase_current_funds(self,amount):
# #         self.current_funds += amount

# #     def decrease_current_funds(self,amount):
# #         self.current_funds -= amount 
    
# #     def update_current_funds(self,amount):
# #         self.current_funds = amount 
# #     def update_company_is_dead(self,is_dead):
# #         self.dead = is_dead
# #     def is_dead(self):
# #         return self.dead 
# #     def check_company_status(self):
# #         if self.dead:
# #             self.update_company_is_dead(True)
# #         else:
# #             # display informationa bout selecting jobs 
# #             if self.selected_jobs:
# #                 for job in self.selected_jobs:
# #                     if job['assigned_employee_count']:
# #                         self.update_selected_job_progress(job['name'],job['assigned_employee_count'])
# #                     if job['progress'] >= job['max_progress']:
# #                         self.increase_available_employee_count(job['assigned_employee_count'])
# #                         self.increase_current_funds(job['reward'])
# #                         self.completed_jobs += 1
# #                         self.remove_selected_job(job['name'])
# #                     else:
# #                         # will need to replace this magic number 
# #                         self.update_selected_job_deadline(job['name'],1)
# #                     if job['deadline'] <= 0:
# #                         print(f"Job '{job['name']}' has missed the deadline")
# #                         self.failed_jobs += 1
# #                         self.remove_selected_job(job['name'])
# #             else:
# #                 print('No select jobs to report')

# #     def print_status_report(self):
            
# #             # Print current funds
# #             print(f"Current Funds: ${self.current_funds}")

# #             print(f"Current Max Employee Count: {self.max_employee_count}")

# #             # Print current available employee count
# #             print(f"Current Available Employee Count: {self.current_available_employee_count}")

# #             # Print total number of jobs completed
# #             print(f"Total Number of Jobs Completed: {self.completed_jobs}")
# #             print(f"Total Number of Jobs Failed: {self.failed_jobs}")
# #             if len(self.selected_jobs):
# #                 self.print_selected_jobs()
# #             else:
# #                 print("No jobs currently selected")


# import random

# class Company:
#     def __init__(self, starting_funds, starting_employee_count):
#         self.current_funds = starting_funds
#         self.max_employee_count = starting_employee_count
#         self.current_available_employee_count = self.max_employee_count
#         self.completed_jobs = 0
#         self.failed_jobs = 0
#         self.available_jobs = {}
#         self.jobs_queue = []
#         self.dead = False


#     def display_random_jobs(self, count=3):
#         """Select and display a specified number of random jobs from available jobs."""
#         if not self.available_jobs:
#             print("No available jobs to display.")
#             return
        
#         # Get a list of job names
#         job_names = list(self.available_jobs.keys())
        
#         # Ensure there are enough jobs to sample
#         if len(job_names) < count:
#             count = len(job_names)
        
#         # Select random job names
#         selected_jobs = random.sample(job_names, count)
        
#         # Display details for each selected job
#         print(f"Displaying {count} random available jobs:")
#         for job_name in selected_jobs:
#             self.print_available_job(job_name)
#             print()  # Adds a blank line between jobs

#     def populate_available_jobs(self):
#         for i in range(1, 300):
#             job_name = f"Job {chr(65 + (i // 26))}{chr(65 + (i % 26))}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 10 + (i % 5) * 10,
#                 "progress": 0,
#                 "max_progress": 2 + (i % 5) * 2,
#                 "assigned_employee_count": 0,
#                 "deadline": 4 + (i % 5) * 4,
#                 "reward": 50 + (i % 5) * 50,
#                 "difficulty": ["Easy", "Medium", "Hard"][(i % 3)],
#             }

#     def queue_in_progress_job(self, job_name):
#         if job_name in self.available_jobs:
#             # Remove the job from available_jobs and add to jobs_queue
#             # job_details = self.available_jobs.pop(job_name)
#             # self.jobs_queue.append(job_)
#             self.jobs_queue.append(self.available_jobs[job_name])
#             print(f"Job '{job_name}' has been queued for processing.")
#         else:
#             print(f"Job '{job_name}' is not available.")
            
#     def queue_job(self, job_name):
#         if job_name in self.available_jobs:
#             # Remove the job from available_jobs and add to jobs_queue
#             job_details = self.available_jobs.pop(job_name)
#             self.jobs_queue.append({"name": job_name, "details": job_details})
#             print(f"Job '{job_name}' has been queued for processing.")
#         else:
#             print(f"Job '{job_name}' is not available.")
        
#     def display_queued_jobs(self):
#         print("Jobs in Queue:")
#         if not self.jobs_queue:
#             print("  No jobs in the queue.")
#         for job in self.jobs_queue:
#             print(f"    Job Name: {job['name']}")
#             print(f"    Deadline: {job['deadline']}")
#             print(f"    Progress: {job['progress']}")
#             print(f"    Assigned Employee Count: {job['assigned_employee_count']}")
#             print()
#         else:
#             print("No jobs in progress")

#     def display_available_jobs(self):
#         for job_name, job_details in self.available_jobs.items():
#             print(f"Job Name: {job_name}")
#             for key, value in job_details.items():
#                 print(f"  {key}: {value}")
#             print()  # Adds a blank line between jobs
    
#     def print_available_job(self, job_name):
#         if job_name in self.available_jobs:
#             job_details = self.available_jobs[job_name]
#             print(f"Job Name: {job_name}")
#             for key, value in job_details.items():
#                 print(f"  {key}: {value}")
#         else:
#             print(f"Job '{job_name}' not found in available jobs.")
    
#     def assign_workers_to_job(self, job_name, worker_count):
#         """Assign workers to a job and handle the associated costs."""
#         if job_name not in self.available_jobs:
#             print(f"Job '{job_name}' not found.")
#             return
        
#         job = self.available_jobs[job_name]
#         total_cost = worker_count * job["cost_per_worker"]
        
#         if total_cost > self.current_funds:
#             print("Not enough funds to assign that many workers.")
#         elif worker_count > self.current_available_employee_count:
#             print("Not enough available workers.")
#         else:
#             job["assigned_employee_count"] += worker_count
#             self.decrease_current_funds(total_cost)
#             self.decrease_available_employee_count(worker_count)
#             print(f"Assigned {worker_count} workers to job '{job_name}'.")

#     def hire_workers(self, count, cost_per_worker):
#         """Hire workers and handle the associated costs."""
#         total_cost = count * cost_per_worker
#         if total_cost > self.current_funds:
#             print("Not enough funds to hire that many workers.")
#         else:
#             self.increase_max_employee_count(count)
#             self.increase_available_employee_count(count)
#             self.decrease_current_funds(total_cost)
#             print(f"Hired {count} workers.")

#     def increase_max_employee_count(self, amount):
#         self.max_employee_count += amount 
        
#     def increase_available_employee_count(self, amount):
#         self.current_available_employee_count += amount 
        
#     def decrease_max_employee_count(self, amount):
#         self.max_employee_count -= amount 
        
#     def decrease_available_employee_count(self, amount):
#         self.current_available_employee_count -= amount 
    
#     def get_max_employee_count(self):
#         return self.max_employee_count
    
#     def get_current_employee_count(self):
#         return self.current_available_employee_count
    
#     def increase_current_funds(self, amount):
#         self.current_funds += amount

#     def decrease_current_funds(self, amount):
#         self.current_funds -= amount 
    
#     def update_current_funds(self, amount):
#         self.current_funds = amount 
    
#     def update_company_is_dead(self, is_dead):
#         self.dead = is_dead
    
#     def is_dead(self):
#         return self.dead 
    
#     def check_company_status(self):
#         if self.dead:
#             print("The company is dead.")
#         else:
#             for job_name, job in list(self.available_jobs.items()):
#                 if job["assigned_employee_count"]:
#                     # Update the 'progress' key in the job dictionary
#                     job["progress"] += job["assigned_employee_count"]
                    
#                     # Ensure the progress does not exceed max progress
#                     if job["progress"] > job["max_progress"]:
#                         job["progress"] = job["max_progress"]
                    
#                     # Check job status
#                     if job["progress"] >= job["max_progress"]:
#                         self.increase_available_employee_count(job["assigned_employee_count"])
#                         self.increase_current_funds(job["reward"])
#                         self.completed_jobs += 1
#                         del self.available_jobs[job_name]
#                         print(f"Job '{job_name}' completed.")
#                     else:
#                         # Update job deadline
#                         job["deadline"] -= 1
#                         if job["deadline"] <= 0:
#                             print(f"Job '{job_name}' has missed the deadline.")
#                             self.failed_jobs += 1
#                             del self.available_jobs[job_name]

#     def print_status_report(self):
#         """Print the status report of the company."""
#         print(f"Current Funds: ${self.current_funds}")
#         print(f"Current Max Employee Count: {self.max_employee_count}")
#         print(f"Current Available Employee Count: {self.current_available_employee_count}")
#         print(f"Total Number of Jobs Completed: {self.completed_jobs}")
#         print(f"Total Number of Jobs Failed: {self.failed_jobs}")
        
#         if self.available_jobs:
#             self.display_available_jobs()
#         else:
#             print("No jobs available.")

#     def find_easy_jobs(self, count=3):
#         """Find and return a specified number of easy jobs from available jobs."""
#         easy_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Easy"]
        
#         # Ensure there are enough easy jobs to sample
#         if len(easy_jobs) < count:
#             count = len(easy_jobs)
        
#         # Select the easy jobs
#         selected_easy_jobs = random.sample(easy_jobs, count) if easy_jobs else []
        
#         # Display details for each selected easy job
#         print(f"Displaying {count} easy jobs:")
#         for job_name in selected_easy_jobs:
#             self.print_available_job(job_name)
#             print()  # Adds a blank line between jobs

#     def find_medimum_jobs(self, count=3):
#         """Find and return a specified number of easy jobs from available jobs."""
#         medium_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Medium"]
        
#         # Ensure there are enough easy jobs to sample
#         if len(medium_jobs) < count:
#             count = len(medium_jobs)
        
#         # Select the easy jobs
#         selected_medium_jobs = random.sample(medium_jobs, count) if medium_jobs else []
        
#         # Display details for each selected easy job
#         print(f"Displaying {count} medium jobs:")
#         for job_name in selected_medium_jobs:
#             self.print_available_job(job_name)
#             print()  # Adds a blank line between jobs

#     def find_hard_jobs(self, count=3):
#         """Find and return a specified number of easy jobs from available jobs."""
#         hard_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Hard"]
        
#         # Ensure there are enough easy jobs to sample
#         if len(hard_jobs) < count:
#             count = len(hard_jobs)
        
#         # Select the easy jobs
#         selected_hard_jobs = random.sample(hard_jobs, count) if hard_jobs else []
        
#         # Display details for each selected easy job
#         print(f"Displaying {count} hard jobs:")
#         for job_name in selected_hard_jobs:
#             self.print_available_job(job_name)
#             print()  # Adds a blank line between jobs


import random

class Company:
    def __init__(self, starting_funds, starting_employee_count):
        self.current_funds = starting_funds
        self.max_employee_count = starting_employee_count
        self.current_available_employee_count = self.max_employee_count
        self.completed_jobs = 0
        self.failed_jobs = 0
        self.available_jobs = {}
        self.jobs_queue = []
        self.dead = False

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
        for i in range(1, 300):
            job_name = f"Job {chr(65 + (i // 26))}{chr(65 + (i % 26))}"
            self.available_jobs[job_name] = {
                "name": job_name,
                "cost_per_worker": 10 + (i % 5) * 10,
                "progress": 0,
                "max_progress": 2 + (i % 5) * 2,
                "assigned_employee_count": 0,
                "deadline": 4 + (i % 5) * 4,
                "reward": 50 + (i % 5) * 50,
                "difficulty": ["Easy", "Medium", "Hard"][(i % 3)],
            }

    def queue_job(self, job_name):
        """Queue a job for processing."""
        if job_name in self.available_jobs:
            job_details = self.available_jobs.pop(job_name)
            self.jobs_queue.append(job_details)
            print(f"Job '{job_name}' has been queued for processing.")
        else:
            print(f"Job '{job_name}' is not available.")
        
    def display_queued_jobs(self):
        """Display the jobs currently in the queue."""
        if not self.jobs_queue:
            print("No jobs in the queue.")
        else:
            print("Jobs in Queue:")
            for job in self.jobs_queue:
                print(f"  Job Name: {job['name']}")
                print(f"  Deadline: {job['deadline']}")
                print(f"  Progress: {job['progress']}")
                print(f"  Assigned Employee Count: {job['assigned_employee_count']}")
                print()
    def process_queued_jobs(self):
        """Process each queued job and handle completion, rewards, and removal from the queue."""
        if not self.jobs_queue:
            print("No jobs in the queue")
        else:
            for job in self.jobs_queue[:]:  # Iterate over a copy of the queue to modify it during iteration
                if job["progress"] >= job["max_progress"]:
                    # Job is complete, process reward and update statistics
                    self.increase_current_funds(job["reward"])
                    self.completed_jobs += 1
                    self.jobs_queue.remove(job)  # Remove the job from the queue
                    print(f"Job '{job['name']}' completed and reward of ${job['reward']} added to funds.")
                else:
                    # Job is not yet complete, skip to next job
                    continue
   
    def display_available_jobs(self):
        """Display all available jobs."""
        if not self.available_jobs:
            print("No available jobs.")
        else:
            for job_name, job_details in self.available_jobs.items():
                print(f"Job Name: {job_name}")
                for key, value in job_details.items():
                    print(f"  {key}: {value}")
                print()  # Adds a blank line between jobs
    
    def print_available_job(self, job_name):
        """Print details of a specific available job."""
        if job_name in self.available_jobs:
            job_details = self.available_jobs[job_name]
            print(f"Job Name: {job_name}")
            for key, value in job_details.items():
                print(f"  {key}: {value}")
        else:
            print(f"Job '{job_name}' not found in available jobs.")
    
    def assign_workers_to_job(self, job_name, worker_count):
        """Assign workers to a job and handle the associated costs."""
        if job_name not in self.available_jobs:
            print(f"Job '{job_name}' not found.")
            return
        
        job = self.available_jobs[job_name]
        total_cost = worker_count * job["cost_per_worker"]
        
        if total_cost > self.current_funds:
            print("Not enough funds to assign that many workers.")
        elif worker_count > self.current_available_employee_count:
            print("Not enough available workers.")
        else:
            job["assigned_employee_count"] += worker_count
            self.decrease_current_funds(total_cost)
            self.decrease_available_employee_count(worker_count)
            print(f"Assigned {worker_count} workers to job '{job_name}'.")


    def hire_workers(self, count, cost_per_worker):
        """Hire workers and handle the associated costs."""
        total_cost = count * cost_per_worker
        if total_cost > self.current_funds:
            print("Not enough funds to hire that many workers.")
        else:
            self.increase_max_employee_count(count)
            self.increase_available_employee_count(count)
            self.decrease_current_funds(total_cost)
            print(f"Hired {count} workers.")
    
    def get_cost_per_worker(self, job_name):
            """Get the cost per worker for a specific job."""
            if job_name in self.available_jobs:
                return self.available_jobs[job_name]["cost_per_worker"]
            else:
                print(f"Job '{job_name}' not found.")
                return None

    def increase_max_employee_count(self, amount):
        self.max_employee_count += amount 
        
    def increase_available_employee_count(self, amount):
        self.current_available_employee_count += amount 
        
    def decrease_max_employee_count(self, amount):
        self.max_employee_count -= amount 
        
    def decrease_available_employee_count(self, amount):
        self.current_available_employee_count -= amount 
    
    def get_max_employee_count(self):
        return self.max_employee_count
    
    def get_current_employee_count(self):
        return self.current_available_employee_count
    
    def increase_current_funds(self, amount):
        self.current_funds += amount

    def decrease_current_funds(self, amount):
        self.current_funds -= amount 
    
    def update_current_funds(self, amount):
        self.current_funds = amount 
    
    def update_company_is_dead(self, is_dead):
        self.dead = is_dead
    
    def is_dead(self):
        return self.dead 
    
    def check_company_status(self):
        if self.dead:
            print("The company is dead.")
        else:
            for job in self.jobs_queue[:]:
                if job["assigned_employee_count"]:
                    job["progress"] += job["assigned_employee_count"]
                    
                    if job["progress"] > job["max_progress"]:
                        job["progress"] = job["max_progress"]
                    
                    if job["progress"] >= job["max_progress"]:
                        self.increase_available_employee_count(job["assigned_employee_count"])
                        self.increase_current_funds(job["reward"])
                        self.completed_jobs += 1
                        self.jobs_queue.remove(job)
                        print(f"Job '{job['name']}' completed.")
                    else:
                        job["deadline"] -= 1
                        if job["deadline"] <= 0:
                            print(f"Job '{job['name']}' has missed the deadline.")
                            self.failed_jobs += 1
                            self.jobs_queue.remove(job)

    def print_status_report(self):
        """Print the status report of the company."""
        print(f"Current Funds: ${self.current_funds}")
        print(f"Current Max Employee Count: {self.max_employee_count}")
        print(f"Current Available Employee Count: {self.current_available_employee_count}")
        print(f"Total Number of Jobs Completed: {self.completed_jobs}")
        print(f"Total Number of Jobs Failed: {self.failed_jobs}")
        self.display_queued_jobs()

    def find_easy_jobs(self, count=3):
            """Find and return a specified number of easy jobs from available jobs."""
            easy_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Easy"]
            
            # Ensure there are enough easy jobs to sample
            if len(easy_jobs) < count:
                count = len(easy_jobs)
            
            # Select the easy jobs
            selected_easy_jobs = random.sample(easy_jobs, count) if easy_jobs else []
            return selected_easy_jobs

    def find_medium_jobs(self, count=3):
        """Find and return a specified number of medium jobs from available jobs."""
        medium_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Medium"]
        
        # Ensure there are enough medium jobs to sample
        if len(medium_jobs) < count:
            count = len(medium_jobs)
        
        # Select the medium jobs
        selected_medium_jobs = random.sample(medium_jobs, count) if medium_jobs else []
        return selected_medium_jobs

    def find_hard_jobs(self, count=3):
        """Find and return a specified number of hard jobs from available jobs."""
        hard_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Hard"]
        
        # Ensure there are enough hard jobs to sample
        if len(hard_jobs) < count:
            count = len(hard_jobs)
        
        # Select the hard jobs
        selected_hard_jobs = random.sample(hard_jobs, count) if hard_jobs else []
        return selected_hard_jobs