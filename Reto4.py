
import json

# Diccionario
input1 = input()
dic1 = json.loads(input1)

# Juegos a consultar
input2 = input()
list1 = list(input2.split(" "))

clasificados = {}

# ------- Programa -------
def clasificar():
    dic_clasificar = {}
    for i in dic1:
        seccion = {i : dic1.get(i)}
        for j in list1:
            if i == j:
                dic_clasificar.update(seccion)

    
    clasificados.update(dic_clasificar)


def precioTotal():
    return sum(clasificados.values())

def juegosDisponibles():
    precios_sort = sorted(clasificados.values())
    juegos_sort = {}

    for i in precios_sort:
        for j in clasificados:
            if clasificados[j] == i:
                juegos_sort.update({j : i})

    return " ".join(juegos_sort.keys())[::-1]




# Procesar datos
clasificar()

# Salidas
print(precioTotal())
print(juegosDisponibles())


