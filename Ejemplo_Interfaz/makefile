src = main.py
CC = python3

.PHONY = Compilar

all: Compilar #clean

Compilar:
	@nohup $(CC) $(src) >> Salida.txt & 

clean:
	@rm -f nohup.out