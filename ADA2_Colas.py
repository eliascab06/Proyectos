class Cola:
    def __init__(self, limite=5):
        self.items = []
        self.limite = limite

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.limite

    def encolar(self, dato):
        if not self.esta_llena():
            self.items.append(dato)
        else:
            print("⚠️ La cola está llena. No se puede agregar más elementos.")

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("⚠️ La cola está vacía.")
            return None

    def ver_cola(self):
        return self.items


def es_entero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def combinar_colas(cola1, cola2):
    cola_resultado = Cola(limite=min(cola1.limite, cola2.limite))

    for i in range(min(len(cola1.items), len(cola2.items))):
        a = cola1.items[i]
        b = cola2.items[i]

        if es_entero(a) and es_entero(b):
            suma = float(a) + float(b)
            cola_resultado.encolar(suma)
        else:
            cola_resultado.encolar(str(a) + str(b))

    return cola_resultado


print("=== PROGRAMA DE COMBINACIÓN DE COLAS ===\n")

colaA = Cola()
colaB = Cola()

print("Ingresa los elementos de la Cola A (números o caracteres):")
for i in range(colaA.limite):
    valor = input(f"Elemento {i+1}: ")
    colaA.encolar(valor)

print("\nIngresa los elementos de la Cola B (números o caracteres):")
for i in range(colaB.limite):
    valor = input(f"Elemento {i+1}: ")
    colaB.encolar(valor)

resultado = combinar_colas(colaA, colaB)

print("\n=== RESULTADO ===")
print("Cola A:        ", colaA.ver_cola())
print("Cola B:        ", colaB.ver_cola())
print("Cola Resultado:", resultado.ver_cola())
