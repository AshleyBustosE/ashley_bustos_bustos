# Actualización realizada para actividad de control de versiones con Git

import tkinter as tk
from tkinter import ttk, messagebox

from crud import (
    agregar_paciente,
    mostrar_pacientes,
    actualizar_paciente,
    eliminar_paciente
)

# -----------------------------
# Funciones
# -----------------------------

# Limpiar los campos de entrada
def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_diagnostico.delete(0, tk.END)
    entry_correo.delete(0, tk.END)

# Cargar los pacientes en la tabla
def cargar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

    pacientes = mostrar_pacientes()
    if pacientes:
        for paciente in pacientes:
            tabla.insert("", tk.END, values=paciente)
    else:
        messagebox.showinfo("Información", "No hay pacientes registrados.")

# Agregar un paciente a la base de datos
def agregar():

    if(
        entry_id.get() == "" or
        entry_nombre.get() == "" or
        entry_edad.get() == "" or
        entry_genero.get() == "" or
        entry_diagnostico.get() == "" or
        entry_correo.get() == ""
    ):
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos antes de agregar un paciente.")
        return

    agregado = agregar_paciente(
        entry_id.get(),
        entry_nombre.get(),
        entry_edad.get(),
        entry_genero.get(),
        entry_diagnostico.get(),
        entry_correo.get()
    )

    if agregado:
        messagebox.showinfo("Éxito", "El paciente ha sido agregado correctamente.")
        limpiar_campos()
        cargar_tabla()
    else:
        messagebox.showerror("Error", "No se pudo agregar el paciente. Intente nuevamente.")

# Actualizar un paciente en la base de datos
def actualizar():
    actualizado = actualizar_paciente(
        entry_id.get(),
        entry_nombre.get(),
        entry_edad.get(),
        entry_genero.get(),
        entry_diagnostico.get(),
        entry_correo.get()
    )

    if actualizado:
        messagebox.showinfo("Éxito", "El paciente ha sido actualizado correctamente.")
        limpiar_campos()
        cargar_tabla()
    else:
        messagebox.showerror("Error", "No se pudo actualizar el paciente. Intente nuevamente.")

# Eliminar un paciente de la base de datos
def eliminar():

    if entry_id.get() == "":
        messagebox.showwarning("Campo vacío", "Por favor, ingrese el ID del paciente que desea eliminar.")
        return

    respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este paciente?")
    if respuesta:
        eliminado = eliminar_paciente(entry_id.get())
        if eliminado:
            messagebox.showinfo("Éxito", "El paciente ha sido eliminado correctamente.")
            limpiar_campos()
            cargar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el paciente. Intente nuevamente.")

# -----------------------------
# Ventana principal
# -----------------------------

ventana = tk.Tk()
ventana.title("Gestión de Pacientes")
ventana.geometry("850x550")
ventana.resizable(False, False)


# -----------------------------
# Labels
# -----------------------------

tk.Label(ventana, text="ID").grid(row=0, column=0, padx=10, pady=5)
tk.Label(ventana, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
tk.Label(ventana, text="Edad").grid(row=2, column=0, padx=10, pady=5)
tk.Label(ventana, text="Género").grid(row=3, column=0, padx=10, pady=5)
tk.Label(ventana, text="Diagnóstico").grid(row=4, column=0, padx=10, pady=5)
tk.Label(ventana, text="Correo").grid(row=5, column=0, padx=10, pady=5)


# -----------------------------
# Entry
# -----------------------------

entry_id = tk.Entry(ventana)
entry_id.grid(row=0, column=1)

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.grid(row=1, column=1)

entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1)

entry_genero = tk.Entry(ventana)
entry_genero.grid(row=3, column=1)

entry_diagnostico = tk.Entry(ventana)
entry_diagnostico.grid(row=4, column=1)

entry_correo = tk.Entry(ventana)
entry_correo.grid(row=5, column=1)


# -----------------------------
# Botones
# -----------------------------

tk.Button(
    ventana,
    text="Agregar",
    command=agregar,
    width=15
).grid(row=6, column=0)

tk.Button(
    ventana,
    text="Actualizar",
    command=actualizar,
    width=15
).grid(row=6, column=1)

tk.Button(
    ventana,
    text="Eliminar",
    command=eliminar,
    width=15
).grid(row=6, column=2)

tk.Button(
    ventana,
    text="Mostrar",
    command=cargar_tabla,
    width=15
).grid(row=6, column=3)


# -----------------------------
# Treeview
# -----------------------------

tabla = ttk.Treeview(
    ventana, 
    columns=("ID", "Nombre", "Edad", "Género", "Diagnóstico", "Correo"),
    show="headings",
    height=12
)

tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Género", text="Género")
tabla.heading("Diagnóstico", text="Diagnóstico")
tabla.heading("Correo", text="Correo")

tabla.column("ID", width=50)
tabla.column("Nombre", width=150)
tabla.column("Edad", width=50)
tabla.column("Género", width=100)
tabla.column("Diagnóstico", width=150)
tabla.column("Correo", width=150)

# Función para seleccionar un paciente de la tabla y llenar los campos de entrada
def seleccionar_paciente(event):
    seleccionado = tabla.focus()
    if seleccionado:
        valores = tabla.item(seleccionado, "values")
        limpiar_campos()
        entry_id.insert(0, valores[0])
        entry_nombre.insert(0, valores[1])
        entry_edad.insert(0, valores[2])
        entry_genero.insert(0, valores[3])
        entry_diagnostico.insert(0, valores[4])
        entry_correo.insert(0, valores[5])

tabla.bind("<<TreeviewSelect>>", seleccionar_paciente)

tabla.grid(row=7, column=0, columnspan=7, padx=10, pady=10)

def iniciar():
    cargar_tabla()
    ventana.mainloop()


