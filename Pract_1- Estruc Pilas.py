class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = []
    
    def push(self, elemento):
        if len(self.elementos) >= self.capacidad:
            print(f"Error: Desbordamiento (la pila está llena). No se puede insertar {elemento}.")
        else:
            self.elementos.append(elemento)
            print(f"Insertado {elemento} → PILA: {self.elementos}")
    
    def pop(self, etiqueta):
        if len(self.elementos) == 0:
            print(f"Error: Subdesbordamiento al intentar eliminar ({etiqueta}). La pila está vacía.")
        else:
            eliminado = self.elementos.pop()
            print(f"Eliminado {eliminado} (operación {etiqueta}) → PILA: {self.elementos}")
    
    def mostrar_estado(self):
        print(f"\nPILA FINAL: {self.elementos}")
        print(f"TOPE = {len(self.elementos)}")

# Simulación 
pila = Pila(8)

# Operaciones
pila.push("X")
pila.push("Y")
pila.pop("Z")
pila.pop("T")
pila.pop("U")  # Error
pila.push("V")
pila.push("W")
pila.pop("p")
pila.push("R")


pila.mostrar_estado()
