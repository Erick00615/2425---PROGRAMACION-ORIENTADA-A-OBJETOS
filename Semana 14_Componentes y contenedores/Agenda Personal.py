#Objetivo: Desarrollar una aplicación GUI utilizando Tkinter en Python que funcione como una agenda personal.
#La aplicación permitirá al usuario agregar, ver, y eliminar eventos o tareas programadas.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

# Función para agregar un evento a la lista
def agregar_evento():
    # Obtiene los datos de los campos de entrada
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    # Validación simple para verificar si los campos están vacíos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    # Agrega el evento a la lista
    tree.insert('', 'end', values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada después de agregar
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    # Obtiene el evento seleccionado
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
        return

    # Confirmar eliminación
    confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
    if confirmar:
        tree.delete(selected_item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Crear los contenedores (Frames)
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

frame_eventos = tk.Frame(ventana)
frame_eventos.pack(pady=10)

# Etiquetas y campos de entrada para fecha, hora y descripción
label_fecha = tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):")
label_fecha.grid(row=0, column=0, padx=5)

entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5)

entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5)

# Botones para agregar y eliminar eventos
btn_agregar = tk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(frame_entrada, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=10)

# Crear la lista de eventos (TreeView)
tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill=tk.BOTH, expand=True)

# Botón para salir de la aplicación
btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()