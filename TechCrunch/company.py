# # # # # from assignment import Assignment
# # # import random 
# # # class Company:
# # #     def __init__(self,starting_funds,starting_employee_count):
# # #         self.current_funds = starting_funds
# # #         self.max_employee_count = starting_employee_count
# # #         self.current_available_employee_count = self.max_employee_count
# # #         self.completed_jobs = 0
# # #         self.failed_jobs = 0
# # #         # will probably have to append these jobs from somewhere else 
# # #         self.available_jobs = {}
# # #         self.dead = False

# # #     def display_random_jobs(self, count=3):
# # #         """Select and display a specified number of random jobs from available jobs."""
# # #         if not self.available_jobs:
# # #             print("No available jobs to display.")
# # #             return
        
# # #         # Get a list of job names
# # #         job_names = list(self.available_jobs.keys())
        
# # #         # Ensure there are enough jobs to sample
# # #         if len(job_names) < count:
# # #             count = len(job_names)
        
# # #         # Select random job names
# # #         selected_jobs = random.sample(job_names, count)
        
# # #         # Display details for each selected job
# # #         print(f"Displaying {count} random available jobs:")
# # #         for job_name in selected_jobs:
# # #             self.print_available_job(job_name)
# # #             print()  # Adds a blank line between jobs

# # #     def populate_available_jobs(self):
# # #         for i in range(1,300):
# # #             job_name = f"Job {chr(65 + (i // 26))}{chr(65 + (i % 26))}"
# # #             self.available_jobs[job_name] = {
# # #                 "name": job_name,
# # #                 "cost_per_worker": 10 + (i % 5) * 10,
# # #                 "progress": 0,
# # #                 "max_progress": 2 + (i % 5) * 2,
# # #                 "assigned_employee_count": 0,
# # #                 "deadline": 4 + (i % 5) * 4,
# # #                 "reward": 50 + (i % 5) * 50,
# # #                 "difficulty": ["Easy", "Medium", "Hard"][(i % 3)],
# # #             }

# # #     def display_available_jobs(self):
# # #          for job_name, job_details in self.available_jobs.items():
# # #                 print(f"Job Name: {job_name}")
# # #                 for key, value in job_details.items():
# # #                     print(f"  {key}: {value}")
# # #                 print()  # Adds a blank line between jobs
    
# # #     def print_available_job(self, job_name):
# # #         if job_name in self.available_jobs:
# # #             job_details = self.available_jobs[job_name]
# # #             print(f"Job Name: {job_name}")
# # #             for key, value in job_details.items():
# # #                 print(f"  {key}: {value}")
# # #         else:
# # #             print(f"Job '{job_name}' not found in available jobs.")
    

# # #     # def get_selected_jobs_size(self):
# # #     #     return len(self.selected_jobs)
    
# # #     # def print_selected_jobs(self):
# # #     #     if self.selected_jobs:
# # #     #         for job in self.selected_jobs:
# # #     #             print(f"Job Name: {job['name']}")
# # #     #             for key, value in job.items():
# # #     #                 print(f"  {key}: {value}")
# # #     #             print()  # Adds a blank line between jobs
# # #     #     else:
# # #     #         print("No jobs have been selected.")
    
# # #     # def add_available_job(self, job_name, job_details):
# # #     #     """Add a job to the list of available jobs."""
# # #     #     self.available_jobs[job_name] = job_details
# # #     #     print(f"Job '{job_name}' has been added to available jobs.")
   
# # #     # def add_selected_job(self, job_name):
# # #     #     """Add a job to the list of selected jobs if it exists in available jobs."""
# # #     #     if job_name in self.available_jobs:
# # #     #         self.available_jobs[job_name]['is_available'] = 0
# # #     #         self.selected_jobs.append(self.available_jobs[job_name])
# # #     #         self.decrease_current_funds(self.available_jobs[job_name]['cost'])
# # #     #         print(f"Job '{job_name}' has been added to selected jobs.")
# # #     #     else:
# # #     #         print(f"Job '{job_name}' not found in available jobs.")

# # #     # def remove_selected_job(self, job_name):
# # #     #     """Remove a job from the list of selected jobs if it exists."""
# # #     #     for job in self.selected_jobs:
# # #     #         if job['name'] == job_name:
# # #     #             self.available_jobs[job_name]['is_available'] = 1
# # #     #             self.selected_jobs.remove(job)
# # #     #             print(f"Job '{job_name}' has been removed from selected jobs.")
# # #     #             return
# # #     #     print(f"Job '{job_name}' not found in selected jobs.")

# # #     def update_selected_job_progress(self, job_name, progress_amount):
# # #         for job in self.selected_jobs:
# # #             if job['name'] == job_name:
# # #                 # Update the 'progress' key in the job dictionary
# # #                 job['progress'] += progress_amount
                
# # #                 # Ensure the progress does not exceed max progress
# # #                 if job['progress'] > job['max_progress']:
# # #                     job['progress'] = job['max_progress']
                
# # #                 print(f"Updated progress for {job_name} to {job['progress']}.")
# # #                 return
# # #         print(f"Job '{job_name}' not found in selected jobs.")
    
# # #     def update_selected_assigned_employee_count(self, job_name, assigned_employee_count):
# # #         for job in self.selected_jobs:
# # #             if job['name'] == job_name:
# # #                 # # Update the 'progress' key in the job dictionary
# # #                 if assigned_employee_count >= self.current_available_employee_count:
# # #                     assigned_employee_count = self.current_available_employee_count
# # #                     job['assigned_employee_count'] += assigned_employee_count
# # #                     self.decrease_max_employee_count(assigned_employee_count)
# # #                 elif assigned_employee_count > 0:
# # #                      job['assigned_employee_count'] += assigned_employee_count
# # #                      self.decrease_available_employee_count(assigned_employee_count)
                
# # #                 print(f"Updated assigned_employee_count for {job_name} to {job['assigned_employee_count']}.")
# # #                 return
# # #         print(f"Job '{job_name}' not found in selected jobs.")

# # #     def update_selected_job_deadline(self,job_name,deadline_update_amount):
# # #         for job in self.selected_jobs:
# # #             if job['name'] == job_name:
# # #                 job['deadline'] -= deadline_update_amount

# # #                 if job['deadline'] <= 0:
# # #                     job['deadline'] = 0

# # #     def assign_workers_to_job(self, job_name, worker_count, cost_per_worker):
# # #         total_cost = worker_count * cost_per_worker
# # #         if total_cost > self.funds:
# # #             print("Not enough funds to assign that many workers.")
# # #         elif worker_count > self.current_available_employee_count:
# # #             print("Not enough available workers.")
# # #         else:
# # #             if len(self.selected_jobs):
# # #                 self.update_selected_assigned_employee_count(job_name,worker_count)
# # #             else:
# # #                 print("No jobs to assign employees")

# # #     # core mechanic of game 
# # #     def hire_workers(self,count,cost_per_worker):
# # #         total_cost = count * cost_per_worker 
# # #         if total_cost > self.current_funds:
# # #             print("Not enough funds to hire that many workers.")
# # #         else:
# # #             self.increase_max_employee_count(count)
# # #             self.increase_available_employee_count(count)
# # #         self.decrease_current_funds(total_cost)

# # #     def increase_max_employee_count(self,amount):
# # #         self.max_employee_count += amount 
        
# # #     def increase_available_employee_count(self,amount):
# # #         self.current_available_employee_count += amount 
# # #     def decrease_max_employee_count(self,amount):
# # #         self.max_employee_count -= amount 
# # #     def decrease_available_employee_count(self,amount):
# # #         self.current_available_employee_count += amount 
    
# # #     def get_max_employee_count(self):
# # #         return self.max_employee_count
# # #     def get_current_employee_count(self):
# # #         return self.current_available_employee_count
    
# # #     def increase_current_funds(self,amount):
# # #         self.current_funds += amount

# # #     def decrease_current_funds(self,amount):
# # #         self.current_funds -= amount 
    
# # #     def update_current_funds(self,amount):
# # #         self.current_funds = amount 
# # #     def update_company_is_dead(self,is_dead):
# # #         self.dead = is_dead
# # #     def is_dead(self):
# # #         return self.dead 
# # #     def check_company_status(self):
# # #         if self.dead:
# # #             self.update_company_is_dead(True)
# # #         else:
# # #             # display informationa bout selecting jobs 
# # #             if self.selected_jobs:
# # #                 for job in self.selected_jobs:
# # #                     if job['assigned_employee_count']:
# # #                         self.update_selected_job_progress(job['name'],job['assigned_employee_count'])
# # #                     if job['progress'] >= job['max_progress']:
# # #                         self.increase_available_employee_count(job['assigned_employee_count'])
# # #                         self.increase_current_funds(job['reward'])
# # #                         self.completed_jobs += 1
# # #                         self.remove_selected_job(job['name'])
# # #                     else:
# # #                         # will need to replace this magic number 
# # #                         self.update_selected_job_deadline(job['name'],1)
# # #                     if job['deadline'] <= 0:
# # #                         print(f"Job '{job['name']}' has missed the deadline")
# # #                         self.failed_jobs += 1
# # #                         self.remove_selected_job(job['name'])
# # #             else:
# # #                 print('No select jobs to report')

# # #     def print_status_report(self):
            
# # #             # Print current funds
# # #             print(f"Current Funds: ${self.current_funds}")

# # #             print(f"Current Max Employee Count: {self.max_employee_count}")

# # #             # Print current available employee count
# # #             print(f"Current Available Employee Count: {self.current_available_employee_count}")

# # #             # Print total number of jobs completed
# # #             print(f"Total Number of Jobs Completed: {self.completed_jobs}")
# # #             print(f"Total Number of Jobs Failed: {self.failed_jobs}")
# # #             if len(self.selected_jobs):
# # #                 self.print_selected_jobs()
# # #             else:
# # #                 print("No jobs currently selected")


# # import random

# # class Company:
# #     def __init__(self, starting_funds, starting_employee_count):
# #         self.current_funds = starting_funds
# #         self.max_employee_count = starting_employee_count
# #         self.current_available_employee_count = self.max_employee_count
# #         self.completed_jobs = 0
# #         self.failed_jobs = 0
# #         self.available_jobs = {}
# #         self.jobs_queue = []
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
# #         for i in range(1, 300):
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

# #     def queue_in_progress_job(self, job_name):
# #         if job_name in self.available_jobs:
# #             # Remove the job from available_jobs and add to jobs_queue
# #             # job_details = self.available_jobs.pop(job_name)
# #             # self.jobs_queue.append(job_)
# #             self.jobs_queue.append(self.available_jobs[job_name])
# #             print(f"Job '{job_name}' has been queued for processing.")
# #         else:
# #             print(f"Job '{job_name}' is not available.")
            
# #     def queue_job(self, job_name):
# #         if job_name in self.available_jobs:
# #             # Remove the job from available_jobs and add to jobs_queue
# #             job_details = self.available_jobs.pop(job_name)
# #             self.jobs_queue.append({"name": job_name, "details": job_details})
# #             print(f"Job '{job_name}' has been queued for processing.")
# #         else:
# #             print(f"Job '{job_name}' is not available.")
        
# #     def display_queued_jobs(self):
# #         print("Jobs in Queue:")
# #         if not self.jobs_queue:
# #             print("  No jobs in the queue.")
# #         for job in self.jobs_queue:
# #             print(f"    Job Name: {job['name']}")
# #             print(f"    Deadline: {job['deadline']}")
# #             print(f"    Progress: {job['progress']}")
# #             print(f"    Assigned Employee Count: {job['assigned_employee_count']}")
# #             print()
# #         else:
# #             print("No jobs in progress")

# #     def display_available_jobs(self):
# #         for job_name, job_details in self.available_jobs.items():
# #             print(f"Job Name: {job_name}")
# #             for key, value in job_details.items():
# #                 print(f"  {key}: {value}")
# #             print()  # Adds a blank line between jobs
    
# #     def print_available_job(self, job_name):
# #         if job_name in self.available_jobs:
# #             job_details = self.available_jobs[job_name]
# #             print(f"Job Name: {job_name}")
# #             for key, value in job_details.items():
# #                 print(f"  {key}: {value}")
# #         else:
# #             print(f"Job '{job_name}' not found in available jobs.")
    
# #     def assign_workers_to_job(self, job_name, worker_count):
# #         """Assign workers to a job and handle the associated costs."""
# #         if job_name not in self.available_jobs:
# #             print(f"Job '{job_name}' not found.")
# #             return
        
# #         job = self.available_jobs[job_name]
# #         total_cost = worker_count * job["cost_per_worker"]
        
# #         if total_cost > self.current_funds:
# #             print("Not enough funds to assign that many workers.")
# #         elif worker_count > self.current_available_employee_count:
# #             print("Not enough available workers.")
# #         else:
# #             job["assigned_employee_count"] += worker_count
# #             selfis there a way to progressively include loyee_count(self, amount):
# #         self.max_employee_count += amount 
        
# #     def increase_available_employee_count(self, amount):
# #         self.current_available_employee_count += amount 
        
# #     def decrease_max_employee_count(self, amount):
# #         self.max_employee_count -= amount 
        
# #     def decrease_available_employee_count(self, amount):
# #         self.current_available_employee_count -= amount 
    
# #     def get_max_employee_count(self):
# #         return self.max_employee_count
    
# #     def get_current_employee_count(self):
# #         return self.current_available_employee_count
    
# #     def increase_current_funds(self, amount):
# #         self.current_funds += amount

# #     def decrease_current_funds(self, amount):
# #         self.current_funds -= amount 
    
# #     def update_current_funds(self, amount):
# #         self.current_funds = amount 
    
# #     def update_company_is_dead(self, is_dead):
# #         self.dead = is_dead
    
# #     def is_dead(self):
# #         return self.dead 
    
# #     def check_company_status(self):
# #         if self.dead:
# #             print("The company is dead.")
# #         else:
# #             for job_name, job in list(self.available_jobs.items()):
# #                 if job["assigned_employee_count"]:
# #                     # Update the 'progress' key in the job dictionary
# #                     job["progress"] += job["assigned_employee_count"]
                    
# #                     # Ensure the progress does not exceed max progress
# #                     if job["progress"] > job["max_progress"]:
# #                         job["progress"] = job["max_progress"]
                    
# #                     # Check job status
# #                     if job["progress"] >= job["max_progress"]:
# #                         self.increase_available_employee_count(job["assigned_employee_count"])
# #                         self.increase_current_funds(job["reward"])
# #                         self.completed_jobs += 1
# #                         del self.available_jobs[job_name]
# #                         print(f"Job '{job_name}' completed.")
# #                     else:
# #                         # Update job deadline
# #                         job["deadline"] -= 1
# #                         if job["deadline"] <= 0:
# #                             print(f"Job '{job_name}' has missed the deadline.")
# #                             self.failed_jobs += 1
# #                             del self.available_jobs[job_name]

# #     def print_status_report(self):
# #         """Print the status report of the company."""
# #         print(f"Current Funds: ${self.current_funds}")
# #         print(f"Current Max Employee Count: {self.max_employee_count}")
# #         print(f"Current Available Employee Count: {self.current_available_employee_count}")
# #         print(f"Total Number of Jobs Completed: {self.completed_jobs}")
# #         print(f"Total Number of Jobs Failed: {self.failed_jobs}")
        
# #         if self.available_jobs:
# #             self.display_available_jobs()
# #         else:
# #             print("No jobs available.")

# #     def find_easy_jobs(self, count=3):
# #         """Find and return a specified number of easy jobs from available jobs."""
# #         easy_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Easy"]
        
# #         # Ensure there are enough easy jobs to sample
# #         if len(easy_jobs) < count:
# #             count = len(easy_jobs)
        
# #         # Select the easy jobs
# #         selected_easy_jobs = random.sample(easy_jobs, count) if easy_jobs else []
        
# #         # Display details for each selected easy job
# #         print(f"Displaying {count} easy jobs:")
# #         for job_name in selected_easy_jobs:
# #             self.print_available_job(job_name)
# #             print()  # Adds a blank line between jobs

# #     def find_medimum_jobs(self, count=3):
# #         """Find and return a specified number of easy jobs from available jobs."""
# #         medium_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Medium"]
        
# #         # Ensure there are enough easy jobs to sample
# #         if len(medium_jobs) < count:
# #             count = len(medium_jobs)
        
# #         # Select the easy jobs
# #         selected_medium_jobs = random.sample(medium_jobs, count) if medium_jobs else []
        
# #         # Display details for each selected easy job
# #         print(f"Displaying {count} medium jobs:")
# #         for job_name in selected_medium_jobs:
# #             self.print_available_job(job_name)
# #             print()  # Adds a blank line between jobs

# #     def find_hard_jobs(self, count=3):
# #         """Find and return a specified number of easy jobs from available jobs."""
# #         hard_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Hard"]
        
# #         # Ensure there are enough easy jobs to sample
# #         if len(hard_jobs) < count:
# #             count = len(hard_jobs)
        
# #         # Select the easy jobs
# #         selected_hard_jobs = random.sample(hard_jobs, count) if hard_jobs else []
        
# #         # Display details for each selected easy job
# #         print(f"Displaying {count} hard jobs:")
# #         for job_name in selected_hard_jobs:
# #             self.print_available_job(job_name)
# #             print()  # Adds a blank line between jobs


# # import random

# # class Company:
# #     def __init__(self, starting_funds, starting_employee_count):
# #         self.current_funds = starting_funds
# #         self.max_employee_count = starting_employee_count
# #         self.current_available_employee_count = self.max_employee_count
# #         self.completed_jobs = 0
# #         self.failed_jobs = 0
# #         self.available_jobs = {}
# #         self.jobs_queue = []
# #         self.dead = False
# #         self.current_quarter = 1 

# #     # Define a fixed cost per worker
# #     FIXED_COST_PER_WORKER = 50  # or any other reasonable number
# #     def get_quarter(self):
# #         return self.current_quarter
    
# #     def advance_quarter(self):
# #         """Advance to the next quarter and adjust job difficulty."""
# #         self.current_quarter += 1
# #         self.update_job_difficulty()

# #     def update_job_difficulty(self):
# #         """Update the difficulty of jobs based on the current quarter."""
# #         # This example increases the proportion of harder jobs as quarters progress.
# #         total_jobs = len(self.available_jobs)
# #         num_easy_jobs = max(1, int(total_jobs * max(0.1, 0.5 - 0.05 * (self.current_quarter - 1))))
# #         num_medium_jobs = max(1, int(total_jobs * max(0.3, 0.4 - 0.03 * (self.current_quarter - 1))))
# #         num_hard_jobs = max(1, total_jobs - num_easy_jobs - num_medium_jobs)
        
# #         self.populate_jobs(num_easy=num_easy_jobs, num_medium=num_medium_jobs, num_hard=num_hard_jobs)

# #     def populate_jobs(self, num_easy=100, num_medium=100, num_hard=100):
# #         """Populate jobs with a mix of difficulties."""
# #         self.available_jobs = {}
        
# #         for i in range(num_easy):
# #             job_name = f"EasyJob{chr(65 + i)}"
# #             self.available_jobs[job_name] = {
# #                 "name": job_name,
# #                 "cost_per_worker": 10,
# #                 "progress": 0,
# #                 "max_progress": 5,
# #                 "assigned_employee_count": 0,
# #                 "deadline": 10,
# #                 "reward": 100,
# #                 "difficulty": "Easy",
# #             }
        
# #         for i in range(num_medium):
# #             job_name = f"MediumJob{chr(65 + i)}"
# #             self.available_jobs[job_name] = {
# #                 "name": job_name,
# #                 "cost_per_worker": 20,
# #                 "progress": 0,
# #                 "max_progress": 10,
# #                 "assigned_employee_count": 0,
# #                 "deadline": 8,
# #                 "reward": 200,
# #                 "difficulty": "Medium",
# #             }
        
# #         for i in range(num_hard):
# #             job_name = f"HardJob{chr(65 + i)}"
# #             self.available_jobs[job_name] = {
# #                 "name": job_name,
# #                 "cost_per_worker": 30,
# #                 "progress": 0,
# #                 "max_progress": 15,
# #                 "assigned_employee_count": 0,
# #                 "deadline": 6,
# #                 "reward": 300,
# #                 "difficulty": "Hard",
# #             }

# #     def get_random_job(self, difficulty):
# #         """Get a random job based on difficulty."""
# #         jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == difficulty]
# #         if jobs:
# #             return random.choice(jobs)
# #         return None
    
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



# #     def queue_job(self, job_name):
# #         """Queue a job for processing."""
# #         if job_name in self.available_jobs:
# #             job_details = self.available_jobs.pop(job_name)
# #             self.jobs_queue.append(job_details)
# #             print(f"Job '{job_name}' has been queued for processing.")
# #         else:
# #             print(f"Job '{job_name}' is not available.")
        
# #     def display_queued_jobs(self):
# #         """Display the jobs currently in the queue."""
# #         if not self.jobs_queue:
# #             print("No jobs in the queue.")
# #         else:
# #             print("Jobs in Queue:")
# #             for job in self.jobs_queue:
# #                 print(f"  Job Name: {job['name']}")
# #                 print(f"  Deadline: {job['deadline']}")
# #                 print(f"  Progress: {job['progress']}")
# #                 print(f"  Assigned Employee Count: {job['assigned_employee_count']}")
# #                 print()
# #     def process_queued_jobs(self):
# #         """Process each queued job and handle completion, rewards, and removal from the queue."""
# #         if not self.jobs_queue:
# #             print("No jobs in the queue")
# #         else:
# #             for job in self.jobs_queue[:]:  # Iterate over a copy of the queue to modify it during iteration
# #                 if job["progress"] >= job["max_progress"]:
# #                     # Job is complete, process reward and update statistics
# #                     self.increase_current_funds(job["reward"])
# #                     self.completed_jobs += 1
# #                     self.jobs_queue.remove(job)  # Remove the job from the queue
# #                     print(f"Job '{job['name']}' completed and reward of ${job['reward']} added to funds.")
# #                 else:
# #                     # Job is not yet complete, skip to next job
# #                     continue
   
# #     def display_available_jobs(self):
# #         """Display all available jobs."""
# #         if not self.available_jobs:
# #             print("No available jobs.")
# #         else:
# #             for job_name, job_details in self.available_jobs.items():
# #                 print(f"Job Name: {job_name}")
# #                 for key, value in job_details.items():
# #                     print(f"  {key}: {value}")
# #                 print()  # Adds a blank line between jobs
    
# #     def print_available_job(self, job_name):
# #         """Print details of a specific available job."""
# #         if job_name in self.available_jobs:
# #             job_details = self.available_jobs[job_name]
# #             print(f"Job Name: {job_name}")
# #             for key, value in job_details.items():
# #                 print(f"  {key}: {value}")
# #         else:
# #             print(f"Job '{job_name}' not found in available jobs.")
    
# #     def assign_workers_to_job(self, job_name, worker_count):
# #         """Assign workers to a job and handle the associated costs."""
# #         if job_name not in self.available_jobs:
# #             print(f"Job '{job_name}' not found.")
# #             return
        
# #         job = self.available_jobs[job_name]
# #         total_cost = worker_count * job["cost_per_worker"]
        
# #         if total_cost > self.current_funds:
# #             print("Not enough funds to assign that many workers.")
# #         elif worker_count > self.current_available_employee_count:
# #             print("Not enough available workers.")
# #         else:
# #             job["assigned_employee_count"] += worker_count
# #             self.decrease_current_funds(total_cost)
# #             self.decrease_available_employee_count(worker_count)
# #             print(f"Assigned {worker_count} workers to job '{job_name}'.")


# #     def hire_workers(self, count):
# #         """Hire workers and handle the associated costs."""
# #         total_cost = count * self.FIXED_COST_PER_WORKER
# #         if total_cost > self.current_funds:
# #             print("Not enough funds to hire that many workers.")
# #         else:
# #             self.increase_max_employee_count(count)
# #             self.increase_available_employee_count(count)
# #             self.decrease_current_funds(total_cost)
# #             print(f"Hired {count} workers.")
# #     def get_worker_cost(self):
# #         return self.FIXED_COST_PER_WORKER
    
# #     def get_cost_per_worker(self, job_name):
# #             """Get the cost per worker for a specific job."""
# #             if job_name in self.available_jobs:
# #                 return self.available_jobs[job_name]["cost_per_worker"]
# #             else:
# #                 print(f"Job '{job_name}' not found.")
# #                 return None

# #     def increase_max_employee_count(self, amount):
# #         self.max_employee_count += amount 
        
# #     def increase_available_employee_count(self, amount):
# #         self.current_available_employee_count += amount 
        
# #     def decrease_max_employee_count(self, amount):
# #         self.max_employee_count -= amount 
        
# #     def decrease_available_employee_count(self, amount):
# #         self.current_available_employee_count -= amount 
    
# #     def get_max_employee_count(self):
# #         return self.max_employee_count
    
# #     def get_current_employee_count(self):
# #         return self.current_available_employee_count
    
# #     def increase_current_funds(self, amount):
# #         self.current_funds += amount

# #     def decrease_current_funds(self, amount):
# #         self.current_funds -= amount 
    
# #     def update_current_funds(self, amount):
# #         self.current_funds = amount 
    
# #     def update_company_is_dead(self, is_dead):
# #         self.dead = is_dead
    
# #     def is_dead(self):
# #         return self.dead 
    
# #     def check_company_status(self):
# #         if self.dead:
# #             print("The company is dead.")
# #         else:
# #             for job in self.jobs_queue[:]:
# #                 if job["assigned_employee_count"]:
# #                     job["progress"] += job["assigned_employee_count"]
                    
# #                     if job["progress"] > job["max_progress"]:
# #                         job["progress"] = job["max_progress"]
                    
# #                     if job["progress"] >= job["max_progress"]:
# #                         self.increase_available_employee_count(job["assigned_employee_count"])
# #                         self.increase_current_funds(job["reward"])
# #                         self.completed_jobs += 1
# #                         self.jobs_queue.remove(job)
# #                         print(f"Job '{job['name']}' completed.")
# #                     else:
# #                         job["deadline"] -= 1
# #                         if job["deadline"] <= 0:
# #                             print(f"Job '{job['name']}' has missed the deadline.")
# #                             self.failed_jobs += 1
# #                             self.jobs_queue.remove(job)

# #     def print_status_report(self):
# #         """Print the status report of the company."""
# #         print(f"Current Funds: ${self.current_funds}")
# #         print(f"Current Max Employee Count: {self.max_employee_count}")
# #         print(f"Current Available Employee Count: {self.current_available_employee_count}")
# #         print(f"Total Number of Jobs Completed: {self.completed_jobs}")
# #         print(f"Total Number of Jobs Failed: {self.failed_jobs}")
# #         self.display_queued_jobs()

# #     def find_easy_jobs(self, count=3):
# #             """Find and return a specified number of easy jobs from available jobs."""
# #             easy_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Easy"]
            
# #             # Ensure there are enough easy jobs to sample
# #             if len(easy_jobs) < count:
# #                 count = len(easy_jobs)
            
# #             # Select the easy jobs
# #             selected_easy_jobs = random.sample(easy_jobs, count) if easy_jobs else []
# #             return selected_easy_jobs

# #     def find_medium_jobs(self, count=3):
# #         """Find and return a specified number of medium jobs from available jobs."""
# #         medium_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Medium"]
        
# #         # Ensure there are enough medium jobs to sample
# #         if len(medium_jobs) < count:
# #             count = len(medium_jobs)
        
# #         # Select the medium jobs
# #         selected_medium_jobs = random.sample(medium_jobs, count) if medium_jobs else []
# #         return selected_medium_jobs

# #     def find_hard_jobs(self, count=3):
# #         """Find and return a specified number of hard jobs from available jobs."""
# #         hard_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Hard"]
        
# #         # Ensure there are enough hard jobs to sample
# #         if len(hard_jobs) < count:
# #             count = len(hard_jobs)
        
# #         # Select the hard jobs
# #         selected_hard_jobs = random.sample(hard_jobs, count) if hard_jobs else []
# #         return selected_hard_jobs


# import random
# from tabulate import tabulate

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
#         self.current_quarter = 1 

#     # Define a fixed cost per worker
#     FIXED_COST_PER_WORKER = 50 

#     def get_quarter(self):
#         return self.current_quarter
    
#     def advance_quarter(self):
#         """Advance to the next quarter and adjust job difficulty."""
#         self.current_quarter += 1
#         self.update_job_difficulty()

#     def update_job_difficulty(self):
#         """Update the difficulty of jobs based on the current quarter."""
#         if self.current_quarter <= 2:
#             self.populate_jobs(num_easy=10, num_medium=0, num_hard=0)
#         elif self.current_quarter <= 4:
#             self.populate_jobs(num_easy=7, num_medium=3, num_hard=0)
#         else:
#             self.populate_jobs(num_easy=5, num_medium=3, num_hard=2)

#     def populate_jobs(self, num_easy=10, num_medium=10, num_hard=10):
#         """Populate jobs with a mix of difficulties."""
#         self.available_jobs = {}
        
#         for i in range(num_easy):
#             job_name = f"EasyJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 10,
#                 "progress": 0,
#                 "max_progress": 5,
#                 "assigned_employee_count": 0,
#                 "deadline": 10,
#                 "reward": 100,
#                 "difficulty": "Easy",
#             }
        
#         for i in range(num_medium):
#             job_name = f"MediumJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 20,
#                 "progress": 0,
#                 "max_progress": 10,
#                 "assigned_employee_count": 0,
#                 "deadline": 8,
#                 "reward": 200,
#                 "difficulty": "Medium",
#             }
        
#         for i in range(num_hard):
#             job_name = f"HardJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 30,
#                 "progress": 0,
#                 "max_progress": 15,
#                 "assigned_employee_count": 0,
#                 "deadline": 6,
#                 "reward": 300,
#                 "difficulty": "Hard",
#             }

#     def get_random_job(self, difficulty):
#         """Get a random job based on difficulty."""
#         jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == difficulty]
#         if jobs:
#             return random.choice(jobs)
#         return None
    
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

#     def queue_job(self, job_name):
#         """Queue a job for processing."""
#         if job_name in self.available_jobs:
#             job_details = self.available_jobs.pop(job_name)
#             self.jobs_queue.append(job_details)
#             print(f"Job '{job_name}' has been queued for processing.")
#         else:
#             print(f"Job '{job_name}' is not available.")
        
#     def display_queued_jobs(self):
#         """Display the jobs currently in the queue in a tabular format."""
#         if not self.jobs_queue:
#             print("No jobs in the queue.")
#             return

#         # Prepare data for tabulation
#         table_data = []
#         headers = ["Job Name", "Deadline", "Progress", "Assigned Employees"]

#         for job in self.jobs_queue:
#             row = [
#                 job['name'],
#                 job['deadline'],
#                 job['progress'],
#                 job['assigned_employee_count']
#             ]
#             table_data.append(row)

#         # Print the table
#         print("\nJobs in Queue:")
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
#     def process_queued_jobs(self):
#         """Process each queued job and handle completion, rewards, and removal from the queue."""
#         if not self.jobs_queue:
#             print("No jobs in the queue")
#         else:
#             for job in self.jobs_queue[:]:  # Iterate over a copy of the queue to modify it during iteration
#                 if job["progress"] >= job["max_progress"]:
#                     # Job is complete, process reward and update statistics
#                     self.increase_current_funds(job["reward"])
#                     self.completed_jobs += 1
#                     self.jobs_queue.remove(job)  # Remove the job from the queue
#                     print(f"Job '{job['name']}' completed and reward of ${job['reward']} added to funds.")
#                 else:
#                     # Job is not yet complete, skip to next job
#                     continue
   
#     def display_available_jobs(self):
#         """Display all available jobs in a tabular format."""
#         print()
#         if not self.available_jobs:
#             print("No available jobs.")
#             return

#         # Prepare data for tabulation
#         table_data = []
#         headers = ["Job Name", "Difficulty", "Cost per Worker", "Progress", "Max Progress", "Assigned Employees", "Deadline", "Reward"]

#         for job_name, job_details in self.available_jobs.items():
#             row = [
#                 job_name,
#                 job_details["difficulty"],
#                 job_details["cost_per_worker"],
#                 job_details["progress"],
#                 job_details["max_progress"],
#                 job_details["assigned_employee_count"],
#                 job_details["deadline"],
#                 job_details["reward"]
#             ]
#             table_data.append(row)

#         # Print the table
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
#     def print_available_job(self, job_name):
#         """Print details of a specific available job."""
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

#     def hire_workers(self, count):
#         """Hire workers and handle the associated costs."""
#         total_cost = count * self.FIXED_COST_PER_WORKER
#         if total_cost > self.current_funds:
#             print("Not enough funds to hire that many workers.")
#         else:
#             self.increase_max_employee_count(count)
#             self.increase_available_employee_count(count)
#             self.decrease_current_funds(total_cost)
#             print(f"Hired {count} workers.")
            
#     def get_worker_cost(self):
#         return self.FIXED_COST_PER_WORKER
    
#     def get_cost_per_worker(self, job_name):
#         """Get the cost per worker for a specific job."""
#         if job_name in self.available_jobs:
#             return self.available_jobs[job_name]["cost_per_worker"]
#         else:
#             print(f"Job '{job_name}' not found.")
#             return None

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
#             print("Company is dead.")
#         else:
#             print(f"Current Funds: ${self.current_funds}")
#             print(f"Available Employees: {self.current_available_employee_count}/{self.max_employee_population}")
#             print(f"Completed Jobs: {self.completed_jobs}")
#             print(f"Failed Jobs: {self.failed_jobs}")
#             self.display_available_jobs()
#             self.display_queued_jobs()
    
# #     def get_available_jobs(self):
# #         return self.available_jobs



# import random
# from tabulate import tabulate

# """

# player will get supply capped and fked over if they dont prioritze their funds 

# """
# class Company:
#     def __init__(self, starting_funds, starting_employee_count):
#         self.current_funds = starting_funds
#         self.max_employee_population = 5
#         self.current_available_employee_count = starting_employee_count
#         self.completed_jobs = 0
#         self.failed_jobs = 0
#         self.available_jobs = {}
#         self.jobs_queue = []
#         self.dead = False
#         self.expansion_level = 1  # Tracks the company's expansion level

#     FIXED_COST_PER_WORKER = 50  # Fixed cost per worker

# # should bring in new features when expansion happens 
#     def expand_company(self):
#         self.expansion_level += 1
#         self.update_job_difficulty()

#     def get_funds(self):
#         return self.current_funds
#     def get_max_employee_population(self):
#         return self.max_employee_count
#     def get_available_employee_count(self):
#         return self.employee_count
    
#     def update_job_difficulty(self):
#         """Update the difficulty of jobs based on the current quarter."""
#         total_jobs = len(self.available_jobs)
#         num_easy_jobs = max(1, int(total_jobs * max(0.1, 0.5 - 0.05 * (self.current_quarter - 1))))
#         num_medium_jobs = max(1, int(total_jobs * max(0.3, 0.4 - 0.03 * (self.current_quarter - 1))))
#         num_hard_jobs = max(1, total_jobs - num_easy_jobs - num_medium_jobs)
        
#         self.populate_jobs(num_easy=num_easy_jobs, num_medium=num_medium_jobs, num_hard=num_hard_jobs)

#     def populate_jobs(self, num_easy=3, num_medium=3, num_hard=3):
#         """Populate jobs with a mix of difficulties."""
#         self.available_jobs = {}
        
#         for i in range(num_easy):
#             job_name = f"EasyJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 10,
#                 "progress": 0,
#                 "max_progress": 5,
#                 "assigned_employee_count": 0,
#                 "deadline": 10,
#                 "reward": 100,
#                 "difficulty": "Easy",
#             }
        
#         for i in range(num_medium):
#             job_name = f"MediumJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 20,
#                 "progress": 0,
#                 "max_progress": 10,
#                 "assigned_employee_count": 0,
#                 "deadline": 8,
#                 "reward": 200,
#                 "difficulty": "Medium",
#             }
        
#         for i in range(num_hard):
#             job_name = f"HardJob{chr(65 + i)}"
#             self.available_jobs[job_name] = {
#                 "name": job_name,
#                 "cost_per_worker": 30,
#                 "progress": 0,
#                 "max_progress": 15,
#                 "assigned_employee_count": 0,
#                 "deadline": 6,
#                 "reward": 300,
#                 "difficulty": "Hard",
#             }

#     def get_random_job(self, difficulty):
#         """Get a random job based on difficulty."""
#         jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == difficulty]
#         if jobs:
#             return random.choice(jobs)
#         return None
    
#     def display_queued_jobs(self):
#         """Display the jobs currently in the queue in a tabular format."""
#         if not self.jobs_queue:
#             print("No jobs in the queue.")
#             return

#         # Prepare data for tabulation
#         table_data = []
#         headers = ["Job Name", "Deadline", "Progress", "Assigned Employees"]

#         for job in self.jobs_queue:
#             row = [
#                 job['name'],
#                 job['deadline'],
#                 job['progress'],
#                 job['assigned_employee_count']
#             ]
#             table_data.append(row)

#         # Print the table
#         print("Jobs in Queue:")
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))

#     def queue_job(self, job_name):
#         """Queue a job for processing."""
#         if job_name in self.available_jobs:
#             job_details = self.available_jobs.pop(job_name)
#             self.jobs_queue.append(job_details)
#             print(f"Job '{job_name}' has been queued for processing.")
#         else:
#             print(f"Job '{job_name}' is not available.")
        
#     def display_available_jobs(self):
#         """Display all available jobs."""
#         if not self.available_jobs:
#             print("No available jobs.")
#         else:
#             headers = ["Job Name", "Difficulty", "Cost/Worker", "Progress", "Max Progress", "Reward", "Deadline"]
#             table_data = []
            
#             for job_name, job_details in self.available_jobs.items():
#                 row = [
#                     job_name,
#                     job_details["difficulty"],
#                     job_details["cost_per_worker"],
#                     job_details["progress"],
#                     job_details["max_progress"],
#                     job_details["reward"],
#                     job_details["deadline"]
#                 ]
#                 table_data.append(row)
                
#             print("Available Jobs:")
#             print(tabulate(table_data, headers=headers, tablefmt="grid"))

#     def display_available_jobs(self):
#         """Display all available jobs with numbers for user selection and return an array of job names."""
#         job_names = []
        
#         if not self.available_jobs:
#             print("No available jobs.")
#             return job_names
        
#         headers = ["#", "Job Name", "Difficulty", "Cost/Worker", "Progress", "Max Progress", "Reward", "Deadline"]
#         table_data = []
        
#         for index, (job_name, job_details) in enumerate(self.available_jobs.items(), start=1):
#             row = [
#                 index,  # Display job number
#                 job_name,
#                 job_details["difficulty"],
#                 job_details["cost_per_worker"],
#                 job_details["progress"],
#                 job_details["max_progress"],
#                 job_details["reward"],
#                 job_details["deadline"]
#             ]
#             table_data.append(row)
#             job_names.append(job_name)  # Collect job names
        
#         print("Available Jobs:")
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))

#         return job_names



#     def assign_workers_to_job(self, job_name, worker_count):
#         """Assign workers to a job and handle the associated costs."""
#         if job_name not in self.available_jobs:
#             print(f"Job '{job_name}' not found.")
#             return
#         job = self.available_jobs[job_name]
        
#         if worker_count >= self.employee_count:
#             worker_count = self.employee_count
#         job["assigned_employee_count"] += worker_count
#         total_cost = worker_count * job["cost_per_worker"]
#         self.decrease_current_funds(total_cost)
#         self.decrease_available_employee_count(worker_count)

#     def hire_workers(self, count):
#         """Hire workers and handle the associated costs."""
#         total_cost = count * self.FIXED_COST_PER_WORKER       
#         self.decrease_current_funds(total_cost)
#         self.increase_max_employee_count(count)
#         self.increase_available_employee_count(count)
#         self.decrease_current_funds(total_cost)
#         if count > 1:
#             print(f"Hired {count} workers.")
#         else:
#             print(f"Hired {count} worker.")

#          # if total_cost > self.current_funds:
#         #     print("Not enough funds to hire that many workers.")
#         # else:
#         #     self.increase_max_employee_count(count)
#         #     self.increase_available_employee_count(count)
#         #     self.decrease_current_funds(total_cost)
#         #     print(f"Hired {count} workers.")
        
#         # if total_cost > self.current_funds:
#         #     print("Not enough funds to hire that many workers.")
#         # else:
#         #     self.increase_max_employee_count(count)
#         #     self.increase_available_employee_count(count)
#         #     self.decrease_current_funds(total_cost)
#         #     print(f"Hired {count} workers.")

#     def get_worker_cost(self):
#         return self.FIXED_COST_PER_WORKER
    
#     def increase_max_employee_count(self, amount):
#         self.max_employee_count += amount 
        
#     def increase_available_employee_count(self, amount):
#         self.employee_count += amount 
        
#     def decrease_max_employee_count(self, amount):
#         self.max_employee_count -= amount 
        
#     def decrease_available_employee_count(self, amount):
#         self.employee_count -= amount 
    
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
#         if self.current_funds <= 0:
#             self.dead = True 
#             print("The company is dead.")
#         else:
#             for job in self.jobs_queue[:]:
#                 if job["assigned_employee_count"]:
#                     job["progress"] += job["assigned_employee_count"]
                    
#                     if job["progress"] > job["max_progress"]:
#                         job["progress"] = job["max_progress"]
                    
#                     if job["progress"] >= job["max_progress"]:
#                         self.increase_available_employee_count(job["assigned_employee_count"])
#                         self.increase_current_funds(job["reward"])
#                         self.completed_jobs += 1
#                         self.jobs_queue.remove(job)
#                         print(f"Job '{job['name']}' completed.")
#                     else:
#                         job["deadline"] -= 1
#                         if job["deadline"] <= 0:
#                             print(f"Job '{job['name']}' has missed the deadline.")
#                             self.failed_jobs += 1
#                             self.jobs_queue.remove(job)

#     def print_status_report(self):
#         """Print the status report of the company."""
#         if self.current_funds < 0:
#             print(f"Current Funds: -${self.current_funds}")
#         else:
#             print(f"Current Funds: ${self.current_funds}")
            
#         print(f"Current Max Employee Count: {self.max_employee_count}")
#         print(f"Current Available Employee Count: {self.employee_count}")
#         print(f"Total Number of Jobs Completed: {self.completed_jobs}")
#         print(f"Total Number of Jobs Failed: {self.failed_jobs}")
#         self.display_queued_jobs()

#     def find_easy_jobs(self, count=3):
#         """Find and return a specified number of easy jobs from available jobs."""
#         easy_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Easy"]
#         if len(easy_jobs) < count:
#             count = len(easy_jobs)
#         selected_easy_jobs = random.sample(easy_jobs, count) if easy_jobs else []
#         return selected_easy_jobs

#     def find_medium_jobs(self, count=3):
#         """Find and return a specified number of medium jobs from available jobs."""
#         medium_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Medium"]
#         if len(medium_jobs) < count:
#             count = len(medium_jobs)
#         selected_medium_jobs = random.sample(medium_jobs, count) if medium_jobs else []
#         return selected_medium_jobs

#     def find_hard_jobs(self, count=3):
#         """Find and return a specified number of hard jobs from available jobs."""
#         hard_jobs = [job_name for job_name, details in self.available_jobs.items() if details["difficulty"] == "Hard"]
#         if len(hard_jobs) < count:
#             count = len(hard_jobs)
#         selected_hard_jobs = random.sample(hard_jobs, count) if hard_jobs else []
#         return selected_hard_jobs


import random
from tabulate import tabulate

class Company:
    def __init__(self, starting_funds, starting_employee_count,max_population):
        self.current_funds = starting_funds
        # self.max_employee_population = max_population
        self.current_available_employee_count = starting_employee_count
        self.completed_jobs = 0
        self.failed_jobs = 0
        self.available_jobs = {}
        self.jobs_queue = []
        self.dead = False
        self.expansion_level = 1  # Tracks the company's expansion level
        self.expansion_cost = 500  # Base cost for expanding the company
 # Space-related job names
        self.easy_jobs = [
        "Space Janitor",
        "Launch Pad Technician",
        "Satellite Maintenance Assistant",
        "Spacecraft Cleaning Specialist",
        "Mission Control Support",
        "Astronaut Aide",
        "Space Supply Coordinator",
        "Space Station Cook",
        "Space Shuttle Ground Crew",
        "Telescope Operator",
        "Flight Log Assistant",
        "Orbital Logistics Clerk",
        "Space Research Intern",
        "Habitat Maintenance Worker",
        "Space Inventory Clerk",
        "Space Shuttle Refueling Technician",
        "Spacecraft Systems Tester",
        "Space Mission Scheduler",
        "Spacecraft Docking Assistant",
        "Space Communications Liaison",
        "Astronaut Equipment Assistant",
        "Space Station Maintenance Worker",
        "Spacecraft Storage Specialist",
        "Satellite Calibration Technician",
        "Mission Planning Assistant",
        "Spacecraft Assembly Helper",
        "Rocket Launch Coordinator",
        "Orbital Station Clerk",
        "Spacecraft Inspection Assistant",
        "Telescope Maintenance Worker",
        "Spacecraft Refurbishment Specialist",
        "Space Operations Assistant",
        "Space Research Coordinator",
        "Astronaut Supplies Manager",
        "Spacecraft Inventory Supervisor",
        "Launch Vehicle Technician",
        "Space Station Hygiene Officer",
        "Orbital Cargo Handler",
        "Space Shuttle Preflight Inspector",
        "Satellite Monitoring Technician",
        "Space Expedition Support",
        "Astronaut Training Assistant",
        "Space Shuttle Cleanup Crew",
        "Spacecraft Component Tester",
        "Space Mission Inventory Clerk",
        "Orbital Research Assistant",
        "Spacecraft Ground Support",
        "Space Station Log Keeper",
        "Spacecraft Operations Assistant",
        "Satellite Repair Specialist",
        "Space Shuttle Ground Technician",
        "Space Exploration Assistant",
        "Orbital Habitation Technician",
        "Spacecraft Safety Inspector",
        "Mission Control Assistant",
        "Space Station Equipment Operator",
        "Spacecraft Calibration Specialist",
        "Launch Pad Maintenance Worker",
        "Space Shuttle Maintenance Crew",
        "Astronaut Health Aide",
        "Space Station Resource Manager",
        "Orbital Systems Tester",
        "Spacecraft Operation Support",
        "Satellite Launch Assistant",
        "Space Mission Prep Assistant",
        "Spacecraft Communication Technician",
        "Space Research Aide",
        "Orbital Station Technician",
        "Space Shuttle Refurbishment Crew",
        "Astronaut Gear Technician",
        "Spacecraft Refueling Assistant",
        "Space Exploration Assistant",
        "Mission Log Keeper",
        "Space Station Ground Crew",
        "Space Shuttle Operations Assistant",
        "Spacecraft System Maintainer",
        "Space Mission Inventory Manager",
        "Orbital Maintenance Specialist",
        "Satellite Calibration Assistant",
        "Space Shuttle Mission Support",
        "Spacecraft Logistics Coordinator",
        "Astronaut Equipment Specialist",
        "Space Station Hygiene Technician",
        "Space Shuttle Refueling Crew",
        "Spacecraft Assembly Coordinator",
        "Space Mission Equipment Technician",
        "Orbital Launch Assistant",
        "Space Research Technician",
        "Space Station Operations Specialist",
        "Satellite Deployment Assistant",
        "Spacecraft Inspection Supervisor",
        "Space Shuttle Inspection Crew",
        "Orbital Station Ground Support",
        "Space Exploration Log Keeper",
        "Spacecraft Equipment Coordinator",
        "Mission Control Support Staff",
        "Space Shuttle System Technician",
        "Space Station Equipment Specialist",
        "Astronaut Training Coordinator",
        "Spacecraft Maintenance Helper",
        "Space Mission Refueling Technician",
        "Orbital Resource Manager",
        "Space Shuttle Mission Technician",
        "Space Station Log Specialist",
        "Satellite Operation Assistant",
        "Spacecraft Operations Coordinator",
        "Space Exploration Technician",
        "Orbital Maintenance Coordinator",
        "Space Shuttle Ground Support",
        "Space Mission Logistics Assistant",
        "Spacecraft Repair Technician",
        "Astronaut Systems Aide",
        "Space Station Cleaning Crew",
        "Spacecraft Docking Specialist",
        "Mission Control Systems Assistant",
        "Space Shuttle Maintenance Technician",
        "Space Exploration Maintenance",
        "Orbital Operations Specialist",
        "Spacecraft Preflight Coordinator",
        "Space Shuttle Refueling Supervisor",
        "Space Mission Calibration Technician",
        "Astronaut Equipment Coordinator",
        "Space Station Logistics Supervisor",
        "Spacecraft Systems Support",
        "Orbital Launch Technician",
        "Space Shuttle Operations Coordinator",
        "Space Research Logistics Manager"
    ]


        self.medium_jobs = [
            "Spacecraft Systems Engineer",
            "Orbital Mechanics Specialist",
            "Mission Planning Coordinator",
            "Space Research Scientist",
            "Satellite Systems Engineer",
            "Space Mission Analyst",
            "Space Habitat Engineer",
            "Spacecraft Pilot",
            "Space Robotics Technician",
            "Space Station Systems Engineer",
            "Space Exploration Planner",
            "Satellite Launch Coordinator",
            "Astrobiologist",
            "Space Communication Engineer",
            "Spacecraft Flight Controller",
            "Space Logistics Manager",
            "Space Mission Specialist",
            "Extravehicular Activity Coordinator",
            "Orbital Debris Analyst",
            "Space Operations Supervisor",
            "Interplanetary Navigation Expert",
            "Spacecraft Thermal Systems Engineer",
            "Orbital Dynamics Specialist",
            "Satellite Operations Engineer",
            "Spacecraft Avionics Engineer",
            "Space Research Coordinator",
            "Mission Operations Manager",
            "Spacecraft Propulsion Engineer",
            "Satellite Communications Specialist",
            "Space Systems Analyst",
            "Space Habitat Systems Engineer",
            "Orbital Flight Controller",
            "Space Engineering Technician",
            "Space Systems Designer",
            "Satellite Integration Specialist",
            "Space Mission Coordinator",
            "Space Exploration Engineer",
            "Orbital Mechanics Engineer",
            "Space Research Analyst",
            "Space Operations Engineer",
            "Spacecraft Navigation Specialist",
            "Space Mission Planner",
            "Space Station Maintenance Engineer",
            "Satellite Deployment Engineer",
            "Space Habitat Designer",
            "Spacecraft Systems Analyst",
            "Orbital Logistics Specialist",
            "Space Exploration Specialist",
            "Satellite Monitoring Engineer",
            "Spacecraft Engineering Specialist",
            "Space Systems Manager",
            "Space Mission Operations Manager",
            "Orbital Debris Specialist",
            "Space Research Engineer",
            "Spacecraft Integration Engineer",
            "Space Station Systems Analyst",
            "Satellite Operations Manager",
            "Space Exploration Manager",
            "Space Mission Operations Specialist",
            "Orbital Systems Specialist",
            "Space Habitat Systems Specialist",
            "Space Research Manager",
            "Spacecraft Support Engineer",
            "Space Mission Systems Engineer",
            "Satellite Engineering Manager",
            "Spacecraft Design Specialist",
            "Orbital Navigation Engineer",
            "Space Exploration Analyst",
            "Spacecraft Maintenance Engineer",
            "Space Systems Coordinator",
            "Space Mission Support Engineer",
            "Satellite Systems Specialist",
            "Space Station Engineering Manager",
            "Spacecraft Propulsion Specialist",
            "Space Exploration Coordinator",
            "Orbital Systems Manager",
            "Spacecraft Systems Manager",
            "Satellite Research Engineer",
            "Space Mission Support Specialist",
            "Space Habitat Researcher",
            "Spacecraft Design Engineer",
            "Space Systems Researcher",
            "Orbital Operations Manager",
            "Space Research Specialist",
            "Spacecraft Integration Manager",
            "Satellite Systems Manager",
            "Space Mission Engineering Specialist",
            "Space Exploration Director",
            "Orbital Mechanics Analyst",
            "Space Habitat Operations Specialist",
            "Spacecraft Maintenance Specialist",
            "Space Research Operations Manager",
            "Space Mission Systems Analyst",
            "Spacecraft Operations Engineer",
            "Orbital Logistics Manager",
            "Space Exploration Researcher"
        ]

        self.hard_jobs = [
        "Chief Space Scientist",
        "Space Mission Commander",
        "Deep Space Navigator",
        "Astrophysicist",
        "Spacecraft Design Engineer",
        "Space Program Director",
        "Extraterrestrial Geologist",
        "Space Technology Innovator",
        "Space Habitat Architect",
        "Space Exploration Chief",
        "Spaceflight Safety Engineer",
        "Orbital Dynamics Expert",
        "Interstellar Research Leader",
        "Spacecraft Propulsion Specialist",
        "Space Mission Strategist",
        "Space Station Operations Director",
        "Space Robotics Lead Engineer",
        "Advanced Propulsion Systems Engineer",
        "Interplanetary Logistics Coordinator",
        "Deep Space Communication Specialist",
        "Chief Astronaut Trainer",
        "Space Policy Advisor",
        "Intergalactic Research Scientist",
        "Space Mission Director",
        "Advanced Space Systems Engineer",
        "Deep Space Exploration Specialist",
        "Chief Space Engineer",
        "Space Innovation Strategist",
        "Space Exploration Project Manager",
        "Space Mission Systems Director",
        "Astrobiology Research Director",
        "Spacecraft Systems Director",
        "Orbital Infrastructure Specialist",
        "Interstellar Navigation Engineer",
        "Space Science Director",
        "Chief Orbital Scientist",
        "Space Technology Development Manager",
        "Space Habitat Engineering Director",
        "Space Exploration Technology Specialist",
        "Space Mission Coordination Director",
        "Advanced Spacecraft Systems Analyst",
        "Intergalactic Operations Manager",
        "Space Research and Development Chief",
        "Chief Space Operations Officer",
        "Space Exploration Engineering Leader",
        "Deep Space Research Manager",
        "Space Systems Innovation Leader",
        "Chief Spacecraft Engineer",
        "Interstellar Engineering Specialist",
        "Space Habitat Research Leader",
        "Space Mission Research Director",
        "Advanced Orbital Mechanics Specialist",
        "Space Exploration Operations Chief",
        "Chief Astronaut Mission Commander",
        "Space Engineering Research Director",
        "Spacecraft Systems Innovation Specialist",
        "Interplanetary Mission Leader",
        "Deep Space Systems Engineer",
        "Space Exploration Research Lead",
        "Space Technology Advancement Director",
        "Orbital Dynamics Research Specialist",
        "Chief Space Program Engineer",
        "Space Mission Development Director",
        "Advanced Space Systems Manager",
        "Interstellar Spacecraft Engineer",
        "Space Exploration Logistics Chief",
        "Chief Space Operations Engineer",
        "Space Habitat Design Director",
        "Deep Space Mission Commander",
        "Spacecraft Engineering Research Lead",
        "Space Mission Technology Specialist",
        "Intergalactic Systems Engineer",
        "Advanced Space Exploration Manager",
        "Space Technology Integration Specialist",
        "Space Systems Research Director",
        "Chief Orbital Research Engineer",
        "Space Exploration Project Director",
        "Space Mission Operations Lead",
        "Advanced Space Mission Strategist",
        "Interstellar Space Research Director",
        "Chief Spacecraft Systems Engineer",
        "Spacecraft Innovation Director",
        "Deep Space Engineering Specialist",
        "Space Systems Operations Director",
        "Space Exploration Chief Engineer",
        "Intergalactic Mission Specialist",
        "Space Mission Systems Chief",
        "Chief Space Technology Specialist",
        "Advanced Orbital Engineering Director",
        "Space Exploration Research Manager",
        "Spacecraft Operations Director",
        "Deep Space Research Specialist"
        ]

    FIXED_COST_PER_WORKER = 10  # Fixed cost per worker
    
    def expand_company(self):
        """Expand the company, increasing employee capacity and job difficulty."""
        if self.current_funds < self.expansion_cost:
            print("Not enough funds to expand the company.")
            return
        
        # Deduct the expansion cost
        self.decrease_current_funds(self.expansion_cost)
        
        # Increase expansion level and employee capacity
        self.expansion_level += 1
        # self.max_employee_population += 5  # Increase capacity by 5 for each expansion
        
        # Increase the expansion cost for future expansions
        self.expansion_cost = int(self.expansion_cost * 1.5)
        
        # Update job difficulty
        self.update_job_difficulty()
        
        print(f"Company expanded to level {self.expansion_level}.") 
            #   Max employees increased to {self.max_employee_population}.")

    def hire_workers(self, count):
        """Hire workers and handle the associated costs."""
        # if count + self.current_available_employee_count > self.max_employee_population:
        #     print("No space for more employees.")
        #     return

        total_cost = count * self.FIXED_COST_PER_WORKER       
        if total_cost > self.current_funds:
            print("Not enough funds to hire that many workers.")
            return
        
        # Deduct cost and update employee counts
        self.decrease_current_funds(total_cost)
        self.current_available_employee_count += count
        
        print(f"Hired {count} worker(s).")
        
    def assign_workers_to_job(self, job_name, worker_count):
            """Assign workers to a job and handle the associated costs, adding the job to the queue."""
            if job_name not in self.available_jobs:
                print(f"Job '{job_name}' not found.")
                return
            
            if worker_count > self.current_available_employee_count:
                print("Not enough available employees.")
                return

            job = self.available_jobs[job_name]
            total_cost = worker_count * job["cost_per_worker"]
            
            if total_cost > self.current_funds:
                print("Not enough funds to assign that many workers.")
                return

            # If all checks pass, assign the workers and update funds
            job["assigned_employee_count"] += worker_count
            self.decrease_current_funds(total_cost)
            self.current_available_employee_count -= worker_count

            # Queue the job for processing
            self.queue_job(job_name)

            print(f"Assigned {worker_count} worker(s) to job '{job_name}' and added it to the job queue.")

    def update_job_difficulty(self):
        """Update the difficulty of jobs based on the current expansion level."""
        total_jobs = len(self.available_jobs)
        num_easy_jobs = max(1, int(total_jobs * max(0.1, 0.5 - 0.05 * (self.expansion_level - 1))))
        num_medium_jobs = max(1, int(total_jobs * max(0.3, 0.4 - 0.03 * (self.expansion_level - 1))))
        num_hard_jobs = max(1, total_jobs - num_easy_jobs - num_medium_jobs)
        
        self.populate_jobs(num_easy=num_easy_jobs, num_medium=num_medium_jobs, num_hard=num_hard_jobs)

    def populate_jobs(self, num_easy=3, num_medium=3, num_hard=3):
        """Populate jobs with a mix of difficulties and rename based on difficulty."""
        self.available_jobs = {}
        
        # Easy jobs
        easy_job_names = random.sample(self.easy_jobs, min(num_easy, len(self.easy_jobs)))
        for i, job_name in enumerate(easy_job_names):
            self.available_jobs[job_name] = {
                "name": job_name,
                "cost_per_worker": 10,
                "progress": 0,
                "max_progress": 5,
                "assigned_employee_count": 0,
                "deadline": 10,
                "reward": 100,
                "difficulty": "Easy",
            }
        
        # Medium jobs
        medium_job_names = random.sample(self.medium_jobs, min(num_medium, len(self.medium_jobs)))
        for i, job_name in enumerate(medium_job_names):
            self.available_jobs[job_name] = {
                "name": job_name,
                "cost_per_worker": 20,
                "progress": 0,
                "max_progress": 10,
                "assigned_employee_count": 0,
                "deadline": 8,
                "reward": 200,
                "difficulty": "Medium",
            }
        
        # Hard jobs
        hard_job_names = random.sample(self.hard_jobs, min(num_hard, len(self.hard_jobs)))
        for i, job_name in enumerate(hard_job_names):
            self.available_jobs[job_name] = {
                "name": job_name,
                "cost_per_worker": 30,
                "progress": 0,
                "max_progress": 15,
                "assigned_employee_count": 0,
                "deadline": 6,
                "reward": 300,
                "difficulty": "Hard",
            }

    def display_queued_jobs(self):
        """Display the jobs currently in the queue in a tabular format."""
        if not self.jobs_queue:
            print("No jobs in the queue.")
            return

        table_data = []
        headers = ["Job Name", "Deadline", "Progress", "Assigned Employees"]

        for job in self.jobs_queue:
            row = [
                job['name'],
                job['deadline'],
                job['progress'],
                job['assigned_employee_count']
            ]
            table_data.append(row)

        print("Jobs in Queue:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def queue_job(self, job_name):
        """Queue a job for processing."""
        if job_name in self.available_jobs:
            job_details = self.available_jobs[job_name]
            self.jobs_queue.append(job_details)
            print(f"Job '{job_name}' has been queued for processing.")
        else:
            print(f"Job '{job_name}' is not available.")
        
    def display_available_jobs(self):
        """Display all available jobs with numbers for user selection and return an array of job names."""
        job_names = []
        
        if not self.available_jobs:
            print("No available jobs.")
            return job_names
        
        headers = ["#", "Job Name", "Difficulty", "Cost/Worker", "Progress", "Max Progress", "Reward", "Deadline"]
        table_data = []
        
        for index, (job_name, job_details) in enumerate(self.available_jobs.items(), start=1):
            row = [
                index,  # Display job number
                job_name,
                job_details["difficulty"],
                job_details["cost_per_worker"],
                job_details["progress"],
                job_details["max_progress"],
                job_details["reward"],
                job_details["deadline"]
            ]
            table_data.append(row)
            job_names.append(job_name)  # Collect job names
        
        print("Available Jobs:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        return job_names

    def assign_workers_to_job(self, job_name, worker_count):
        """Assign workers to a job and handle the associated costs."""
        if job_name not in self.available_jobs:
            print(f"Job '{job_name}' not found.")
            return
        
        if worker_count > self.current_available_employee_count:
            print("Not enough available employees.")
            return

        job = self.available_jobs[job_name]
        job["assigned_employee_count"] += worker_count
        total_cost = worker_count * job["cost_per_worker"]
        
        if total_cost > self.current_funds:
            print("Not enough funds to assign that many workers.")
            job["assigned_employee_count"] -= worker_count
            return

        self.decrease_current_funds(total_cost)
        self.current_available_employee_count -= worker_count
        print(f"Assigned {worker_count} worker(s) to job '{job_name}'.")

    def hire_workers(self, count):
        """Hire workers and handle the associated costs."""
        # if count + self.current_available_employee_count > self.max_employee_population:
        #     print("No space for more employees.")
        #     return

        total_cost = count * self.FIXED_COST_PER_WORKER       
        if total_cost > self.current_funds:
            print("Not enough funds to hire that many workers.")
            return
        
        # Deduct cost and update employee counts
        self.decrease_current_funds(total_cost)
        self.current_available_employee_count += count
        
        print(f"Hired {count} worker(s).")

    def get_worker_cost(self):
        return self.FIXED_COST_PER_WORKER
    
    # def increase_max_employee_count(self, amount):
    #     self.max_employee_population += amount 
        
    def increase_available_employee_count(self, amount):
        self.current_available_employee_count += amount 
        
    # def decrease_max_employee_count(self, amount):
    #     self.max_employee_population -= amount 
        
    def decrease_available_employee_count(self, amount):
        self.current_available_employee_count -= amount 
    
    def increase_current_funds(self, amount):
        self.current_funds += amount

    def decrease_current_funds(self, amount):
        self.current_funds -= amount 

    def update_current_funds(self, amount):
        self.current_funds = amount

    def get_current_funds(self):
        return self.current_funds
    
    def get_population_ratio(self):
        # Return a formatted string showing available employees over max population
        return f"{self.current_available_employee_count}"
    
    def add_job(self, job_name, cost_per_worker, max_progress, reward, deadline):
        self.available_jobs[job_name] = {
            "name": job_name,
            "cost_per_worker": cost_per_worker,
            "progress": 0,
            "max_progress": max_progress,
            "assigned_employee_count": 0,
            "deadline": deadline,
            "reward": reward
        }

    def handle_failed_jobs(self):
        """Handle failed jobs due to missing deadlines or other reasons."""
        for job in self.jobs_queue:
            if job["progress"] < job["max_progress"]:
                self.failed_jobs += 1
                print(f"Job '{job['name']}' failed due to unmet deadline.")
        self.jobs_queue = [job for job in self.jobs_queue if job["progress"] >= job["max_progress"]]

    def game_over(self):
        """Determine if the game is over based on company status."""
        if self.current_funds <= 0:
            self.dead = True
            
        elif self.failed_jobs > 0:
            self.dead = True
            print("Game Over: Too many failed jobs.")

    def is_dead(self):
        return self.dead
    
    def display_company_status(self):
        """Display the current status of the company."""
        print(f"Current Funds: ${self.current_funds}")
        print(f"Available Employees: {self.current_available_employee_count}")

        # Display status of jobs in the queue
        if self.jobs_queue:
            print("\nJobs in Queue:")
            for job in self.jobs_queue:
                print(f"  - {job['name']}: Progress {job['progress']}/{job['max_progress']}, "
                      f"Deadline {job['deadline']}, Workers Assigned: {job['assigned_employee_count']}")
        else:
            print("\nNo jobs in the queue.")

        # Display status of completed and failed jobs
        print(f"\nCompleted Jobs: {self.completed_jobs}")
        print(f"Failed Jobs: {self.failed_jobs}")

        # Display status of available jobs
        if self.available_jobs:
            print("\nAvailable Jobs:")
            for job_name, job in self.available_jobs.items():
                print(f"  - {job_name}: Difficulty {job['difficulty']}, Reward ${job['reward']}, "
                      f"Cost per Worker ${job['cost_per_worker']}, Deadline {job['deadline']}")
        else:
            print("\nNo available jobs at the moment.")
            
    def check_company_status(self):
        """Check and update the current status of the company."""
        if self.current_funds <= 0:
            self.dead = True
            print("Company is bankrupt!")
            return

        if self.jobs_queue:
            # Process jobs in the queue
            jobs_to_remove = []  # List to keep track of jobs that need to be removed

            for job in self.jobs_queue:
                job["progress"] += job["assigned_employee_count"]

                if job["progress"] >= job["max_progress"]:
                    # Job completed
                    self.current_funds += job["reward"]
                    self.completed_jobs += 1
                    print(f"Job '{job['name']}' completed! Reward received: ${job['reward']}.")
                    jobs_to_remove.append(job)
                elif job["deadline"] <= 0:
                    # Job missed deadline
                    self.failed_jobs += 1
                    print(f"Job '{job['name']}' missed its deadline.")
                    jobs_to_remove.append(job)
                else:
                    # Update job deadline
                    job["deadline"] -= 1

            # Remove jobs that were completed or missed deadline
            for job in jobs_to_remove:
                self.jobs_queue.remove(job)
        else:
            print("No jobs to report.")

        # Optionally, populate available jobs with new ones
        self.populate_jobs(2, 1, 0)  # Adjust the numbers as needed



        # if self.dead:
        #     self.update_company_is_dead(True)
        # else:
        #     # display informationa bout selecting jobs 
        #     if self.selected_jobs:
        #         for job in self.selected_jobs:
        #             if job['assigned_employee_count']:
        #                 self.update_selected_job_progress(job['name'],job['assigned_employee_count'])
        #             if job['progress'] >= job['max_progress']:
        #                 self.increase_available_employee_count(job['assigned_employee_count'])
        #                 self.increase_current_funds(job['reward'])
        #                 self.completed_jobs += 1
        #                 self.remove_selected_job(job['name'])
        #             else:
        #                 # will need to replace this magic number 
        #                 self.update_selected_job_deadline(job['name'],1)
        #             if job['deadline'] <= 0:
        #                 print(f"Job '{job['name']}' has missed the deadline")
        #                 self.failed_jobs += 1
        #                 self.remove_selected_job(job['name'])
        #     else:
        #         print('No select jobs to report')
