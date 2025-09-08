def main():
    calificaciones = [0] * 5  # lista de 5 elementos inicializados en 0
    for i in range(5):
        calificaciones[i] = int(input("Captura la calificación: "))

    print("Calificaciones capturadas:", calificaciones)