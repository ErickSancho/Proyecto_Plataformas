import os
import csv
from datetime import date
import pandas as pd

def setup():
    check = os.path.isdir('config')
    if (check == False):
        os.mkdir('config')

def ingresos (path):
    ingreso = float(input("Digite el monto de su ingresos en colones: "))
    fecha = date.today().strftime("%d/%m/%Y")
    nota = input("Indique el concepto del ingreso:\n")
    
    with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([ingreso,fecha,nota])

def gastos(path):
    gasto = float(input("Digite el monto de su gasto en colones: "))*(-1)
    fecha = date.today().strftime("%d/%m/%Y")
    nota = input("Indique el concepto del gasto:\n")
    
    with open(os.path.join(path, 'registro.csv'), "a") as f:
        writer = csv.writer(f)
        writer.writerow([gasto,fecha,nota])

def balance(path):
    read = 5




class Person:
    def __init__ (self,name):
        self.n=name

    def crearCuenta(self):
        cuenta = input("Digite el nombre de la cuenta a crear (recuerde que este debe ser ilustrativo para saber a qué hace alusión: \n")
        path = './config/'+ cuenta
        os.mkdir(path)

        csvPath = path + '/'
        with open(os.path.join(csvPath, 'registro.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha','Concepto'])

        with open(os.path.join(csvPath, 'balance.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha',])
    
    
    def definirAction(self):
        define = input("Indique la cuenta a la que se realizan los cambios: \n")
        path = './config/'+ define
        check = os.path.isdir(path)
        
        if(check == True):
            action = input("Indique si va a realizar un ingreso un gasto: \n")
            if (action=="ingreso"):
                ingresos(path)
            elif (action=="gasto"):
                gastos(path)
        else:
            print("No ingresó un nombre válido.")

            

 
        
   

    