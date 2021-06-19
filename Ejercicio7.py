"Funciones si sentido"
def vocales(letra):
    for car in letra:
        if car in('a','e','i','o','u'):
            print(car)

"Llamada a funcion"
oración =input("Ingrese oración: ")
vocales(oración.lower())