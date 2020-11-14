import os
import csv
from datetime import date
import pandas as pd

class Personal:

    def setupPersona(self):
        check = os.path.isdir('config')
        if (check == False):
            os.mkdir('config')

    def createUser(self, user, password):
      usr = str (user)
      pswrd = str (password)
      with open(os.path.join('./config/','userData.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow([usr,pswrd])
    
    def loginUser(self, textUser, textPassword):
      user = pd.read_csv('./config/userData.csv')
      if user[0][0] == textUser and user[0][1] == textPassword:
        return True
      else:
        return False


    def crearCuenta(self,text):
        cuenta = str(text)
        path = './config/'+ cuenta
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
        path = './config/' + cuentaIncome + '/'
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([monto,fecha,concepto])


    def gastos(self, cuentaGasto, montoGasto, conceptoGasto):
        gasto = float(montoGasto)*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        path = './config/' + cuentaGasto + '/'
        concepto = str(conceptoGasto)
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,concepto])


    def balance(self, cuentaBalance):
        registro = './config/' + cuentaBalance + '/registro.csv'
        data = pd.read_csv(registro)
        
        total = data['Monto'].sum()
        print(total)
        fecha = date.today().strftime("%d/%m/%Y")
        with open(os.path.join(registro, 'balance.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([total,fecha])
