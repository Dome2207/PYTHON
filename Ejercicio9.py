"Funciones matematicas"
import math
num1, num2, num, men = 12.572, 15.4, 4, '1234'
print(math.ceil(num1), '\t' , math.floor(num1))
print(round(num1,1), '\t' , type(num), '\t' ,  type(men))

#Funciones de cadenas
mensaje = 'Hola'+'mundo'+'Python'
men1 = mensaje.split()
men2 = "".join(men1)
print(mensaje[0], mensaje[0:4],men1,men2)
print(mensaje.find("mundo"),mensaje.lower())