import tkinter as tk
import tkinter.messagebox
from Job01 import Task
from Job02 import taskManager 

class MyTaskManager():
    
    def getEntry(self):
        nom = self.Entry1.get()
        description = self.Entry2.get()
        date = self.Entry3.get()
        completion = self.check_state.get()
        priority = self.Entry4.get()                                        # Job04
        print(nom," ",description," ",date," ",completion)
        self.Liste_de_tache.add(nom,description,date,completion,priority)
        self.Entry1.delete(0, tk.END)
        self.Entry2.delete(0, tk.END)
        self.Entry3.delete(0, tk.END)
        self.Entry4.delete(0, tk.END)
    
    def delete_task(self):
        index = self.task_list.curselection()
        if index:
            index = int(index[0])
            self.Liste_de_tache.delete(index)
            self.task_list.delete(index) 
            
    def show_tasks(self):
        self.task_list.delete(0, tk.END)
        for Task in self.Liste_de_tache.liste:
            self.task_list.insert(tk.END, Task.task_title)
    
    def show_tasks_details(self, event):
        index = self.task_list.curselection()
        if index:
            index = int(index[0])
            Task = self.Liste_de_tache.liste[index]
            if Task.task_completed == 1:
                Details = f"Titre : {Task.task_title}\nDescription : {Task.task_description}\nDate : {Task.task_due_date}\nComplétion : oui\nOrdre de priorité : {Task.task_priority}"
            else:
                Details = f"Titre : {Task.task_title}\nDescription : {Task.task_description}\nDate : {Task.task_due_date}\nComplétion : non\nOrdre de priorité : {Task.task_priority}"
            tk.messagebox.showinfo("Détails de la tâche : \n",Details)
        
    def __init__(self):
        self.Liste_de_tache = LISTE
        self.root = tk.Tk()
        
        self.root.geometry("700x700")
        self.root.title("Mon task manager")
        self.label = tk.Label(self.root, text="Votre task manager", font=('Arial',18))
        self.label.pack(padx=20, pady=20)
        
        self.label = tk.Label(self.root, text="Nom de la tâche", font=('Arial',14))
        self.label.pack(padx=10, pady=10)
        self.Entry1 = tk.Entry(self.root, width=60, font=('Arial', 16))
        self.Entry1.pack(padx=10)
        self.label = tk.Label(self.root, text="Description", font=('Arial',14))
        self.label.pack(padx=10, pady=10)
        self.Entry2 = tk.Entry(self.root, width=60, font=('Arial', 16))
        self.Entry2.pack(padx=10)
        self.label = tk.Label(self.root, text="Date de rendu", font=('Arial',14))
        self.label.pack(padx=10, pady=10)
        self.Entry3 = tk.Entry(self.root, width=60, font=('Arial', 16))
        self.Entry3.pack(padx=10)
        # Job04
        self.label = tk.Label(self.root, text="Ordre de priorité", font=('Arial',14))
        self.label.pack(padx=10, pady=10)
        self.Entry4 = tk.Entry(self.root, width=60, font=('Arial', 16))
        self.Entry4.pack(padx=10)
        
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Complété ?", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.ButtonFrame = tk.Frame(self.root)
        self.ButtonFrame.columnconfigure(0,weight=1)
        self.ButtonFrame.columnconfigure(1,weight=1)
        self.ButtonFrame.columnconfigure(2,weight=1)
        self.btn1 = tk.Button(self.ButtonFrame, text="Add", command=self.getEntry)
        self.btn1.grid(row=0, column=0,padx= 10,  sticky=tk.W+tk.E)
        self.btn2 = tk.Button(self.ButtonFrame, text="Delete", command=self.delete_task)
        self.btn2.grid(row=0, column=1,padx= 10,  sticky=tk.W+tk.E)
        self.btn3 = tk.Button(self.ButtonFrame, text="Show", command=self.show_tasks)
        self.btn3.grid(row=0, column=2,padx= 10,  sticky=tk.W+tk.E)
        self.ButtonFrame.pack(fill='x')
        
        self.task_list = tk.Listbox(self.root, width=60)
        self.task_list.pack(padx=10, pady=10)
        self.task_list.bind("<Double-Button-1>", self.show_tasks_details)
        
        self.root.mainloop()
        
    
        
LISTE = taskManager()
MyTaskManager()