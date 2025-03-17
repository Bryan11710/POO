import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entry.get().strip()
    if dato:
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

def limpiar_datos():
    if lista.size() > 0:
        lista.delete(0, tk.END)
    else:
        messagebox.showinfo("Información", "La lista ya está vacía.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Datos GUI")
root.geometry("400x300")
root.resizable(False, False)

# Marco principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Etiqueta
label = tk.Label(frame, text="Ingrese un dato:", font=("Arial", 12))
label.pack(pady=5)

# Campo de texto
entry = tk.Entry(frame, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Botón Agregar
tagregar = tk.Button(frame, text="Agregar", font=("Arial", 12), command=agregar_dato)
tagregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(frame, font=("Arial", 12), height=10)
lista.pack(pady=5, fill=tk.BOTH, expand=True)

# Botón Limpiar
tlimpiar = tk.Button(frame, text="Limpiar", font=("Arial", 12), command=limpiar_datos)
tlimpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
