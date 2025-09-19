import numpy as np
import time

def prueba_forma_alumnos(num_alumnos, num_materias):
    # Forma A: filas = alumnos, columnas = materias
    matriz = np.random.randint(0, 100, size=(num_alumnos, num_materias))
    
    inicio = time.time()
    total = 0
    # Recorremos todos los alumnos y materias
    for i in range(num_alumnos):
        for j in range(num_materias):
            total += matriz[i, j]
    fin = time.time()
    
    return fin - inicio, total

def prueba_forma_materias(num_alumnos, num_materias):
    # Forma B: filas = materias, columnas = alumnos
    matriz = np.random.randint(0, 100, size=(num_materias, num_alumnos))
    
    inicio = time.time()
    total = 0
    # Recorremos todas las materias y alumnos
    for j in range(num_materias):
        for i in range(num_alumnos):
            total += matriz[j, i]
    fin = time.time()
    
    return fin - inicio, total

# --- PRUEBA ---
for alumnos, materias in [(1000, 100), (10000, 500), (100000, 10000)]:
    print(f"\n📊 Prueba con {alumnos} alumnos y {materias} materias:")
    
    t1, _ = prueba_forma_alumnos(alumnos, materias)
    print(f" Forma A (alumnos x materias): {t1:.4f} segundos")
    
    t2, _ = prueba_forma_materias(alumnos, materias)
    print(f" Forma B (materias x alumnos): {t2:.4f} segundos")

#Conclusión
#En conclusión la seria A o t1 en este caso es el más rapido, ya que 
#recorre la memoria continuamente, a diferencia del B o t2, que tarda 
#un poco más porque el tamaño es mucho mayor, de hecho, da un aviso del tiempo de espera.