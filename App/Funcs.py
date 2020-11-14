class funcs:        
    def Escritura(self, texto, path):
        f = open(self.Archivo, "a")
        f.write(texto)
        f.close()

    