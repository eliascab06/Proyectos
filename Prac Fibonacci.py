def fibonacci(n):
    serie = [0, 1]  # primeros dos términos
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])  # suma los dos últimos
    return serie[:n]  # devuelve solo n términos

# Pedir al usuario cuántos términos quiere
n = int(input("¿Cuántos términos de Fibonacci quieres ver?: "))

print(f"Serie de Fibonacci con {n} términos:")
print(fibonacci(n))
