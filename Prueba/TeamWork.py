

print("""
      Yo hice este cambio, ahora hazlo vos. 
      Att: Julian :)
      """)

from random import *

# 1. menor a 1 o superior a 100 ERROR
# 2. Si el numero del usuario es menor al elegido por el programa INCORRECTO
# 3. Si el numero del usuario es mayor al elegido por el programa INCORRECTO
# 4. Si el numero del usuario es igual al elegido por el programa CORRECTO junto con los intentos que le tomo

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre + ", bienvenid@ al Juego. \nAdivina el numero del 1 al 100. \nSolo tienes 8 intentos\n")

numero_random = randint(1, 100)
intentos = 1

while intentos <= 8:
    numero = int(input("Ingrese el numero: "))
    if numero < 1 or numero > 100:
        print("El numero no puede ser menor a 1 o mayor a 100.\n")
        intentos += 1
        continue
    elif numero < numero_random:
        print(f"El {numero} No es. Te falta, mi numero es mayor que ese. \nTienes", (8 - intentos), " intentos restantes.\n")
        intentos += 1
        continue
    elif numero > numero_random:
        print(f"El {numero} No es. Te pasaste, mi numero es menor que ese. \nTienes", (8 - intentos), " intentos restantes.\n")
        intentos += 1
        continue
    elif numero == numero_random:
        print("Correcto. Has adivinado mi numero en ", (intentos), " intentos.")
        break
    elif intentos == 8:
        print("Lo siento, se te han acabado los intentos. El numero era " + str(numero_random) + ". \nGracias por jugar.")
        break
    else:
        print("Error. Intente de nuevo.")
        intentos += 1