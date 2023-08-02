#importamos las librerías necesarias
import math
import pandas as pd

# Función para calcular el promedio de notas
def cal_prom(notas):
    return sum(notas) / len(notas)

# Función para calcular la varianza de notas
def cal_var(notas):
    prom = cal_prom(notas)
    var = sum([(x - prom) ** 2 for x in notas]) / len(notas)
    return math.sqrt(var)

# Crear un diccionario vacío para almacenar los estudiantes y sus notas
dicc_notas = {}

# Solicitar al usuario ingresar el numero de estudiantes y el numero de notas que deberia tener cada estudiante.

num_estudiantes = int(input("Ingrese el número de estudiantes: "))
num_notas = int(input("Ingrese el número de notas que presentan los estudiantes: "))

for i in range(num_estudiantes):
    estudiante = input(f"Ingrese el nombre del estudiante {i+1}: ")
    notas = []
    for n in range(num_notas):
        nota = float(input(f"Ingrese la nota {n+1} de {estudiante}: "))
        notas.append(nota)
    dicc_notas[estudiante] = notas

# Crear un diccionario que estara compuesto por las listas resultantes de las siguentes operaciones.

resultados = {
    "Estudiante": [],
    "Promedio": [],
    "Varianza": []
}

# Calcular las estadísticas para cada estudiante y agregar los resultados al diccionario
for estudiante, notas in dicc_notas.items():
    promedio = cal_prom(notas)
    varianza = cal_var(notas)
    resultados["Estudiante"].append(estudiante)
    resultados["Promedio"].append(promedio)
    resultados["Varianza"].append(varianza)

# mostrar los resultados a traves de un DataFrame
df = pd.DataFrame(resultados)
print(df)