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
        persona.setupPersona()

    def EntraEmpresa(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ingresar a Empresa?',
                content=content,
                auto_dismiss=False,
                size_hint=(None, None), size=(350, 200))

        content.bind(on_press=pop.dismiss)
        content.bind(on_press=ir_login_empresa)
        
        pop.open()

        empresa.setupEmpresa()
        


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
        # Se verifica si 
        Flag_de_Error = True #Bandera para caso de error 
        try:
            self.login = empresa.loginUser(self.nameUser.text, self.namePassword.text)
        except:
            self.Fallo_UC()
            Flag_de_Error = False

        # Si no hubo error se ejecutara 
        if Flag_de_Error:
            if self.login == False:
                self.i = self.i+1
                self.Fallo_UC()
            else:
                persona.ActualUser(self.nameUser.text)
                sm.current = "menupersona"
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
    againPassword = ObjectProperty(None)
    
    def createUser(self):
        if (self.nameAccount.text!="") and (self.namePassword.text!=""): # Reviso que los valores sen validos
            val_cont = general.Revisar_Contrasena(self.namePassword.text) # Reviso que la contrasena sea de mas de 8 digitos
            if val_cont>=8:
                if self.namePassword.text == self.againPassword.text:
                        newUser = persona.createUser(self.nameAccount.text,self.namePassword.text) # Reviso que el usuario no se haya creado y si no lo creo
                        if newUser != -1:
                            persona.ActualUser(self.nameAccount.text)
                            self.nameAccount.text = ""
                            self.namePassword.text = ""
                            sm.current = "createaccountpersona"
                        else:
                            self.nameAccount.text = ""
                            self.namePassword.text = ""
                            self.againPassword.text = ""
                            self.userNotValid()
                    
                else:
                    self.no_coinciden()
            else:
                self.Error_longitud()
        else:
            self.userNotValid()
            
    def userNotValid (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ese usuario ya fue creado, o no es un nombre valido. Intente con otro nombre.',
            content=content,
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
    
        pop.open()

    def no_coinciden (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Las contraseñas ingresadas no coinciden',
            content=content,
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.nameAccount.text = ""
        self.namePassword.text = ""
        self.againPassword.text = ""
        pop.open()
    
    def Error_longitud (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='La contraseña debe ser igual o mayor a 8 digitos\nIngrese de nuevo',
            content=content,
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.namePassword.text = ""
        self.againPassword.text = ""
        pop.open()



#Pagina para crear cuentas:
class CreateAccountPersona (Screen):
    account = ObjectProperty(None)
    def createAccount(self):
        persona.crearCuenta(self.account.text)
        self.account.text = ""
        sm.current="menupersona"
        

# Pagina para registro de Ingresos

class MenuPersona (Screen):
    def Cerrar_secion(self):
        persona.Usuarioactual = ""

class IngresosPersona(Screen):
    nameIngresos = ObjectProperty(None)
    montoIngresos = ObjectProperty(None)
    conceptoIngresos = ObjectProperty(None)
    def ingresos(self):
        persona.ingresos(self.nameIngresos.text,self.montoIngresos.text,self.conceptoIngresos.text)
        self.nameIngresos.text = ""
        self.montoIngresos.text = ""
        self.conceptoIngresos.text = ""

  
# Pagina para Ingreso de Gastos
class GastosPersona(Screen):
    nameGastos = ObjectProperty(None)
    montoGastos = ObjectProperty(None)
    conceptoGastos = ObjectProperty (None)
    def gastos(self):
        persona.gastos(self.nameGastos.text,self.montoGastos.text,self.conceptoGastos.text)
        self.nameGastos.text = ""
        self.montoGastos.text = ""
        self.conceptoGastos.text = ""
# Pagina para muestra de Balance
class BalancePersona(Screen):
    nameBalance = ObjectProperty(None)
    def balance(self):
        persona.balance(self.nameBalance.text)

######################### Defino las clases de pantallas para empresas #########################

# Clase para la pantalla de ingreso a sistema personal.
class LoginEmpresa(Screen):
        #Aquí van los login de la empresa
    nameUser = ObjectProperty(None)
    namePassword = ObjectProperty(None) 
    
    login = False
    i = 0
    def check_userpassword(self):
        # Se verifica si 
        Flag_de_Error = True #Badera para caso de error 
        try:
            self.login = persona.loginUser(self.nameUser.text, self.namePassword.text)
        except:
            self.Fallo_UC()
            Flag_de_Error = False

        # Si no hubo error se ejecutara 
        if Flag_de_Error:
            if self.login == False:
                self.i = self.i+1
                self.Fallo_UC()
            else:
                empresa.ActualUser(self.nameUser.text)
                sm.current = "menuempresa"
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
class CreateUserEmpresa(Screen):
    nameAccount = ObjectProperty(None)
    namePassword = ObjectProperty (None)
    againPassword = ObjectProperty(None)
    
    def createUser(self):
        if (self.nameAccount.text!="") and (self.namePassword.text!=""): # Reviso que los valores sen validos
            val_cont = general.Revisar_Contrasena(self.namePassword.text) # Reviso que la contrasena sea de mas de 8 digitos
            if val_cont>=8:
                if self.namePassword.text == self.againPassword.text:
                        newUser = empresa.createUser(self.nameAccount.text,self.namePassword.text) # Reviso que el usuario no se haya creado y si no lo creo
                        if newUser != -1:
                            empresa.ActualUser(self.nameAccount.text)
                            self.nameAccount.text = ""
                            self.namePassword.text = ""
                            sm.current = "createaccountempresa"
                        else:
                            self.nameAccount.text = ""
                            self.namePassword.text = ""
                            self.againPassword.text = ""
                            self.userNotValid()
                    
                else:
                    self.no_coinciden()
            else:
                self.Error_longitud()
        else:
            self.userNotValid()
            
    def userNotValid (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Ese usuario ya fue creado, o no es un nombre valido. Intente con otro nombre.',
            content=content,
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
    
        pop.open()

#Pagina para crear cuentas bancarias
class CreateAccountEmpresa(Screen):
    account = ObjectProperty(None)
    def createAccount(self):
        empresa.crearCuentaEmpresa(self.account.text)
        self.account.text = ""
        sm.current="menuempresa"

# Pagina para registra de Ingresos
class IngresosEmpresa(Screen):
    nameCuenta = ObjectProperty(None)
    nameMonto = ObjectProperty(None)
    nameConcepto = ObjectProperty(None)
    def ingresos(self):
        empresa.ingresosEmpresa(self.nameCuenta.text,self.nameMonto.text,self.nameConcepto.text)
        self.nameCuenta = ""
        self.nameMonto = ""
        self.nameConcepto = ""

# Pagina para Ingreso de Gastos
class GastosEmpresa(Screen):
    nameGastos = ObjectProperty(None)
    montoGastos = ObjectProperty(None)
    conceptoGastos = ObjectProperty (None)
    def gastos(self):
        empresa.gastosEmpresa(self.nameGastos.text,self.montoGastos.text,self.conceptoGastos.text)
        self.nameGastos.text = ""
        self.montoGastos.text = ""
        self.conceptoGastos.text = ""
# Pagina para muestra de Balance
class BalanceEmpresa(Screen):
    nameBalance = ObjectProperty(None)
    def balance(self):
        empresa.balanceEmpresa(self.nameBalance.text)

class ImpuestoEmpresa(Screen):
    nameEstado = ObjectProperty(None)
    def impuestos(self):
        empresa.taxesEmpresa(self.nameEstado.text)


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
ventanasPersona = [Menu(name="menu"), LoginPersona(name="loginpersona"), CreateUserPersona(name="crearpersona"), IngresosPersona(name="ingresospersona"), GastosPersona(name="gastospersona"), BalancePersona(name="balancepersona"), MenuPersona(name="menupersona"), CreateAccountPersona(name="createaccountpersona")]
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