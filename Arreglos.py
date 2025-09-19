import numpy as np

# Creamos la matriz de 500 alumnos x 6 materias
alumnos = np.zeros((500, 6), dtype=int)

# Ejemplo: asignamos un valor en alumno 321, materia 5
alumnos[320, 4] = 85

# Mostrar toda la tabla
print("Tabla completa de alumnos y materias:")
print(alumnos)

# Mostrar solo los primeros 10 alumnos (para que no sea tan largo en consola)
print("\nPrimeros 10 alumnos con sus materias:")
print(alumnos[:10])

# Mostrar alumno 321 (toda su fila)
print(f"\nCalificaciones del alumno 321: {alumnos[320]}")

# Mostrar alumno 321 en materia 5
print(f"\nMateria 5 del alumno 321: {alumnos[320, 4]}")
