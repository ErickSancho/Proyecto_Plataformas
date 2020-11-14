import os
import csv
from datetime import date
import pandas as pd

class Personal:

    Usuarioactual = ""
    path="./config/Persona/"

    def ActualUser(self, user):
        self.Usuarioactual = str(user)

    def setupPersona(self):
        check = os.path.isdir('./config')
        if (check == False):
            os.mkdir('config')
            os.mkdir('config/Persona')

    def createUser(self, user, password):
        
        usr = str (user)
        pswrd = str (password)
        with open(os.path.join('./config/userData.csv'), "w") as f:
                writer = csv.writer(f)
                writer.writerow([usr,pswrd])
    
    def loginUser(self, textUser, textPassword):
        usr = str(textUser)
        pswrd = str(textPassword)
        user = pd.read_csv('./config/userData.csv',header=None)

        numerocuentas = len(user)
        print(user)
        Flag = False
        for i in range(0,numerocuentas-1):
            if str(user[i][0]) == usr and str(user[i][1]) == pswrd:
                Flag = True

        return Flag



    def crearCuenta(self,text):
        cuenta = str(text)
        path = self.path + self.Usuarioactual + cuenta
        os.mkdir(path)

        csvPath = path + '/'
        with open(os.path.join(csvPath, 'registro.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha','Concepto'])

        with open(os.path.join(csvPath, 'balance.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha',])


    def ingresos (self, cuentaIncome, montoIncome, conceptoIngreso):
        concepto = str(conceptoIngreso)
        fecha = date.today().strftime("%d/%m/%Y")
        monto = float (montoIncome)
        path = self.path + self.Usuarioactual + cuentaIncome + '/'
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([monto,fecha,concepto])


    def gastos(self, cuentaGasto, montoGasto, conceptoGasto):
        gasto = float(montoGasto)*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        path = self.path + self.Usuarioactual + cuentaGasto + '/'
        concepto = str(conceptoGasto)
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,concepto])


    def balance(self, cuentaBalance):
        registro = self.path + self.Usuarioactual + cuentaBalance + '/registro.csv'
        data = pd.read_csv(registro)
        
        total = data['Monto'].sum()
        print(total)
        fecha = date.today().strftime("%d/%m/%Y")
        with open(os.path.join(registro, 'balance.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([total,fecha])
