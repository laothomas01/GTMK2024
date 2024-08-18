# from assignment import Assignment

class Company:
    def __init__(self,total_funding,employee_count):
        self.total_funding = total_funding,
        self.employee_count = employee_count
        self.availabe_employee_count = employee_count
        self.selected_jobs = {}
        self.available_jobs = {
            # a dictionary where
            # the key is mapped to another dictionary 
            "Easy" : {
                "Job A" :
                {   "name" : "Job A",
                    "cost" : 20,
                    "progress" : 3,
                    "assigned_employees" : 0,
                    "deadline": 5,
                    # "reward" : random.range(50,100)
                }
            },
            
            # "Easy" : {
            #     {
            #         "name" : "Job A",
            #         "cost" : 20,
            #         "progress" : 3,
            #         "assigned_employees" : 0,
            #         "deadline": 5,
            #         "reward" : random.range(50,100)
            #     }
            # },

            "Medium" : 
            {
                "Job B" : 
                {
                    "name" : "Job B",
                    "cost" : 40,
                    "progress" : 6,
                    "assigned_employees" : 0,
                    "deadline": 10,
                    # "reward" : random.range(100,200)
                }

            }
        }
    
    def start_game(self,run):
        company = Company(self.current_money,self.current_employee_count)

    def update_selected_job_progress(self,difficulty,job_name,progress,update):
        self.selected_jobs[difficulty][job_name][progress] += update

    def update_selected_job_deadline(self,difficulty,job_name,deadline,update):
        self.selected_jobs[difficulty][job_name][deadline] += update

    def get_selected_job(self,difficulty,job_name):
        return self.available_jobs[difficulty][job_name]
    
    def get_easy_difficulty_job(self,job_name):
        return self.available_jobs["Easy"][job_name]
    
    def get_medium_difficulty_job(self,job_name):
        return self.available_jobs["Medium"][job_name]
    
    def update_easy_difficulty_job_progress(self,jobname,progress_amount):
        self.selected_jobs["Easy"][jobname]["progress"] += progress_amount

    def hire_employee(self,amount):
        cost_per_employee = 25
        total_cost = cost_per_employee * amount 
        self.total_funding = self.total_funding - total_cost

    # def select_job(self,difficulty,job_name):
    #     self.selected_jobs.append(self.get_selected_job(difficulty,job_name))
    
    def print_selected_jobs(self):
        pass
        # print(self.selected_jobs)

    def print_available_jobs(self):
        for difficulty, jobs in self.available_jobs.items():
            print(f"Difficulty: {difficulty}")
            for job_name, job_details in jobs.items():
                print(f"Job Name: {job_name}")
                for detail_key, detail_value in job_details.items():
                    print(f"  {detail_key.capitalize()}: {detail_value}")
                print()  # Add a line break between jobs
    

    

    # def add_project(self,)

# class Company:
#     def __init__(self, overall_funding, employee_count):
#         self.assignments = {}  # Dictionary with string keys and Assignment values
#         self.overall_funding = overall_funding
#         self.employee_count = employee_count
#         self.available_employee_count = employee_count
    
#     def hire_employees(self,amount):
#         self.employee_count += amount 
#         # self.employee_count += 1
#         # print(f"Employee hired. Total employees: {self.employee_count}")

#     def fire_employees(self,amount):
#         self.employee_count -= amount 
#     #     if self.employee_count > 0:
#     #         self.employee_count -= 1
#     #         print(f"Employee fired. Total employees: {self.employee_count}")
#     #     else:
#     #         print("No employees to fire.")

#     def increase_funds(self, amount):
#         self.overall_funding += amount 
#     #     self.overall_funding += amount
#     #     print(f"Funds increased by {amount}. Total funds: {self.overall_funding}")

#     def decrease_funds(self, amount):
#         self.overall_funding -= amount 
#     #     if self.overall_funding >= amount:
#     #         self.overall_funding -= amount
#     #         print(f"Funds decreased by {amount}. Total funds: {self.overall_funding}")
#     #     else:
#     #         print("Insufficient funds to decrease.")

#     def add_assignment(self, key, assignment):
#             self.assignments[key] = assignment 
#     #     if key not in self.assignments:
#     #         self.assignments[key] = assignment
#     #         print(f"Assignment '{key}' added.")
#     #     else:
#     #         print(f"Assignment '{key}' already exists.")
#     def remove_assignment(self,key):
#         self.assignments.pop(key)
        
#     def increase_available_employee_count(self,amount):
#     #     if(amount >= self.employee_count):
#     #         self.available_employee_count = self.employee_count
#     #     else:
#         self.available_employee_count += amount
    
#     def decrease_available_employee_count(self,amount):
#     #     if(amount >= self.employee_count):
#     #         self.available_employee_count = 0
#     #     else:
#         self.available_employee_count -= amount