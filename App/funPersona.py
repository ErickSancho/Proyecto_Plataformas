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
        cuenta = text
        path = './config/'+ cuenta
        os.mkdir(path)

        csvPath = path + '/'
        with open(os.path.join(csvPath, 'registro.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha','Concepto'])

        with open(os.path.join(csvPath, 'balance.csv'), "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Monto','Fecha',])



    def ingresos (self, cuentaIncome):
        ingreso = str(TextIncome)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del ingreso:\n")
        path = './config/' + cuentaIncome + '/'
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
                writer = csv.writer(f)
                writer.writerow([ingreso,fecha,nota])


    def gastos(self, cuentaGasto):
        gasto = float(input("Digite el monto de su gasto en colones: "))*(-1)
        fecha = date.today().strftime("%d/%m/%Y")
        nota = input("Indique el concepto del gasto:\n")
        path = './config/' + cuentaGasto + '/'
        
        with open(os.path.join(path, 'registro.csv'), "a") as f:
            writer = csv.writer(f)
            writer.writerow([gasto,fecha,nota])


    def balance(self, cuentaBalance):
        registro = './config/' + cuentaBalance + '/registro.csv'
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
    