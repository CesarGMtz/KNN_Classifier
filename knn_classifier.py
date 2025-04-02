# Importar librerías necesarias
import csv

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
    
# Acceso a datos
print(patientsE[0].preg)
print(patientsC[0].preg)
