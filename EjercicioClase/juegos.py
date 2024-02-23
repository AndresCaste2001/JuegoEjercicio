import jsonCrud
import time
def registroJuego():
    listaJuegos = jsonCrud.cargarDatos("Juegos.json")
    while True:
        print("*****************************")
        print("       CREACION JUEGOS       ")
        print("*****************************")
        try:
            nombre = input("Ingrese el nombre: ")
            tiempoPartida = int(input(("Ingrese el tiempo por partida en minutos: ")))
            cantJugadores = int(input(("Ingrese la cantidad de jugadores: ")))
            inventario = int(input("Ingrese la cantidad de inventario del juego: "))
        except ValueError:
            print("Ingrese valores correctos")
            time.sleep(2)
            continue
        listaJuegos.append({'nombre':nombre,'tiempoPartida':tiempoPartida,'cantJugadores':cantJugadores,'cantJuegos':inventario})
        jsonCrud.guardarDatos(listaJuegos,"Juegos.json")
        break

def modJuego():
    listaJuegos = jsonCrud.cargarDatos("Juegos.json")
    if listaJuegos:
        while True:


            print("*****************************")
            print("  MODIFICACION JUEGOS  ")
            print("*****************************")

            for index,juego in enumerate(listaJuegos):
                nombre = juego.get('nombre','no existe nombre')
                print(f"{index+1}- {nombre}")
            try:
                opcJuego = int(input("\nIngresa una opcion: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue

            print("1.)Modificar tiempo por partida")
            print("2.)Modificar Cantidad de jugadores")
            print("3.)Modificar cantidad de juegos disponibles")
            print("0.)Salir")
            try:
                opc = int(input("\nIngresa una opcion: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            while True:
                try:
                    if opc == 1:
                        tiempoNuevo = int(input(("Ingresa el nuevo tiempo por partida (minutos): \n")))
                        listaJuegos[opcJuego-1]['tiempoPartida'] = tiempoNuevo
                        break
                    elif opc == 2:
                        cantNuevo = int(input(("Ingresa la nueva cantidad de jugadores: \n")))
                        listaJuegos[opcJuego-1]['cantJugadores'] = cantNuevo
                        break
                    elif opc == 3:
                        invNuevo = int(input(("Ingresa la nueva cantidad de inventario: \n")))
                        listaJuegos[opcJuego-1]['cantJuegos'] = invNuevo
                        break
                except  ValueError:
                    print("Ingrese valores correctos")
                    time.sleep(2)
                    continue
                if opc == 0:
                    break
            jsonCrud.guardarDatos(listaJuegos,"Juegos.json")
            break
    else:
        print("no existen juegos registrados")

def eliminarJuego():
    listaJuegos = jsonCrud.cargarDatos("Juegos.json")
    if listaJuegos:
        while True:
            print("*****************************")
            print("       ELIMINAR JUEGOS       ")
            print("*****************************")

            for index,juego in enumerate(listaJuegos):
                nombre = juego.get('nombre','no existe nombre')
                print(f"{index+1}- {nombre}")
            try:
                opcJuego = int(input("\nIngresa una opcion: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            try:
                listaJuegos.pop(opcJuego-1)
                print("Eliminado con exito")
            except Exception:
                print("Ingrese un indice correcto")
                time.sleep(2)
                continue
            jsonCrud.guardarDatos(listaJuegos,"Juegos.json")
            time.sleep(2)

            break
def consultarJuego():
    listaJuegos = jsonCrud.cargarDatos("Juegos.json")
    if listaJuegos:
        while True:
            print("*****************************")
            print("       CONSULTAR JUEGOS      ")
            print("          POR TIEMPO         ")
            print("*****************************")

            try:
                tiempoReq = int(input("Ingresa el tiempo que tienes disponible para jugar(minutos): "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            print("Juegos relacionados con tu busqueda: ")
            for juego in listaJuegos:
                nombre = juego.get('nombre','no existe nombre')
                tiempo = juego.get('tiempoPartida','no existe tiempo')
                if tiempo<=tiempoReq:
                    print(f" {nombre}")
            time.sleep(3)
            print("\n\n")
            break

def valorarJuego():
    listaJuegos = jsonCrud.cargarDatos("Juegos.json")
    listaValoracion = []
    if listaJuegos:
        while True:
            print("*****************************")
            print("        VALORAR JUEGOS       ")
            print("*****************************")
            print("Juegos Disponibles: ")

            for index,juego in enumerate(listaJuegos):
                nombre = juego.get('nombre','no existe nombre')
                print(f"{index+1}- {nombre}")
            try:
                opcJuego = int(input("\nIngresa una opcion: "))
                valoracion =int(input("Ingresa la valorcion del 1-100: "))
                nombreJuego = listaJuegos[opcJuego-1]['nombre']
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if valoracion>=0 and valoracion<=100:
                listaValoracion = [nombreJuego,valoracion]
                jsonCrud.EscribirValoracion(listaValoracion,"valoraciones.csv")
                print("Valoracion subida exitosamente")
            break

def topValoraciones():
    cantValoracion = {}
    ListaValoracion = jsonCrud.cargarValoracion("valoraciones.csv")
    print("*****************************")
    print("        TOP 3 JUEGOS        ")
    print("*****************************")
    for juego,a in ListaValoracion:
        if juego in cantValoracion:
            cantValoracion[juego] += 1
        else:
            cantValoracion[juego] = 1

    topTres = sorted(cantValoracion.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Los tres juegos con más valoraciones son:")
    for juego, cantidad in topTres:
        print(f"{juego}: {cantidad}")

