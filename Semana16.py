import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        self.tareas = []

        # Entrada de nueva tarea
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        btn_agregar = tk.Button(frame_botones, text="Agregar Tarea", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.completar_tarea)
        btn_completar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50, height=15)
        self.lista.pack(pady=10)

        # Enlaces de teclado
        self.entry.bind("<Return>", lambda event: self.agregar_tarea())
        root.bind("<c>", lambda event: self.completar_tarea())
        root.bind("<C>", lambda event: self.completar_tarea())  # también mayúscula
        root.bind("<d>", lambda event: self.eliminar_tarea())
        root.bind("<D>", lambda event: self.eliminar_tarea())
        root.bind("<Delete>", lambda event: self.eliminar_tarea())
        root.bind("<Escape>", lambda event: self.root.quit())

    def agregar_tarea(self):
        tarea = self.entry.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Escriba una tarea antes de agregar.")

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Ninguna seleccionada", "Seleccione una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Ninguna seleccionada", "Seleccione una tarea para eliminar.")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                self.lista.insert(tk.END, f"✔️ {texto}")
            else:
                self.lista.insert(tk.END, texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
