import os
import csv
from datetime import date
import pandas as pd

class Presonal:

    def setupPersona(self):
        check = os.path.isdir('config')
        if (check == False):
            os.mkdir('config')        

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



    def ingresos (self, path):
        ingreso = float(input("Digite el monto de su ingresos en colones: "))
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del ingreso:\n")
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([ingreso,fecha,nota])


    def gastos(self, path):
        gasto = float(input("Digite el monto de su gasto en colones: "))*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del gasto:\n")
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,nota])


    def balance(self, path):
        registro = path + 'registro.csv'
        data = pd.read_csv(registro)
        
        total = data['Monto'].sum()
        print(total)
        fecha = date.today().strftime("%d/%m/%Y")
        print (fecha)
        print("\n")
        with open(os.path.join(path, 'balance.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([total,fecha])

        prueabPath = path + 'balance.csv'
        prueba = pd.read_csv(prueabPath)
        print (prueba)



    def menu(self):
        
        run = 1

        print("Se ha creado el directorio config, el cual tiene los datos de las cuentas.")
        setupPersona()
        
        while(run == 1):
            define = input("Indique lo que se desea hacer (crear, ingresos, gastos, balance o salir): \n")

            if (define=="ingresos"):
                path = './config/' + input("Indique el nombre de la cuenta a la que desea realizar el cambio: \n")    
                ingresos(path)
            elif (define=="gastos"):
                path = './config/' + input("Indique el nombre de la cuenta a la que desea realizar el cambio: \n") 
                gastos(path)
            elif (define == "balance"):
                path = './config/' + input("Indique el nombre de la cuenta de la cual desea conocer el balance: \n") +'/'
                balance(path)
            elif (define == "crear"):
                crearCuenta()
            elif (define ==  "salir"):
                run = 0
            else:
                print("No indicó una accion válida. Por favor verifique e intente de nuevo.")
    