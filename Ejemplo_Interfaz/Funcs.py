class funcs:
    def __init__(self, Filename):
        self.Archivo = Filename
        
    def Escritura(self, texto):
        f = open(self.Archivo, "a")
        f.write(texto)
        f.close()
    