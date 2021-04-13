import random

adivina = random.randint(1, 1000)

nombre_usuario = str(input("Hola yo soy erre, cual es tu nombre?: ").capitalize())
print(f"\nBienvenido {nombre_usuario} te propongo un juego,estoy pensando en un numero entre 1 y 1000.")
print("\nSi adivinas el numero antes de llegar a 3 intentos fallidos seras el ganador del juego. \nComenzemos.")

num1 = int(input("Que numero crees que es?: "))
if num1 == adivina:
    print(f"GANASTE! FELICITACIONES {nombre_usuario}")
else:
    if num1 < adivina:
        print("Intenta con un numero mas grande")
    else:
        print("Intenta con un numero mas pequeño")
print("\nTe quedan 2 intentos")
num1 = int(input("Intenta con otro numero: "))
if num1 == adivina:
    print(f"GANASTE! FELICITACIONES {nombre_usuario}")
else:
    if num1 < adivina:
        print("Intenta con un numero mas grande")
    else:
        print("Intenta con un numero mas pequeño")
print("\nTe queda 1 solo intento")
num1 = int(input("Intenta con otro numero: "))
if num1 == adivina:
    print(f"GANASTE! FELICITACIONES {nombre_usuario}")
else:
    print("Lamentablemente perdiste, intenta en otro momento")
input("\nMuchas gracias por probar este juego realizado por ERRE, para salir del juego presiona ENTER")
