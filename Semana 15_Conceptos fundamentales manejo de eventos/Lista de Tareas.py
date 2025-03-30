# Objetivo: Desarrollar una aplicación GUI simple para gestionar una lista de tareas, permitiendo al usuario añadir nuevas tareas, marcarlas como
# completadas y eliminarlas. La aplicación deberá responder adecuadamente a los eventos del usuario, como clics del ratón y pulsaciones del teclado.


import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def on_enter_pressed(event):
    add_task()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", on_enter_pressed)

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()