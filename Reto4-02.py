
import json


# Juegos disponibles
input1 = input()
juegos = json.loads(input1)

# Juegos a consultar
input2 = input()
consultar = list(input2.split(" "))

clasificados = {}

# ------- Programa -------
def clasificar():
    for i in consultar:
        for j in juegos:
            if i == j:
                clasificados.update({i : juegos[i]})


def precioTotal():
    return sum(clasificados.values())


def juegosDisponibles():
    return " ".join(clasificados.keys())



# Procesar datos
clasificar()

# Salidas
print(precioTotal())
print(juegosDisponibles())


