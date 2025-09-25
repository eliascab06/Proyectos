temperaturas = []

print("Ingrese la temperatura semanal(7 días):")
for i in range(7):
    temp = float(input(f"Día {i+1}:"))
    temperaturas.append(temp)

promedio = sum(temperaturas)/len(temperaturas)

temp_max = max(temperaturas)
temp_min = min(temperaturas)

dias_prom = sum(1 for t in temperaturas if t > promedio)

print("Los resultados son:")
print(f"La Temperatura Promedio es: {promedio:.2f}°C")
print(f"La Temperatura Máxima es: {temp_max:.2f}°C")
print(f"La Temperatura Mínima es: {temp_min:.2f}°C")
print(f"Los Días con más temperatura son: {dias_prom}")