def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total


def restar_porcentaje(a, b):
    parte = a * b / 100
    return a - parte


def ordenar_mayor_a_menor(datos):
    n = len(datos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if datos[j] < datos[j + 1]:
                temp = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = temp
    return datos


def pila_array(datos):
    pila = [0] * len(datos)
    tope = -1
    for valor in datos:
        tope = tope + 1
        pila[tope] = valor
    resultado = []
    while tope >= 0:
        resultado.append(pila[tope])
        tope = tope - 1
    return resultado


def precio_coche(contador, precios):
    total = 0
    for fila in range(4):
        for col in range(4):
            total = total + contador[fila][col] * precios[col]
    return total