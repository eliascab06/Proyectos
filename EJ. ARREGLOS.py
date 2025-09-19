meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

ventas = [[0 for _ in departamentos] for _ in meses]

def insertar_venta(mes, depto, valor):
    ventas[mes][depto] = valor

def buscar_venta(mes, depto):
    return ventas[mes][depto]

def eliminar_venta(mes, depto):
    ventas[mes][depto] = 0

def mostrar_ventas():
    print("\nTabla de Ventas:")
    print(f"{'Mes':12}{'Ropa':12}{'Deportes':12}{'Juguetería':12}")
    for i in range(len(meses)):
        print(f"{meses[i]:12}", end="")
        for j in range(len(departamentos)):
            print(f"{ventas[i][j]:12}", end="")
        print()

# --- Captura de ventas por teclado ---
for i in range(len(meses)):
    print(f"\n--- Ingresar ventas para {meses[i]} ---")
    for j in range(len(departamentos)):
        valor = int(input(f"Ingrese ventas en {departamentos[j]}: "))
        insertar_venta(i, j, valor)

mostrar_ventas()

# Ejemplo de búsqueda
print("\nEjemplo -> Buscar ventas de Julio en Deportes:")
print("Ventas encontradas:", buscar_venta(6, 1))  

# Ejemplo de eliminación
print("\nEliminando ventas de Enero en Ropa...")
eliminar_venta(0, 0)
mostrar_ventas()
