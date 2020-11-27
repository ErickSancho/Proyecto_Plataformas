import os
import csv
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import crypt

class Empresa:
    
    #definición de variables requeridas
    Usuarioactual = ""
    path = "./config/Empresa/"
    
    def ActualUser (self, user):
        self.Usuarioactual = str (user)
    
    def setupEmpresa(self):
        checkConfig = os.path.isdir('./config')
        checkEmpresa = os.path.isdir ('./config/Empresa')
        if (checkConfig == False):
            os.mkdir('config')
        if (checkEmpresa == False):
            os.mkdir('./config/Empresa')

    def createUser(self, user, password):
        usr = str (user)
        pswrd = crypt.crypt(str (password), 'salt')
        checkFolder = os.path.isdir('./config/Empresa/' + usr)
        checkFile = os.path.isfile('./config/Empresa/userData.csv')
        self.ActualUser(usr)
        if checkFolder == False and checkFile == True:
            os.mkdir('./config/Empresa/' + usr)
            with open(os.path.join('./config/Empresa/userData.csv'), "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([usr,pswrd])

        elif checkFile == False and checkFolder == False:
            os.mkdir('./config/Empresa/' + usr)
            with open(os.path.join('./config/Empresa/userData.csv'), "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(["User","Password"])
                    writer.writerow([usr,pswrd])

        elif checkFolder == True:
            return -1

        path = './config/Empresa/' + usr + '/'
            
        cuentaLista = os.path.isfile(path + 'cuentas.csv')
        if (cuentaLista == False):
            with open(os.path.join(path, 'cuentas.csv'), "w") as f:
                writer = csv.writer(f)
                writer.writerow(['Cuenta'])

    
    def loginUser(self, textUser, textPassword):
        usr = str(textUser)
        pswrd = crypt.crypt(str (textPassword), 'salt')
        user = pd.read_csv('./config/Empresa/userData.csv')

        numerocuentas = len(user)
        Flag = False
        for i in range(0,numerocuentas):
            if str(user["User"][i]) == usr and str(user["Password"][i]) == pswrd:
                Flag = True
                self.ActualUser(usr)

        return Flag
    
    def crearCuentaEmpresa(self, TexInput):
        cuenta = str(TexInput)
        path = self.path + self.Usuarioactual + '/' + cuenta
        os.mkdir(path)
        pathLista = self.path + self.Usuarioactual + '/'
        csvPath = path + '/'
        
        with open(os.path.join(csvPath, 'registro.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha','Concepto'])

        with open(os.path.join(csvPath, 'balance.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha',])
        
        with open(os.path.join(pathLista, 'cuentas.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([cuenta])

    def ingresosEmpresa(self, textCuenta, textMonto, textConcepto): 
        cuenta = str(textCuenta)
        path = self.path + self.Usuarioactual + '/' + cuenta + '/'
        ingreso = float(textMonto)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = str(textConcepto)

        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([ingreso,fecha,nota])

    def gastosEmpresa(self, textCuenta, textMonto, textConcepto):
        cuenta = str(textCuenta)
        path = self.path + self.Usuarioactual + '/' + cuenta + '/'
        gasto = float(textMonto)*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = str(textConcepto)
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,nota])

    def balanceEmpresa(self, textCuenta):
        cuenta = str(textCuenta)
        path = self.path + self.Usuarioactual + '/' + cuenta + '/'
        registro = path + 'registro.csv'
        data = pd.read_csv(registro)
        
        total = data['Monto'].sum()
        
        fecha = date.today().strftime("%d/%m/%Y")
        
        with open(os.path.join(path, 'balance.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([total,fecha])

    def taxesEmpresa(self, textEstado):
        estadoEntidadJuridica = str(textEstado)
        valorNeto = 0
        folders = 0
        impuestoSobreEntJur = 0
        impuestoSobreRenta = 0


        pathLista = self.path + self.Usuarioactual + '/'
        with open(os.path.join(pathLista,'cuentas.csv')) as csvfile:
            folderList = list(csv.reader(csvfile))

        for _, dirnames, _ in os.walk(pathLista):
            folders += len(dirnames)
        
        i=1
        while (i<=folders):
            path = self.path + self.Usuarioactual + '/' + folderList[i][0] +'/'
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
        
        pathAppend = self.path + self.Usuarioactual + '/'
        with open(os.path.join(pathAppend, 'impuesto.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Impuesto'])
            writer.writerow([impuestoSobreEntJur,'Impuesto sobre entidades jurídicas'])
            writer.writerow([impuestoSobreRenta,'Impuesto sobre la renta'])

    def PlotFigures (self,cuentaPlot):
        cuenta = str(cuentaPlot) + '/'
        balancePath = self.path + self.Usuarioactual + '/' + cuenta + '/balance.csv' 
        #registroPath = self.path + self.Usuarioactual + 'registro.csv' 

        balance = pd.read_csv(balancePath)
        #registro = pd.read_csv(registroPath)

        plt.figure(figsize=(8,5))
        plt.plot(balance.Fecha,balance.Monto)
        plt.title('Balance de la cuenta')
        plt.ylabel('Monto')
        plt.xlabel('Fecha')
        plt.grid()
        plt.show()