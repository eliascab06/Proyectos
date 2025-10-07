class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

    def mostrar(self):
        return list(self.items)


class SistemaSeguros:
    def __init__(self):
        self.colas = {}
        self.contadores = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Cola()
            self.contadores[servicio] = 1

        numero_atencion = self.contadores[servicio]
        self.colas[servicio].encolar(numero_atencion)
        self.contadores[servicio] += 1

        print(f"Cliente para servicio {servicio}: número {numero_atencion} asignado.")

    def atender_cliente(self, servicio):
        if servicio not in self.colas or self.colas[servicio].esta_vacia():
            print(f"No hay clientes en espera para el servicio {servicio}.")
        else:
            numero = self.colas[servicio].desencolar()
            print(f"Atendiendo al cliente número {numero} del servicio {servicio}.")

    def ver_cola(self, servicio):
        if servicio not in self.colas or self.colas[servicio].esta_vacia():
            print(f"No hay clientes en cola para el servicio {servicio}.")
        else:
            en_espera = self.colas[servicio].mostrar()
            print(f"Clientes en cola para servicio {servicio}: {en_espera}")
            print(f"Total en cola: {len(en_espera)}")


def main():
    sistema = SistemaSeguros()

    print("=== Sistema de Colas de Servicios ===")
    print("Comandos:")
    print("  C#  → Llega un cliente al servicio #")
    print("  A#  → Atender cliente del servicio #")
    print("  V#  → Ver clientes en cola del servicio #")
    print("  S   → Salir")
    print("-------------------------------------")

    while True:
        comando = input("Ingrese comando: ").strip().upper()

        if comando == "S":
            print("Saliendo del sistema...")
            break
        elif len(comando) < 2:
            print("Comando inválido. Ejemplo: C1, A2 o V3.")
            continue

        accion = comando[0]
        servicio = comando[1:]

        if not servicio.isdigit():
            print("Número de servicio inválido.")
            continue

        servicio = int(servicio)

        if accion == "C":
            sistema.llegada_cliente(servicio)
        elif accion == "A":
            sistema.atender_cliente(servicio)
        elif accion == "V":
            sistema.ver_cola(servicio)
        else:
            print("Comando desconocido. Use C, A, V o S.")


if __name__ == "__main__":
    main()
