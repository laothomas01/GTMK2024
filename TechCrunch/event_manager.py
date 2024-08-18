# class EventManager:
#     def __init__(self):
#         self.events = {}  # Dictionary to store events

#     def add_event(self, key, event):
#         if key in self.events:
#             print(f"Event with key '{key}' already exists.")
#         else:
#             self.events[key] = event
#             print(f"Event '{event.name}' added with key '{key}'.")

#     def remove_event(self, key):
#         if key in self.events:
#             removed_event = self.events.pop(key)
#             print(f"Event '{removed_event.name}' removed.")
#         else:
#             print(f"No event found with key '{key}'.")

#     def get_event(self, key):
#         return self.events.get(key, None)

#     def perform_all_tasks(self):
#         for event in self.events.values():
#             event.do_task()
#     def perform_task(self,task_name):
#         event = self.get_event(task_name)
#         if event:
#             event.do_task()
#         else:
#             print(f"No event found with key '{task_name}'.")
    