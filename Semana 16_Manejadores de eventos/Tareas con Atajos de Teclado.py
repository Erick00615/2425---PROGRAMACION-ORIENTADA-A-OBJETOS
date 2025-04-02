#Objetivo: Desarrollar una aplicación GUI que permita a los usuarios gestionar una lista de tareas pendientes. La aplicación deberá permitir añadir
#nuevas tareas, marcar tareas como completadas, y eliminar tareas utilizando tanto la interfaz gráfica (clics de botón) como atajos de teclado.


import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

def mark_completed(event=None):
    try:
        selected_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_index)
        if not task_text.startswith("✔ "):
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, "✔ " + task_text)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")

def delete_task(event=None):
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")

def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Campo de entrada de tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

# Botones
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Añadir", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Completada", command=mark_completed).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Eliminar", command=delete_task).grid(row=0, column=2, padx=5)

# Lista de tareas
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Asignar atajos de teclado
root.bind("<c>", mark_completed)  # Marcar tarea como completada
root.bind("<d>", delete_task)  # Eliminar tarea
root.bind("<Delete>", delete_task)  # También eliminar con tecla Delete
root.bind("<Escape>", close_app)  # Cerrar aplicación

root.mainloop()

