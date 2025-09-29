import tkinter as tk
from tkinter import messagebox

# Inicializamos la pila
pila = []

# Función para actualizar la visualización
def actualizar_pila():
    lista.delete(0, tk.END)
    for elemento in reversed(pila):  # Mostramos el tope arriba
        lista.insert(tk.END, elemento)

# Función para apilar (push)
def push():
    valor = entrada.get()
    if valor != "":
        pila.append(valor)
        entrada.delete(0, tk.END)
        actualizar_pila()
    else:
        messagebox.showwarning("Advertencia", "No puedes insertar un valor vacío")

# Función para desapilar (pop)
def pop():
    if pila:
        elemento = pila.pop()
        messagebox.showinfo("Elemento eliminado", f"Se quitó: {elemento}")
        actualizar_pila()
    else:
        messagebox.showwarning("Advertencia", "La pila está vacía")

# Crear ventana
ventana = tk.Tk()
ventana.title("Visualización de Pila")
ventana.geometry("300x400")

# Entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)

# Botones
boton_push = tk.Button(ventana, text="Apilar (Push)", command=push, bg="lightgreen")
boton_push.pack(pady=5)

boton_pop = tk.Button(ventana, text="Desapilar (Pop)", command=pop, bg="lightcoral")
boton_pop.pack(pady=5)

# Lista visual de la pila
lista = tk.Listbox(ventana, font=("Arial", 14), height=10)
lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Mostrar la pila inicial
actualizar_pila()

# Ejecutar ventana
ventana.mainloop()
