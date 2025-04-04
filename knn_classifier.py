# Librerías necesarias para la ejecución del código
import csv
import math
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Clase para almacenar los datos
class Patient:
    def __init__(self, preg, plas, pres, skin, insu, mass, pedi, age, classi):
        self.preg = float(preg)
        self.plas = float(plas)
        self.pres = float(pres)
        self.skin = float(skin)
        self.insu = float(insu)
        self.mass = float(mass)
        self.pedi = float(pedi)
        self.age = float(age)
        self.classi = classi

# Función principal para la ejecución del KNN con o ssin datos normalizados
def ejecutar_knn(k, normalizar=False, archivo_salida="Resultados.csv"):
    patientsE = []
    patientsC = []

    # Lee y almacena datos de entrenamiento
    with open("Datos/Diabetes-Entrenamiento.csv", newline='') as dE:
        reader = csv.reader(dE, delimiter=',')
        next(reader)
        for row in reader:
            patientsE.append(Patient(*row))

    # Lee y almacena datos para su clasificación
    with open("Datos/Diabetes-Clasificacion.csv", newline='') as dC:
        reader = csv.reader(dC, delimiter=',')
        next(reader)
        for row in reader:
            patientsC.append(Patient(*row))

    # En caso de ser necesario, se normaliza usando MinMaxScaler
    if normalizar:
        scaler = MinMaxScaler()
        X_train = np.array([[p.preg, p.plas, p.pres, p.skin, p.insu, p.mass, p.pedi, p.age] for p in patientsE])
        X_test = np.array([[p.preg, p.plas, p.pres, p.skin, p.insu, p.mass, p.pedi, p.age] for p in patientsC])

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        for i, p in enumerate(patientsE):
            (p.preg, p.plas, p.pres, p.skin, p.insu, p.mass, p.pedi, p.age) = X_train_scaled[i]
        for i, p in enumerate(patientsC):
            (p.preg, p.plas, p.pres, p.skin, p.insu, p.mass, p.pedi, p.age) = X_test_scaled[i]

    # KNN
    distancias = []
    contadorInstancia = 1
    contadorPositivo = 0

    # Escribe los resultados en un archivo csv
    with open(f"Datos/{archivo_salida}", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Instancia", "tested_positive", "tested_negative", "Clase Asignada"])

        # Calcula la distancia euclidiana de cada paciente con los datos de entrenamiento
        for patientC in patientsC:
            distancias.clear()
            for patientE in patientsE:
                distancia = math.sqrt(
                    (patientC.preg - patientE.preg) ** 2 +
                    (patientC.plas - patientE.plas) ** 2 +
                    (patientC.pres - patientE.pres) ** 2 +
                    (patientC.skin - patientE.skin) ** 2 +
                    (patientC.insu - patientE.insu) ** 2 +
                    (patientC.mass - patientE.mass) ** 2 +
                    (patientC.pedi - patientE.pedi) ** 2 +
                    (patientC.age - patientE.age) ** 2
                )
                distancias.append((distancia, patientE.classi))

            # Ordena los datos de menor a mayor
            distancias.sort()
            vecinos = distancias[:k]
            sumaN = sum(1 for (_, clase) in vecinos if clase == "tested_negative")
            sumaP = k - sumaN
            diagnostico = "tested_positive" if sumaP > sumaN else "tested_negative"

            if diagnostico == patientC.classi:
                contadorPositivo += 1

            writer.writerow([contadorInstancia, sumaP, sumaN, diagnostico])
            contadorInstancia += 1

    # Calcula el porcentaje de aciertos
    porcentaje = contadorPositivo / len(patientsC) * 100
    tipo = "Con Normalizacion" if normalizar else "Sin Normalizacion"
    print(f"{tipo} con k = {k} | El {porcentaje:.2f}% de los casos fueron asignados correctamente.")

print("Introduce un valor de k, preferiblemente un valor impar, si deseas ejecutar un escenario predefinido, con valores de 1, 5 y 9 en k, introduce 0")
k_input = int(input())

# Ejecutar con k = 1, 5 y 10 para ambos casos
print("\n Ejecucion Sin Normalizacion ")
if k_input != 0:
    ejecutar_knn(k_input, normalizar=False, archivo_salida="Resultados.csv")
else:
    for k in [1, 5, 9]:
        ejecutar_knn(k, normalizar=False, archivo_salida="Resultados.csv")

print("\n Ejecucion Con Normalizacion")
if k_input != 0:
    ejecutar_knn(k_input, normalizar=True, archivo_salida="ResultadosNormalizados.csv")
else:
    for k in [1, 5, 9]:
        ejecutar_knn(k, normalizar=True, archivo_salida="ResultadosNormalizados.csv")
