import tkinter as tk

class TodoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_list = tk.Listbox(self.root)
        self.task_list.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.update_task_list()
        self.task_entry.delete(0, tk.END)
        
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

if _name_ == "_main_":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
