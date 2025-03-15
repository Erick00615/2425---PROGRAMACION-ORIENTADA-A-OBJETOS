#bjetivo:
#Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios interactuar con datos de
#manera visual, utilizando los conceptos aprendidos sobre GUI.

import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_datos():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Gestión de Datos")
ventana.geometry("400x300")

# Etiqueta de instrucciones
tk.Label(ventana, text="Ingrese un dato y haga clic en 'Agregar':").pack(pady=5)

# Campo de texto para ingresar datos
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar datos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()