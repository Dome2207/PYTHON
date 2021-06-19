"Funcion con retorno de valor"
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ /len(notas)

# llamada a funcion
listanotas = [2,4,6,8,10]
prom=promedio(listanotas)
print("Promedio:{}={}".format(listanotas,prom))