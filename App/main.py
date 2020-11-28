#coding = utf-8

# Librerias de la interrfaz grafica
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.floatlayout import FloatLayout

# funciones para calculos 
import funPersona
import funEmpresa
import Funcs


# Defino el color de la pantalla
Window.clearcolor = (52/255.0, 97/255.0, 180/255.0, 1)


######################## Definicion de clases ############################

# Clase para la pantalla principal en la cual se elige el tipo de uso que se 
# desea dar al sistema Personal o Empresa
class Menu(Screen):
    pass
    # texto = ObjectProperty(None)
    
    def EntraPersona(self):
    #     layout = GridLayout(cols = 2, padding = 30, spacing = 25)
    #     boton_ok = Button(text='Aceptar', size_hint=(0.25, 0.25),font_size= 20)
    #     boton_cancel = Button(text='Cancelar', size_hint=(0.25, 0.25),font_size= 20)
    #     layout.add_widget(boton_ok)
    #     layout.add_widget(boton_cancel)
    #     pop = Popup(title='Ingresar a Persona?',
    #             title_size = '20',
    #             title_align = 'center',
    #             content=layout,
    #             auto_dismiss=False,
    #             size_hint=(None, None), size=(350, 200))

    #     boton_ok.bind(on_press = pop.dismiss)
    #     boton_ok.bind(on_press = ir_login_persona)
    #     boton_cancel.bind(on_press = pop.dismiss)
    #     pop.open()
        persona.setupPersona()

    def EntraEmpresa(self):
    #     layout = GridLayout(cols = 2, padding = 30, spacing = 25)
    #     boton_ok = Button(text='Aceptar', size_hint=(0.25, 0.25),font_size= 20)
    #     boton_cancel = Button(text='Cancelar', size_hint=(0.25, 0.25),font_size= 20)
    #     layout.add_widget(boton_ok)
    #     layout.add_widget(boton_cancel)
    #     pop = Popup(title='Ingresar a Empresa?',
    #             title_size = '20',
    #             title_align = 'center',
    #             content=layout,
    #             auto_dismiss=False,
    #             size_hint=(None, None), size=(350, 200))

    #     boton_ok.bind(on_press = pop.dismiss)
    #     boton_ok.bind(on_press = ir_login_empresa)
    #     boton_cancel.bind(on_press = pop.dismiss)
        
    #     pop.open()

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
                persona.ActualUser(self.nameUser.text)
                self.nameUser.text = ""
                self.namePassword.text = "" 
                sm.current = "menupersona"
            # Verifico si se acabaron los intentos.
            if self.i >= 5:
                self.i = 0
                self.nameUser.text = ""
                self.namePassword.text = "" 
                sm.current = "menu"
        
    
    def Fallo_UC(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Usuario y/o contraseña incorrecto(s), intente de nuevo',
                content=content,
                title_align = 'center',
                title_size = '20',
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
                            self.againPassword.text = ""
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
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
    
        pop.open()

    def no_coinciden (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Las contraseñas ingresadas no coinciden',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        
        self.namePassword.text = ""
        self.againPassword.text = ""
        pop.open()
    
    def Error_longitud (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='La contraseña debe ser igual o mayor a 8 digitos\nIngrese de nuevo',
            content=content,
            title_align = 'center',
            title_size = '20',
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
        try:
            persona.crearCuenta(self.account.text)
            self.account.text = ""
            sm.current="menupersona"
        except:
            self.Error_cuenta()

    def Error_cuenta (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='El nombre de cuenta ingresado no es valido',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.account.text = ""
        pop.open()
        

# Pagina para registro de Ingresos

class MenuPersona (Screen):
    def Seguro_cerrar (self):
        layout = GridLayout(cols = 2, padding = 30, spacing = 25)
        boton = Button(text='Aceptar', size_hint=(0.25, 0.25),font_size= 20)
        boton2 = Button(text='Cancelar', size_hint=(0.25, 0.25),font_size= 20)
        layout.add_widget(boton)
        layout.add_widget(boton2)
        pop = Popup(title='Seguro de cerrar sesión?',
            content=layout,
            title_size = '20',
            title_align = 'center',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 180))

        boton.bind(on_release = pop.dismiss)
        boton.bind(on_release = ir_login_persona)
        boton2.bind(on_release = pop.dismiss)
        pop.open() 
    

class IngresosPersona(Screen):
    nameIngresos = ObjectProperty(None)
    montoIngresos = ObjectProperty(None)
    conceptoIngresos = ObjectProperty(None)
    def ingresos(self):
        try:
            persona.ingresos(self.nameIngresos.text,self.montoIngresos.text,self.conceptoIngresos.text)
            self.nameIngresos.text = ""
            self.montoIngresos.text = ""
            self.conceptoIngresos.text = ""
        except:
            self.Datos_invalidos()


    def Datos_invalidos (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Valores ingresados no son válidos',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.nameIngresos.text = ""
        self.montoIngresos.text = ""
        self.conceptoIngresos.text = ""
        pop.open()     

  
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
        try:
            persona.balance(self.nameBalance.text)
            persona.PlotFigures(self.nameBalance.text)
            self.nameBalance.text = ""
        except:
            self.Datos_invalidos()
            self.nameBalance.text = ""

    
    def Datos_invalidos (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='La cuenta ingresada no es válida',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        pop.open()

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
                empresa.ActualUser(self.nameUser.text)
                self.nameUser.text = ""
                self.namePassword.text = "" 
                sm.current = "menuempresa"
            # Verifico si se acabaron los intentos.
            if self.i >= 5:
                self.i = 0
                sm.current = "menu"
        
    
    def Fallo_UC(self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Usuario y/o contraseña incorrecto(s), intente de nuevo',
                content=content,
                title_align = 'center',
                title_size = '20',
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
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
    
        pop.open()

    def no_coinciden (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Las contraseñas ingresadas no coinciden',
            content=content,
            title_align = 'center',
            title_size = '20',
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
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.namePassword.text = ""
        self.againPassword.text = ""
        pop.open()



#Pagina para crear cuentas:
class CreateAccountEmpresa (Screen):
    account = ObjectProperty(None)
    def createAccount(self):
        try:
            empresa.crearCuentaEmpresa(self.account.text)
            self.account.text = ""
            sm.current="menuempresa"
        except:
            self.Error_cuenta()

    def Error_cuenta (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='El nombre de cuenta ingresado no es valido',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.account.text = ""
        pop.open()
        

# Pagina para registro de Ingresos

class MenuEmpresa (Screen):
    def Seguro_cerrar (self):
        layout = GridLayout(cols = 2, padding = 30, spacing = 25)
        boton = Button(text='Aceptar', size_hint=(0.25, 0.25),font_size= 20)
        boton2 = Button(text='Cancelar', size_hint=(0.25, 0.25),font_size= 20)
        layout.add_widget(boton)
        layout.add_widget(boton2)
        pop = Popup(title='Seguro de cerrar sesión?',
            content=layout,
            title_size = '20',
            title_align = 'center',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 180))

        boton.bind(on_release = pop.dismiss)
        boton.bind(on_release = ir_login_empresa)
        boton2.bind(on_release = pop.dismiss)
        pop.open() 
    

class IngresosEmpresa(Screen):
    nameIngresos = ObjectProperty(None)
    montoIngresos = ObjectProperty(None)
    conceptoIngresos = ObjectProperty(None)
    def ingresos(self):
        try:
            empresa.ingresosEmpresa(self.nameIngresos.text,self.montoIngresos.text,self.conceptoIngresos.text)
            self.nameIngresos.text = ""
            self.montoIngresos.text = ""
            self.conceptoIngresos.text = ""
        except:
            self.Datos_invalidos()


    def Datos_invalidos (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='Valores ingresados no son válidos',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        self.nameIngresos.text = ""
        self.montoIngresos.text = ""
        self.conceptoIngresos.text = ""
        pop.open()     

  
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
        try:
            empresa.balanceEmpresa(self.nameBalance.text)
            empresa.PlotFigures(self.nameBalance.text)
            self.nameBalance.text = ""
        except:
            self.Datos_invalidos()
            self.nameBalance.text = ""
    
    def Datos_invalidos (self):
        content = Button(text='Aceptar', size_hint=(0.5, 0.5),font_size= 20)
        pop = Popup(title='La cuenta ingresada no es válida',
            content=content,
            title_align = 'center',
            title_size = '20',
            auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))

        content.bind(on_release=pop.dismiss)
        pop.open()

class ImpuestoEmpresa(Screen):
    impuesto_ent_jur = ObjectProperty(None)
    impuesto_renta = ObjectProperty(None)

    def Determine(self):

        layout = GridLayout(cols = 2, padding = 30, spacing = 25)
        boton_ok = Button(text='Si', size_hint=(0.25, 0.25),font_size= 20)
        boton_cancel = Button(text='No', size_hint=(0.25, 0.25),font_size= 20)
        layout.add_widget(boton_ok)
        layout.add_widget(boton_cancel)
        pop = Popup(title='¿Esta su empresa registrada?',
                title_size = '20',
                title_align = 'center',
                content=layout,
                auto_dismiss=False,
                size_hint=(None, None), 
                size=(350, 200))

        boton_ok.bind(on_release = pop.dismiss)
        boton_ok.bind(on_press = self.impuestos_si)
        boton_cancel.bind(on_release = pop.dismiss)
        boton_cancel.bind(on_press = self.impuestos_no)
        
        pop.open()


    def impuestos_si(self, *kargs):
        val1, val2 = empresa.taxesEmpresaSI()
        if float(val1)<0:
            val1 = str(0.0)
        if float(val2)<0:
            val2 = str(0.0)
        
        self.impuesto_ent_jur.text, self.impuesto_renta.text = val1, val2

    
    def impuestos_no(self, *kargs):
        val1, val2 = empresa.taxesEmpresaNO()
        if float(val1)<0:
            val1 = str(0.0)
        if float(val2)<0:
            val2 = str(0.0)
        
        self.impuesto_ent_jur.text, self.impuesto_renta.text = val1, val2



        


############## Declaro manejador de ventanas ##############
class WindowManager(ScreenManager):
    pass

###################### Fin de clases, Definicion de instantias #########3################
###################### Defino funciones necesarias ######################
def ir_login_persona(*args):
    sm.current = "loginpersona"
    sm.transition.direction = "left"
    persona.Usuarioactual = ""

def ir_login_empresa(*args):
    sm.current = "loginempresa"
    sm.transition.direction = "left"


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
ventanasPersona = [Menu(name="menu"), LoginPersona(name="loginpersona"), CreateUserPersona(name="crearpersona"), IngresosPersona(name="ingresospersona"), 
                    GastosPersona(name="gastospersona"), BalancePersona(name="balancepersona"), MenuPersona(name="menupersona"), CreateAccountPersona(name="createaccountpersona")]

ventanasEmpresa = [LoginEmpresa(name="loginempresa"), CreateUserEmpresa(name="crearempresa"), IngresosEmpresa(name="ingresosempresa"), GastosEmpresa(name="gastosempresa"), 
                    BalanceEmpresa(name="balanceempresa"), MenuEmpresa(name = "menuempresa"), CreateAccountEmpresa(name="createaccountempresa"), ImpuestoEmpresa(name="impuestoempresa")]

for ventana in ventanasPersona:     #Ventanas para Persona
    sm.add_widget(ventana)

for ventana in ventanasEmpresa:     #Ventanas para Empresa
    sm.add_widget(ventana)

# Defino la pantalla inicial
sm.current = "impuestoempresa"

# El incializador o  constructor
class ControlFinancieroApp(App):
    def build(self):
        return sm


# Inicializador
if __name__ == "__main__":
    ControlFinancieroApp().run()

# python3 main.py funPersona.py funEmpresa.py Funcs.py