class Task():
    
    def __init__(self,title,description,due_date,completed,priority):
        self.task_title = title
        self.task_description = description
        self.task_due_date = due_date
        self.task_completed = completed
        self.task_priority = priority                       # Job04
    
    def get_title(self):
        return self.task_title
    
    def get_description(self):
        return self.task_description
    
    def get_due_date(self):
        return self.task_due_date
    
    def get_completed(self):
        return self.task_completed
    
    def get_priority(self):                     # Job04
        return self.task_priority
    
    def set_title(self,a):
        self.task_title = a
    
    def set_description(self,a):
        self.task_description = a
    
    def set_due_date(self,a):
        self.task_due_date = a
    
    def set_completed(self,a):
        self.task_completed = a
    
    def set_priority(self,a):                   # Job04
        self.task_priority = a