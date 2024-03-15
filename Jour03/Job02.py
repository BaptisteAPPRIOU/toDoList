from Job01 import Task

class taskManager():
    
    def __init__(self):
        self.liste = []

    def add(self,a,b,c,d,e):
        z = Task(a,b,c,d,e)
        self.liste.append(z)
        print(f"Nouvelle tâche : {z.get_title()}")
    
    def delete(self,Task_index):
        if 0 <= Task_index < len(self.liste):
            task_deleted = self.liste.pop(Task_index)
            print("Tâche supprimée : ",str(task_deleted))
        else:
            print("Pas de tâche à supprimer")
                
    def show(self):
        if self.liste:
            for i in range(len(self.liste)):
                print(self.liste[i].get_title())
        else:
            print("Pas de tâche à afficher")
