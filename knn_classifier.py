# Importar librerías necesarias
import csv
import math

# Definir una clase para los datos
class Patient:
    def __init__(self, preg, plas, pres, skin, insu, mass, pedi, age, classi):
        self.preg = int(preg)
        self.plas = int(plas)
        self.pres = int(pres)
        self.skin = int(skin)
        self.insu = int(insu)
        self.mass = float(mass)
        self.pedi = float(pedi)
        self.age = int(age)
        self.classi = classi

# Definir array de objetos de clase
patientsE = []
patientsC = []

# Almacenar datos de entrenamiento
with open("Datos\Diabetes-Entrenamiento.csv", newline='') as dE:
    spamreader = csv.reader(dE, delimiter=',')
    next(spamreader)
    for row in spamreader:
        tempObj = Patient(*row)
        patientsE.append(tempObj)
        
# Almacenar datos para su clasificación
with open("Datos\Diabetes-Clasificacion.csv", newline='') as dC:
    spamreader = csv.reader(dC, delimiter=',')
    next(spamreader)
    for row in spamreader:
        tempObj = Patient(*row)
        patientsC.append(tempObj)

k = int(input("Ingresa K: "))
distancias = []

for patientC in patientsC:
    for patientE in patientsE:
        distancia = math.sqrt(
            (patientC.preg - patientE.preg)**2 +
            (patientC.plas - patientE.plas)**2 +
            (patientC.pres - patientE.pres)**2 +
            (patientC.skin - patientE.skin)**2 +
            (patientC.insu - patientE.insu)**2 +
            (patientC.mass - patientE.mass)**2 +
            (patientC.pedi - patientE.pedi)**2 +
            (patientC.age - patientE.age)**2
        )

        if len(distancias) < k:
            distancias.append(distancia)
            
        else:
            distancias.sort()
            if distancia < distancias[-1]:
                distancias.pop(-1)
                distancias.append(distancia)

    print(distancias)
    
# # Acceso a datos
# print(patientsE)
# print(patientsC)
