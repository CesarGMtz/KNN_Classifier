# Importar librerías necesarias
import csv

# Definir una clase para los datos
class Patient:
    def __init__(self, preg, plas, pres, skin, insu, mass, pedi, age, classi):
        self.preg = preg
        self.plas = plas
        self.pres = pres
        self.skin = skin
        self.insu = insu
        self.mass = mass
        self.pedi = pedi
        self.age = age
        self.classi = classi

# Definir array de objetos de clase
patients = []

with open("Datos\Diabetes-Entrenamiento.csv", newline='') as dE:
    spamreader = csv.reader(dE, delimiter=',')
    next(spamreader)
    for row in spamreader:
        tempObj = Patient(*row)
        patients.append(tempObj)
        
# Acceso a datos
print(patients[0].preg)
