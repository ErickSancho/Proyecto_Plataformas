#coding = utf-8

# Librerias de la interrfaz grafica
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from kivy.uix.floatlayout import FloatLayout

# funciones para calculos 
import funPersona
import funEmpresa
import Funcs

######################## Definicion de clases ############################

# Clase para la pantalla principal en la cual se elige el tipo de uso que se 
# desea dar al sistema Personal o Empresa
class Menu(Screen):
    
    texto = ObjectProperty(None)
    
    def EntraPersona(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ingresar a Persona?',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        content.bind(on_press=ir_login_persona)
        pop.open()

    def EntraEmpresa(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ingresar a Empresa?',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        content.bind(on_press=ir_login_empresa)
        
        pop.open()
        


# content=Label(text='Invalid username or password.'),
#########################  Defino las clases para la parte personal  ########################

# Clase para la pantalla de ingreso a sistema personal.
class LoginPersona(Screen):
    #Aquí van los login de la persona
    nameUser = ObjectProperty(None)
    namePassword = ObjectProperty(None) 

    login = False
    i = 0
    def check_userpassword(self):        
        self.login = persona.loginUser(self.nameUser.text, self.namePassword.text)
        if self.login == False:
            self.i = self.i+1
            self.Fallo_UC()
        # Verifico si se acabaron los intentos.
        if self.i >= 5:
            self.i = 0
            sm.current = "menu"
        
    
    def Fallo_UC(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Usuario y/o contraseña incorrecto(s), intente de nuevo',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        
        self.nameUser.text = ""
        self.namePassword.text = ""

        pop.open()

# Pagina para crear usuario
class CreateUserPersona(Screen):
    nameAccount = ObjectProperty(None)
    namePassword = ObjectProperty (None)
    persona.createUser(nameAccount,namePassword)


#Pagina para crear cuentas:
class CreateAccountPersona (Screen):
    account = ObjectProperty(None)
    persona.crearCuenta(self.account)

# Pagina para registro de Ingresos

class MenuPersona (Screen):
  pass

class IngresosPersona(Screen):
    nameIngresos = ObjectProperty(None)
    montoIngresos = ObjectProperty(None)
    conceptoIngresos = ObjectProperty(None)
    persona.ingresos(self.nameIngresos.text,self.montoIngresos.text,self.conceptoIngresos.text)
  
# Pagina para Ingreso de Gastos
class GastosPersona(Screen):
    nameGastos = ObjectProperty(None)
    montoGastos = ObjectProperty(None)
    conceptoGastos = ObjectProperty (None)
    persona.gastos(self.nameGastos.text,self.montoGastos.text,self.conceptoGastos.text)
# Pagina para muestra de Balance
class BalancePersona(Screen):
    nameBalance = ObjectProperty(None)
    persona.balance(self.nameBalance.text)

######################### Defino las clases de pantallas para empresas #########################

# Clase para la pantalla de ingreso a sistema personal.
class LoginEmpresa(Screen):
        #Aquí van los login de la persona
    nameUser = ObjectProperty(None)
    namePassword = ObjectProperty(None) 

    login = False
    i = 0
    def check_userpassword(self):        
        self.login = empresa.loginUser(self.nameUser.text, self.namePassword.text)
        print(self.nameUser.text, self.namePassword.text)
        if self.login == False:
            self.i = self.i+1
            self.Fallo_UC()
        # Verifico que no cumple el limite.
        if self.i >= 5:
            self.i = 0
            sm.current = "menu"
        
    
    def Fallo_UC(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Usuario y/o contraseña incorrecto(s), intente de nuevo',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        
        self.nameUser.text = ""
        self.namePassword.text = ""

        pop.open()
    
# Pagina para crear usuario
class CreateUserEmpresa(Screen):
    nameAccount = ObjectProperty(None)
    namePassword = ObjectProperty (None)
    empresa.createUser(self.nameAccount.text,self.namePassword.text)

#Pagina para crear cuentas bancarias
class CreateAccountEmpresa(Screen):
    account = ObjectProperty(None)
    empresa.crearCuentaEmpresa(self.account.text)

# Pagina para registra de Ingresos
class IngresosEmpresa(Screen):
    nameCuenta = ObjectProperty(None)
    nameMonto = ObjectProperty(None)
    nameConcepto = ObjectProperty(None)
    empresa.ingresosEmpresa(self.nameCuenta,self.nameMonto,self.nameConcepto)
  
# Pagina para Ingreso de Gastos
class GastosEmpresa(Screen):
    nameCuenta = ObjectProperty(None)
    nameMonto = ObjectProperty(None)
    nameConcepto = ObjectProperty(None)
    empresa.gastosEmpresa(self.nameCuenta,self.nameMonto,self.nameConcepto)
# Pagina para muestra de Balance
class BalanceEmpresa(Screen):
    nameBalance = ObjectProperty(None)
    empresa.balanceEmpresa(self.nameBalance)

class ImpuestoEmpresa(Screen):
    nameEstado = ObjectProperty(None)
    empresa.impuestosEmpresa(self.nameEstado.text)


############## Declaro manejador de ventanas ##############
class WindowManager(ScreenManager):
    pass

###################### Fin de clases, Definicion de instantias #########3################
###################### Defino funciones necesarias ######################
def ir_login_persona(*args):
    sm.current = "loginpersona"

def ir_login_empresa(*args):
    sm.current = "loginempresa"


###################### Fin de funciones necesarias ######################
# Defino el archivo donde se definira el estilo y formato de la pantalla
kv = Builder.load_file("estilo.kv")

#Declaro la instancia controladora de ventanas
sm = WindowManager()

# Declaro las intancias de las funciones Persona y Empresa
persona = funPersona.Personal()
empresa = funEmpresa.Empresa()

general = Funcs.funcs()

# Defino las pantallas al manejador de ventanas
ventanasPersona = [Menu(name="menu"), LoginPersona(name="loginpersona"), CreateUserPersona(name="crearpersona"), IngresosPersona(name="ingresospersona"), GastosPersona(name="gastospersona"), BalancePersona(name="balancepersona")]
ventanasEmpresa = [LoginEmpresa(name="loginempresa"), CreateUserEmpresa(name="crearempresa"), IngresosEmpresa(name="ingresosempresa"), GastosEmpresa(name="gastosempresa"), BalanceEmpresa(name="balanceempresa")]

for ventana in ventanasPersona:     #Ventanas para Persona
    sm.add_widget(ventana)

for ventana in ventanasEmpresa:     #Ventanas para Empresa
    sm.add_widget(ventana)

# Defino la pantalla inicial
sm.current = "menu"

# El incializador o  constructor
class ControlFinancieroApp(App):
    def build(self):
        return sm


# Inicializador
if __name__ == "__main__":
    ControlFinancieroApp().run()

# python3 main.py funPersona.py funEmpresa.py Funcs.py