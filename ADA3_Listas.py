import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ==============================
# ESTRUCTURA DE DATOS PRINCIPAL
# ==============================
POSTRES = []  # lista de diccionarios [{'postre': 'Flan', 'ingredientes': ['leche','huevo']}]

def ordenar_postres():
    POSTRES.sort(key=lambda x: x['postre'].lower())

def find_index(nombre):
    for i, p in enumerate(POSTRES):
        if p['postre'].lower() == nombre.lower():
            return i
    return None

# ==============================
# FUNCIONES DE LÓGICA
# ==============================

def mostrar_postres():
    """Actualiza la lista visual de postres."""
    lista_postres.delete(0, tk.END)
    for p in POSTRES:
        lista_postres.insert(tk.END, p['postre'])

def alta_postre():
    nombre = entry_postre.get().strip()
    if not nombre:
        messagebox.showerror("Error", "Debes ingresar un nombre de postre.")
        return
    if find_index(nombre) is not None:
        messagebox.showwarning("Aviso", "Ese postre ya existe.")
        return
    ingredientes = simpledialog.askstring("Ingredientes", 
        "Introduce los ingredientes separados por comas (,):")
    if not ingredientes:
        messagebox.showerror("Error", "Debes ingresar al menos un ingrediente.")
        return
    lista = [i.strip() for i in ingredientes.split(",") if i.strip()]
    POSTRES.append({'postre': nombre, 'ingredientes': lista})
    ordenar_postres()
    mostrar_postres()
    messagebox.showinfo("Éxito", f"Postre '{nombre}' agregado correctamente.")

def baja_postre():
    seleccion = lista_postres.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un postre para eliminar.")
        return
    nombre = lista_postres.get(seleccion)
    idx = find_index(nombre)
    if idx is not None:
        POSTRES.pop(idx)
        mostrar_postres()
        lista_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Postre '{nombre}' eliminado.")

def mostrar_ingredientes(event=None):
    """Cuando el usuario selecciona un postre, se muestran sus ingredientes."""
    lista_ingredientes.delete(0, tk.END)
    seleccion = lista_postres.curselection()
    if not seleccion:
        return
    nombre = lista_postres.get(seleccion)
    idx = find_index(nombre)
    if idx is None:
        return
    for ing in POSTRES[idx]['ingredientes']:
        lista_ingredientes.insert(tk.END, ing)

def insertar_ingrediente():
    seleccion = lista_postres.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un postre primero.")
        return
    nombre = lista_postres.get(seleccion)
    idx = find_index(nombre)
    nuevo = simpledialog.askstring("Nuevo ingrediente", "Ingresa el nombre del nuevo ingrediente:")
    if not nuevo:
        return
    if nuevo.lower() in (i.lower() for i in POSTRES[idx]['ingredientes']):
        messagebox.showwarning("Aviso", f"'{nuevo}' ya está en la lista de '{nombre}'.")
        return
    POSTRES[idx]['ingredientes'].append(nuevo.strip())
    mostrar_ingredientes()
    messagebox.showinfo("Éxito", f"Ingrediente '{nuevo}' añadido a '{nombre}'.")

def eliminar_ingrediente():
    seleccion_postre = lista_postres.curselection()
    seleccion_ing = lista_ingredientes.curselection()
    if not seleccion_postre or not seleccion_ing:
        messagebox.showwarning("Aviso", "Selecciona un postre y un ingrediente.")
        return
    nombre = lista_postres.get(seleccion_postre)
    ingrediente = lista_ingredientes.get(seleccion_ing)
    idx = find_index(nombre)
    POSTRES[idx]['ingredientes'].remove(ingrediente)
    mostrar_ingredientes()
    messagebox.showinfo("Éxito", f"Ingrediente '{ingrediente}' eliminado de '{nombre}'.")

def quitar_duplicados():
    seen = {}
    nuevos = []
    for p in POSTRES:
        key = p['postre'].lower()
        if key not in seen:
            seen[key] = set(map(str.lower, p['ingredientes']))
        else:
            seen[key].update(map(str.lower, p['ingredientes']))
    for name, ing_set in seen.items():
        nuevos.append({'postre': name.capitalize(), 'ingredientes': sorted(list(ing_set))})
    nuevos.sort(key=lambda x: x['postre'].lower())
    POSTRES.clear()
    POSTRES.extend(nuevos)
    mostrar_postres()
    lista_ingredientes.delete(0, tk.END)
    messagebox.showinfo("Limpieza completa", "Duplicados eliminados y listas combinadas correctamente.")

# ==============================
# INTERFAZ GRÁFICA (Tkinter)
# ==============================
root = tk.Tk()
root.title("Gestión de Postres 🍰")
root.geometry("700x500")
root.resizable(False, False)

# Marco de Postres
frame_postres = tk.LabelFrame(root, text="Postres", padx=10, pady=10)
frame_postres.pack(side="left", fill="y", padx=10, pady=10)

entry_postre = tk.Entry(frame_postres, width=25)
entry_postre.pack()
tk.Button(frame_postres, text="Agregar Postre", command=alta_postre).pack(pady=3)
tk.Button(frame_postres, text="Eliminar Postre", command=baja_postre).pack(pady=3)
tk.Button(frame_postres, text="Eliminar Duplicados", command=quitar_duplicados).pack(pady=3)

lista_postres = tk.Listbox(frame_postres, width=30, height=20)
lista_postres.pack(pady=10)
lista_postres.bind("<<ListboxSelect>>", mostrar_ingredientes)

# Marco de Ingredientes
frame_ing = tk.LabelFrame(root, text="Ingredientes", padx=10, pady=10)
frame_ing.pack(side="right", fill="both", expand=True, padx=10, pady=10)

lista_ingredientes = tk.Listbox(frame_ing, width=40, height=20)
lista_ingredientes.pack(pady=10)

tk.Button(frame_ing, text="Agregar Ingrediente", command=insertar_ingrediente).pack(pady=3)
tk.Button(frame_ing, text="Eliminar Ingrediente", command=eliminar_ingrediente).pack(pady=3)

# Iniciar interfaz
mostrar_postres()
root.mainloop()
