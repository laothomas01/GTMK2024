# # from assignment import Assignment

class Company:
    def __init__(self,starting_funds,starting_employee_count):
        self.current_funds = starting_funds
        self.current_available_employee_count = starting_employee_count
        self.selected_jobs = []
        self.available_jobs = {
                "Job A": {
                    "name": "Job A",
                    "cost": 20,
                    "progress": 0,
                    "max_progress": 3,
                    "assigned_employees": 0,
                    "deadline": 5,
                    "difficulty": "Easy"
                }
                ,
                "Job B": {
                    "name": "Job B",
                    "cost": 40,
                    "progress": 0,
                    "max_progress": 6,
                    "assigned_employees": 0,
                    "deadline": 10,
                    "difficulty": "Medium"
                    }
        }
        
    def print_available_jobs(self):
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
    
    def add_selected_job(self,job_name):
        if job_name in self.available_jobs:
            self.selected_jobs.append(self.available_jobs[job_name])
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

    def remove_selected_job(self,job_name):
        if self.selected_jobs:
            for job in self.selected_jobs:
                if job['name'] == job_name:
                    self.selected_jobs.remove(job)
                    print(f"Job '{job_name}' has been removed from selected jobs.")
                    return
                print(f"Job '{job_name}' not found in selected jobs.")
        else:
             print("No jobs have been selected yet.")

    def update_selected_job_progress(self,job_name,progress_amount):
        if self.selected_jobs:
            for job in self.selected_jobs:
                if job['name'] == job_name:
                    self.selected_jobs['progress'] += progress_amount
       
    
    
     # for job_name, job_details in self.selec_jobs.items():
        #     print(f"Job Name: {job_name}")
        #     for key, value in job_details.items():
        #         print(f"  {key}: {value}")
        #     print()  # Adds a blank line between jobs





# class Company:
#     def __init__(self,total_funding,employee_count):
#             self.total_funding = total_funding
#             self.employee_count = employee_count
#             self.available_jobs = {
#                  "a" :  {
#                       "a" : 0
#                  }
#                 # "Job A": {
#                 #     "name": "Job A",
#                 #     "cost": 20,
#                 #     "progress": 0,
#                 #     "max_progress": 3,
#                 #     "assigned_employees": 0,
#                 #     "deadline": 5,
#                 #     "difficulty": "Easy"
#                 # }



#                 # ,
#                 # "Job B": {
#                 #     "name": "Job B",
#                 #     "cost": 40,
#                 #     "progress": 0,
#                 #     "max_progress": 6,
#                 #     "assigned_employees": 0,
#                 #     "deadline": 10,
#                 #     "difficulty": "Medium"
#                 #     }
#                 }
#     def print_funding(self):
#          print(self.total_funding)
#          print(self.available_jobs)
#     def get_available_jobs(self):
#          return self.available_jobs
#     def print_available_jobs(self):
#         print(self.available_jobs)
#         # for job_name, job_details in self.available_jobs.items():
#         #     print(f"Job Name: {job_name}")
#         #     for key, value in job_details.items():
#         #         print(f"  {key}: {value}")
#         #     print()
#     # def update_selected_job_progress(self,difficulty,job_name,progress,update):
#     #     self.selected_jobs[difficulty][job_name][progress] += update

#     # def update_selected_job_deadline(self,difficulty,job_name,deadline,update):
#     #     self.selected_jobs[difficulty][job_name][deadline] += update

#     # def get_available_job(self,difficulty,job_name):
#     #     return self.available_jobs[difficulty][job_name]
    
#     # def get_easy_difficulty_job(self,job_name):
#     #     return self.available_jobs["Easy"][job_name]
    
#     # def get_medium_difficulty_job(self,job_name):
#     #     return self.available_jobs["Medium"][job_name]
    
#     # def update_easy_difficulty_job_progress(self,jobname,progress_amount):
#     #     self.selected_jobs["Easy"][jobname]["progress"] += progress_amount

#     # def hire_employee(self,amount):
#     #     cost_per_employee = 25
#     #     total_cost = cost_per_employee * amount 
#     #     self.total_funding = self.total_funding - total_cost
    
#     # def s/elect_job(self,difficulty,job_name):
         
#     # def select_job(self,difficulty,job_name):
#     #     self.selected_jobs.append(self.get_selected_job(difficulty,job_name))
#     # def 
        
    

    

#     # def add_project(self,)

# # class Company:
# #     def __init__(self, overall_funding, employee_count):
# #         self.assignments = {}  # Dictionary with string keys and Assignment values
# #         self.overall_funding = overall_funding
# #         self.employee_count = employee_count
# #         self.available_employee_count = employee_count
    
# #     def hire_employees(self,amount):
# #         self.employee_count += amount 
# #         # self.employee_count += 1
# #         # print(f"Employee hired. Total employees: {self.employee_count}")

# #     def fire_employees(self,amount):
# #         self.employee_count -= amount 
# #     #     if self.employee_count > 0:
# #     #         self.employee_count -= 1
# #     #         print(f"Employee fired. Total employees: {self.employee_count}")
# #     #     else:
# #     #         print("No employees to fire.")

# #     def increase_funds(self, amount):
# #         self.overall_funding += amount 
# #     #     self.overall_funding += amount
# #     #     print(f"Funds increased by {amount}. Total funds: {self.overall_funding}")

# #     def decrease_funds(self, amount):
# #         self.overall_funding -= amount 
# #     #     if self.overall_funding >= amount:
# #     #         self.overall_funding -= amount
# #     #         print(f"Funds decreased by {amount}. Total funds: {self.overall_funding}")
# #     #     else:
# #     #         print("Insufficient funds to decrease.")

# #     def add_assignment(self, key, assignment):
# #             self.assignments[key] = assignment 
# #     #     if key not in self.assignments:
# #     #         self.assignments[key] = assignment
# #     #         print(f"Assignment '{key}' added.")
# #     #     else:
# #     #         print(f"Assignment '{key}' already exists.")
# #     def remove_assignment(self,key):
# #         self.assignments.pop(key)
        
# #     def increase_available_employee_count(self,amount):
# #     #     if(amount >= self.employee_count):
# #     #         self.available_employee_count = self.employee_count
# #     #     else:
# #         self.available_employee_count += amount
    
# #     def decrease_available_employee_count(self,amount):
# #     #     if(amount >= self.employee_count):
# #     #         self.available_employee_count = 0
# #     #     else:
# #         self.available_employee_count -= amount