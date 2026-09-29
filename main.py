import random
from stock import CATEGORIAS, TIPOS, PRECIOS, STOCK
from math_operations import (
    sumar_lista,
    restar_porcentaje,
    ordenar_mayor_a_menor,
    pila_array,
    precio_coche,
)

#constants
HISTORIAL = []          #lista de coches construidos
CUOTA = 0               #se fija al construir el primer coche
INGRESOS = 0            #suma de ganancias
TAX = 21                #% de impuesto


#Construir
def construir_coche():
    global CUOTA

    # Matriz 4x4 llena de 0 -> aqui apuntamos lo que elige el jugador
    contador = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    for fila in range(4):
        print(CATEGORIAS[fila])
        for col in range(4):
            print(" ", col, TIPOS[col], "precio", PRECIOS[col],
                  "stock", STOCK[fila][col])

        while True:
            eleccion = input("Elige 0-3: ")
            if eleccion == "0" or eleccion == "1" or eleccion == "2" or eleccion == "3":
                col = int(eleccion)
                if STOCK[fila][col] > 0:
                    STOCK[fila][col] = STOCK[fila][col] - 1
                    contador[fila][col] = contador[fila][col] + 1
                    break
                else:
                    print("Sin stock, elige otro.")
            else:
                print("Opcion no valida.")

    #Precio total usando la matriz contador * precios
    total = precio_coche(contador, PRECIOS)

    coche = {
        "contador": contador,
        "precio": total,
        "vendido": False,
        "venta": 0,
        "tax": 0,
        "ganancia": 0,
    }
    HISTORIAL.append(coche)

    #Fijar cuota la primera vez: entre 80% y 150% del precio
    if CUOTA == 0:
        minimo = int(total * 0.8)
        maximo = int(total * 1.5)
        CUOTA = random.randint(minimo, maximo)

    print("Coche construido. Precio total:", total, "€")
    print("Cuota a cumplir:", CUOTA, "€")


# ---------- HISTORIAL ----------
def historial():
    if len(HISTORIAL) == 0:
        print("No hay coches.")
        return

    #pila_array invierte 
    orden = pila_array(HISTORIAL)
    orden = pila_array(orden)

    print("===== HISTORIAL =====")
    numero = 1
    for coche in orden:
        print("\nCoche #", numero, "| precio:", coche["precio"], "€")
        for fila in range(4):
            for col in range(4):
                if coche["contador"][fila][col] > 0:
                    print("   ", CATEGORIAS[fila], TIPOS[col],
                          "x", coche["contador"][fila][col])
        if coche["vendido"]:
            print("   Vendido por", coche["venta"], "€",
                  "| ganancia", coche["ganancia"], "€")
        else:
            print("   (No vendido)")
        numero = numero + 1


#vender
def ganancias():
    global INGRESOS

    #Buscar coches no vendidos
    disponibles = []
    for c in HISTORIAL:
        if c["vendido"] == False:
            disponibles.append(c)

    if len(disponibles) == 0:
        print("No hay coches para vender.")
        return

    for i in range(len(disponibles)):
        print(i, "- precio", disponibles[i]["precio"], "€")

    eleccion = input("Elige coche: ")
    if eleccion == "" or int(eleccion) < 0 or int(eleccion) >= len(disponibles):
        print("Opcion no valida.")
        return

    coche = disponibles[int(eleccion)]

    #Precio de venta = precio + 30%
    venta = coche["precio"] + coche["precio"] * 30 / 100

    # TAX paso a paso (raw)
    print("TAX")
    paso1 = TAX / 100
    print("1) TAX / 100 =", paso1)
    paso2 = venta * paso1
    print("2) venta * paso1 =", venta, "*", paso1, "=", paso2)
    tax = paso2
    print("3) TAX =", tax)

    ganancia = venta - tax
    print("4) ganancia =", venta, "-", tax, "=", ganancia)

    coche["vendido"] = True
    coche["venta"] = venta
    coche["tax"] = tax
    coche["ganancia"] = ganancia

    INGRESOS = INGRESOS + ganancia
    print("Ingresos acumulados:", INGRESOS, "€")


#topearnings
def top_earnings():
    ganancias_lista = []
    for c in HISTORIAL:
        if c["vendido"] == True:
            ganancias_lista.append(c["ganancia"])

    if len(ganancias_lista) == 0:
        print("No hay ventas.")
        return

    ordenadas = ordenar_mayor_a_menor(ganancias_lista)

    print("TOP EARNINGS")
    for g in ordenadas:
        print("  ganancia:", g, "€")


#cuota
def quota():
    return INGRESOS >= CUOTA


#state
def Estado():
    print("Estado->")
    print("Cuota:", CUOTA, "€")
    print("Ingresos:", INGRESOS, "€")
    if quota():
        print("Cuota cumplida: SI")
    else:
        print("Cuota cumplida: NO")

    print("Stock restante:")
    for fila in range(4):
        print(" ", CATEGORIAS[fila], STOCK[fila])


#menu
def menu():
    while True:
        print("===== GARAJE =====")
        print("1. Construir coche")
        print("2. Historial")
        print("3. Vender coche")
        print("4. Top earnings")
        print("5. Estado")
        print("6. Salir")
        op = input("Opcion: ")

        if op == "1":
            construir_coche()
        elif op == "2":
            historial()
        elif op == "3":
            ganancias()
        elif op == "4":
            top_earnings()
        elif op == "5":
            Estado()
        elif op == "6":
            break
        else:
            print("Nope.")


if __name__ == "__main__":
    menu()