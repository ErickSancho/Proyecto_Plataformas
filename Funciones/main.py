#coding = utf-8
import fun

def main():
    fun.setup()

    name = input("Digite su nombre:\n")
    user = fun.Person(name)

    user.crearCuenta()
    user.definirAction()
    user.definirAction()
    user.definirAction()

if __name__ == "__main__":
    main()