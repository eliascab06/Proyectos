import tkinter as tk
from tkinter import ttk, messagebox


# ------------------- MÉTODOS DE BÚSQUEDA -------------------

def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif objetivo < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1


def busqueda_hash(dicc, objetivo):
    return dicc.get(objetivo, None)



# ------------------- VENTANAS DE CADA MÉTODO -------------------

def ventana_secuencial():
    ventana = tk.Toplevel()
    ventana.title("Búsqueda Secuencial")
    ventana.geometry("500x400")

    descripcion = (
        "La búsqueda secuencial consiste en recorrer la lista\n"
        "elemento por elemento hasta encontrar el valor.\n"
        "No requiere que la lista esté ordenada."
    )

    ejemplo_lista = [4, 10, 2, 8, 6, 3, 12]
    objetivo = 8

    tk.Label(ventana, text="BÚSQUEDA SECUENCIAL", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(ventana, text=descripcion, justify="center").pack(pady=10)

    tk.Label(ventana, text=f"Ejemplo: Lista = {ejemplo_lista}\nBuscando el número {objetivo}", font=("Arial", 12)).pack(pady=10)

    resultado = busqueda_secuencial(ejemplo_lista, objetivo)
    texto = "Encontrado en la posición " + str(resultado) if resultado != -1 else "No encontrado"

    tk.Label(ventana, text="Resultado: " + texto, font=("Arial", 14, "bold")).pack(pady=10)



def ventana_binaria():
    ventana = tk.Toplevel()
    ventana.title("Búsqueda Binaria")
    ventana.geometry("500x400")

    descripcion = (
        "La búsqueda binaria divide la lista ordenada por la mitad\n"
        "y decide en qué parte buscar. Es muy eficiente.\n"
        "Requiere que la lista esté ORDENADA."
    )

    ejemplo_lista = [1, 3, 5, 7, 9, 11, 13]
    objetivo = 7

    tk.Label(ventana, text="BÚSQUEDA BINARIA", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(ventana, text=descripcion, justify="center").pack(pady=10)

    tk.Label(ventana, text=f"Ejemplo: Lista = {ejemplo_lista}\nBuscando el número {objetivo}", font=("Arial", 12)).pack(pady=10)

    resultado = busqueda_binaria(ejemplo_lista, objetivo)
    texto = "Encontrado en la posición " + str(resultado) if resultado != -1 else "No encontrado"

    tk.Label(ventana, text="Resultado: " + texto, font=("Arial", 14, "bold")).pack(pady=10)



def ventana_hash():
    ventana = tk.Toplevel()
    ventana.title("Búsqueda Hash")
    ventana.geometry("500x400")

    descripcion = (
        "La búsqueda mediante hash utiliza una tabla hash (diccionario),\n"
        "donde cada elemento se almacena bajo una clave única.\n"
        "Permite búsquedas extremadamente rápidas."
    )

    ejemplo_dicc = {"A001": "Juan", "A002": "María", "A003": "Luis"}
    objetivo = "A002"

    tk.Label(ventana, text="BÚSQUEDA HASH", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(ventana, text=descripcion, justify="center").pack(pady=10)

    tk.Label(ventana, text=f"Ejemplo: Diccionario = {ejemplo_dicc}\nBuscando la llave '{objetivo}'", font=("Arial", 12)).pack(pady=10)

    resultado = busqueda_hash(ejemplo_dicc, objetivo)
    texto = f"Valor encontrado: {resultado}" if resultado else "Clave no encontrada"

    tk.Label(ventana, text="Resultado: " + texto, font=("Arial", 14, "bold")).pack(pady=10)



# ------------------- MENÚ PRINCIPAL -------------------

def menu_principal():
    root = tk.Tk()
    root.title("Métodos de Búsqueda")
    root.geometry("500x400")

    tk.Label(root, text="MÉTODOS DE BÚSQUEDA", font=("Arial", 18, "bold")).pack(pady=20)

    btn1 = ttk.Button(root, text="1. Búsqueda Secuencial", width=30, command=ventana_secuencial)
    btn2 = ttk.Button(root, text="2. Búsqueda Binaria", width=30, command=ventana_binaria)
    btn3 = ttk.Button(root, text="3. Búsqueda Hash", width=30, command=ventana_hash)

    btn1.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    menu_principal()
