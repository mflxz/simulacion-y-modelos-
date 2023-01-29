# María López CI: 27.182.207
# Simulación y modelos 
from collections import Counter
from random import random
import matplotlib.pyplot as plt
# Crea una lista vacía para almacenar los valores
datos = []

# Abre el archivo en modo lectura
with open('archivo.csv', 'r') as file:
    # Recorre cada línea del archivo
    for line in file:
        # Elimina los caracteres de nueva línea y espacio en blanco
        line = line.strip()
        # Agrega el valor a la lista
        datos.append(float(line))

# Calcula la frecuencia de cada elemento en la lista
frecuencia = Counter(datos)

# Calcula la frecuencia acumulada
frecuencia_acumulada = {}
total = sum(frecuencia.values())
acumulado = 0
for key, valor in frecuencia.items():
    acumulado += valor
    frecuencia_acumulada[key] = acumulado / total

# Crea un diccionario vacío para almacenar los contadores
contadores = {}

# Itera 100 veces
for i in range(100):
    r = random()
    for key, value in frecuencia_acumulada.items():
        if r <= value:
            # Aumenta el contador para ese valor
            if key in contadores:
                contadores[key] += 1
            else:
                contadores[key] = 1
            break

# Calcula el porcentaje de que "r" caiga en cada frecuencia acumulada
porcentajes = {}
for key, value in contadores.items():
    porcentajes[key] = (value / 100) * 100

# Imprime los datos del archivo
print('-----------------------------------------------------------')
print('Datos')
print(datos)
# Imprime la frecuencia que se repiten los numeros
print('-----------------------------------------------------------')
print('Cantidad de repeticiones:')
print(dict (frecuencia))
# Imprime los porcentajes
print('-----------------------------------------------------------')
print('Porcentaje')
print(porcentajes)
# Imprime la frecuencia acumulada
print('-----------------------------------------------------------')
print('Frecuencia Acumulada')
print(frecuencia_acumulada )

# Crea un gráfico de barras
plt.bar(porcentajes.keys(), porcentajes.values())

# Agrega títulos al gráfico
plt.title("Simulación de datos")
plt.xlabel("Frecuencia acumulada")
plt.ylabel("Porcentaje")

# Muestra el gráfico
plt.show()
