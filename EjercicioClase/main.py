import time
import juegos
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("*****************************")
    print("  Bienvenidos a la tienda  ")
    print("*****************************")
    print("1.)Gestion de juegos")
    print("2.)Consultas y valoraciones")
    print("0.)Salir")
    try:
        opc = int(input("\nIngresa una opcion: "))
    except ValueError:
        print("\n***ingresa una opcion correcta***")
        time.sleep(2)
        continue
    if opc == 1:
        while True:
            clear()
            print("1.)Registrar Juego")
            print("2.)Modificar Juego")
            print("3.)Eliminar Juego")
            print("0.)Salir")
            try:
                opc = int(input("\nIngresa una opcion: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if opc == 1:
                clear()
                juegos.registroJuego()
                time.sleep(2)
            elif opc == 2:
                clear()
                juegos.modJuego()
                time.sleep(2)
            elif opc == 3:
                clear()
                juegos.eliminarJuego()
                time.sleep(2)
            elif opc == 0: 
                break

    elif opc == 2:
        while True:
            clear()
            print("1.)Consultar Juego")
            print("2.)Valorar Juego")
            print("3.)Top juegos valorados")
            print("0.)Salir")
            try:
                opc = int(input("\nIngresa una opcion: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if opc == 1:
                clear()
                juegos.consultarJuego()
                time.sleep(2)
            elif opc == 2:
                clear()
                juegos.valorarJuego()
                time.sleep(2)
            elif opc == 3:
                clear()
                juegos.topValoraciones()
                time.sleep(3)
            elif opc == 0: 
                break
    elif opc == 0:
        break 