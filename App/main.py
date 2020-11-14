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
        pop.open()

    def EntraEmpresa(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ingresar a Empresa?',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        pop.open()
        
    # def ir_login(self):
    #     sm.current = "loginpersona"

# content=Label(text='Invalid username or password.'),
###  Defino las clases para la parte personal  ####

# Clase para la pantalla de ingreso a sistema personal.
class LoginPersona(Screen):
    pass
# Pagina para crear usuario
class CreateUserPersona(Screen):
    pass
# Pagina para registra de Ingresos
class IngresosPersona(Screen):
    pass
# Pagina para Ingreso de Gastos
class GastosPersona(Screen):
    pass
# Pagina para muestra de Balance
class BalancePersona(Screen):
    pass

### Defino las clases de pantallas para empresas ###

# Pagina de Ingreso de Usuario  No se si se podra emplear la misma que para Persona
# class LoginEmpresa(Screen):
#     pass


#### Declaro manejador de ventanas ####
class WindowManager(ScreenManager):
    pass

###################### Fin de clases, Definicion de instantias #########3################

# Defino el archivo donde se definira el estilo y formato de la pantalla
kv = Builder.load_file("estilo.kv")

#Declaro la instancia controladora de ventanas
sm = WindowManager()

# Declaro las intancias de las funciones Persona y Empresa
persona = funPersona.Presonal()
empresa = funEmpresa.Empresa()

general = Funcs.funcs()

# Defino las pantallas al manejador de ventanas
ventanasPersona = [Menu(name="menu"), LoginPersona(name="loginpersona"), CreateUserPersona(name="crearpersona"), 
                    IngresosPersona(name="ingresospersona"), GastosPersona(name="gastospersona"), 
                    BalancePersona(name="balancepersona")]
# ventanasEmpresa = []
# sm.add_widget(Menu(name="menu"))    #Menu

for ventana in ventanasPersona:     #Ventanas para Persona
    sm.add_widget(ventana)

# for ventana in ventanasEmpresa:     #Ventanas para Empresa
#     sm.add_widget(ventana)

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