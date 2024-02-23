import json
import csv

def cargarDatos(archivo):
    try:
        with open(archivo, "r") as file:
            jsonCampers = json.load(file)
            return jsonCampers
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        jsonCampers = []
        return jsonCampers
    
def guardarDatos(datos, archivo):
    with open(archivo, "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)
        print("agregado con exito al archivo json")

def EscribirValoracion(datos, archivo):
    try:
        with open(archivo, "a", newline='') as file:
            pedidos = csv.writer(file, delimiter=',')
            pedidos.writerow(datos)
    except Exception:
        print("archivo no encontrado")

def cargarValoracion(archivo):
    try:
        with open(archivo, "r") as file:
            pedidos = csv.reader(file)
            listaPedidos = []
            for row in pedidos:
                listaPedidos.append(row)
            return listaPedidos
    except Exception:
        lista = []
        return lista