from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
#from kivy.uix.floatlayout import FloatLayout

from Funcs import funcs


# Pagina 1.
class Contenedor(Widget):
    name = ObjectProperty(None)     #Valor que se trae desde el ".kv"
    lastName = ObjectProperty(None)

    def Guardar(self): #Funcion que llama Escritura con lo cual se guarda en el un archivo de texto
        cadena ="Nombre: "+ self.name.text+ ", Apellido: "+self.lastName.text+ '\n'
        Doc.Escritura(cadena)
        self.name.text = ""
        self.lastName.text = ""


# Constructor de la aplicacion
class AplicacionApp(App):
    def build(self):
        return Contenedor()


#Se crea la instancia de la funcion de escitura
Doc = funcs("Entradas.txt")

#Archivo ".kv"
kv = Builder.load_file("aplicacion.kv")


if __name__ == "__main__":
    AplicacionApp().run()