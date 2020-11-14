import os
import csv
from datetime import date
import pandas as pd
#definir el login y setup de la empresa (creo que pueden ser iguales)
class Empresa:
    #la función de setup se puede correr después de que se cree el usuario, no lleva ningún parámetro
    def setupEmpresa(self):
        check = os.path.isdir('config')
        if (check == False):
            os.mkdir('config')

        impuestos = os.path.isfile('./config/impuestos.csv')
        if (impuestos == False):
            with open(os.path.join('./config/', 'impuestos.csv'), "w") as f:
                writer = csv.writer(f)
                writer.writerow(['Monto','Impuesto'])
            
        cuentaLista = os.path.isfile('./config/cuentas.csv')
        if (cuentaLista == False):
            with open(os.path.join('./config/', 'cuentas.csv'), "w") as f:
                writer = csv.writer(f)
                writer.writerow(['Cuenta'])

    def crearCuentaEmpresa(self, TexInput):
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
        
        with open(os.path.join('./config', 'cuentas.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([cuenta])

    def ingresosEmpresa(self, textCuenta, textMonto, textConcepto): #redefinir path en todas  las funciones
        path = './config/' + input("Indique el nombre de la cuenta a la que desea realizar el cambio: \n")
        ingreso = float(input("Digite el monto de su ingresos en colones: "))
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del ingreso:\n")

        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([ingreso,fecha,nota])

    def gastosEmpresa(self):
        path = './config/' + input("Indique el nombre de la cuenta a la que desea realizar el cambio: \n")
        gasto = float(input("Digite el monto de su gasto en colones: "))*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del gasto:\n")
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,nota])

    def balanceEmpresa(self):
        path = './config/' + input("Indique el nombre de la cuenta de la cual desea conocer el balance: \n") +'/'
        registro = path + 'registro.csv'
        data = pd.read_csv(registro)
        
        total = data['Monto'].sum()
        
        fecha = date.today().strftime("%d/%m/%Y")
        
        with open(os.path.join(path, 'balance.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([total,fecha])

        prueabPath = path + 'balance.csv'
        prueba = pd.read_csv(prueabPath)
        print (prueba)

    def impuestosEmpresa(self):
        estadoEntidadJuridica = input("Indique si su empresa se encuentra en trámite de inscripción ante Registro de personas jurídicas (s/n): ")
        valorNeto = 0
        folders = 0
        impuestoSobreEntJur = 0
        impuestoSobreRenta = 0

        with open(os.path.join('./config','cuentas.csv')) as csvfile:
            folderList = list(csv.reader(csvfile))

        for _, dirnames, _ in os.walk('./config/'):
            folders += len(dirnames)
        
        i=1
        while (i<=folders):
            path = './config/' + folderList[i][0] +'/'
            with open(os.path.join(path,'balance.csv')) as csvfile:
                num = list(csv.reader(csvfile))
            position = len(num)-1
            valorNeto = valorNeto + float(num[position][0])

            i= i + 1
        
        
        if (estadoEntidadJuridica == 's'):
            impuestoSobreEntJur = valorNeto*0.15
        else:
            impuestoSobreEntJur = valorNeto*0.25
        
        if (valorNeto<5143000):
            impuestoSobreRenta = valorNeto*0.5
        elif (5143000<=valorNeto<7715000):
            impuestoSobreRenta = valorNeto*0.10
        elif (7715000<=valorNeto,10286000):
            impuestoSobreRenta = valorNeto*0.15
        else:
            impuestoSobreRenta = valorNeto*0.20
        
        with open(os.path.join('./config/', 'impuesto.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Impuesto'])
            writer.writerow([impuestoSobreEntJur,'Impuesto sobre entidades jurídicas'])
            writer.writerow([impuestoSobreRenta,'Impuesto sobre la renta'])

        imp = pd.read_csv('./config/impuesto.csv')
        print (imp)


    