import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")


        self.tasks = []


        self.create_widgets()

    def create_widgets(self):

        self.entry = tk.Entry(self.root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.add_task)  # Permitir añadir tarea con Enter


        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)


        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)


        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self, event=None):
        task = self.entry.get()  # Obtener el texto de la tarea
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            completed_task = f"✔️ {task}"
            self.tasks[selected_task_index] = completed_task
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):

        self.task_listbox.delete(0, tk.END)


        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
