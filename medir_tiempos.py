import matplotlib.pyplot as plt
import random
import time
import csv

# Leer los primeros 1000 datos del archivo
def leer_datos(path):
    datos = []
    with open(path, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
             if fila and fila[0].strip().isdigit():  # ✅ Solo si es número válido
                datos.append(int(fila[0]))
    return datos

# Función para medir el tiempo promedio de búsqueda
def medir_tiempos(datos, rango_t):
    tiempos = []

    for t in rango_t:
        # Simular "inserción ordenada" en B-Tree
        estructura_simulada = sorted(datos[:t * 2])  # tamaño proporcional a t

        # Escoger 10 elementos aleatorios a buscar
        elementos_a_buscar = random.sample(datos[:t * 2], 10)

        tiempos_busqueda = []

        for elemento in elementos_a_buscar:
            inicio = time.perf_counter()
            encontrado = elemento in estructura_simulada
            fin = time.perf_counter()
            tiempos_busqueda.append((fin - inicio) * 1000)  # en milisegundos

        tiempo_promedio = sum(tiempos_busqueda) / len(tiempos_busqueda)
        tiempos.append(tiempo_promedio)

        print(f"t = {t}, tiempo promedio = {tiempo_promedio:.5f} ms")

    return tiempos

# Función para graficar
def graficar_tiempos(valores_t, tiempos_promedio):
    plt.figure(figsize=(10, 6))
    plt.plot(valores_t, tiempos_promedio, marker='o', linestyle='-', color='green')
    plt.title('Tiempo promedio de búsqueda vs. t')
    plt.xlabel('Grado mínimo t')
    plt.ylabel('Tiempo promedio de búsqueda (ms)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ----------------------------- MAIN -----------------------------
ruta_archivo = "random_numbers_1000000.csv"
datos = leer_datos(ruta_archivo)

valores_t = list(range(10, 1001, 10))  # de 10 a 1000 de 10 en 10
tiempos = medir_tiempos(datos, valores_t)

graficar_tiempos(valores_t, tiempos)
