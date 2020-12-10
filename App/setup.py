import sys 

def setup():
    for line in sys.stdin: 
        write_file(line)

def write_file(path):
    path = path[:-1]
    with open("./Aplicacion_financiera.desktop", "w") as file:
        file.write("[Desktop Entry]\n")
        file.writelines("Version=1.0\n")
        file.writelines("Name=Aplicacion Financiera\n")
        ruta_exec = "Exec=" + path + "/main.py\n"
        file.write(ruta_exec)
        ruta_ico = "Icon="+path+"/img/dollar.ico\n"
        file.write(ruta_ico)
        file.write("Type=Application")

if __name__ == "__main__":
    setup()