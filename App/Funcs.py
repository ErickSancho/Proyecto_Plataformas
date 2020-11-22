class funcs:        
    def Escritura(self, texto, path):
        f = open(self.Archivo, "a")
        f.write(texto)
        f.close()
    
    def Revisar_Contrasena(self,cont):
        contador = 0
        for L in cont:
            contador += 1
            
        return contador    