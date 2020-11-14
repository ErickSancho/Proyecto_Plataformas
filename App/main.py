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
  sm.current = ""
    pass
# Pagina para crear usuario
class CreateUserPersona(Screen):
  
  name = ObjectProperty(None)
  persona.crearCuenta(str(name))
# Pagina para registra de Ingresos
class IngresosPersona(Screen):
  nameIngresos = ObjectProperty(None)
  persona.ingresos(nameIngresos)
  
# Pagina para Ingreso de Gastos
class GastosPersona(Screen):
    pass
# Pagina para muestra de Balance
class BalancePersona(Screen):
    pass

######################### Defino las clases de pantallas para empresas #########################

# Clase para la pantalla de ingreso a sistema personal.
class LoginEmpresa(Screen):
  sm.current = ""
    pass
# Pagina para crear usuario
class CreateUserEmpresa(Screen):
  
  name = ObjectProperty(None)
  persona.crearCuenta(str(name))
# Pagina para registra de Ingresos
class IngresosEmpresa(Screen):
  nameIngresos = 
  
# Pagina para Ingreso de Gastos
class GastosEmpresa(Screen):
    pass
# Pagina para muestra de Balance
class BalanceEmpresa(Screen):
    pass


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
ventanasPersona = [Menu(name="menu"), LoginPersona(name="loginpersona"), CreateUserPersona(name="crearpersona"), 
                    IngresosPersona(name="ingresospersona"), GastosPersona(name="gastospersona"), 
                    BalancePersona(name="balancepersona")]
 ventanasEmpresa = [LoginEmpresa(name="loginempresa"), CreateUserEmpresa(name="crearempresa"), 
                    IngresosEmpresa(name="ingresosempresa"), GastosEmpresa(name="gastosempresa"), 
                    BalanceEmpresa(name="balanceempresa")]

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