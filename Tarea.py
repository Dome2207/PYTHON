class Tarea:
    def __init__(self):
        pass
    def precio(self):
        precio = float(input("Ingrese el precio: "))
        
        descuento = precio * 0.15
        precio_final = precio - descuento
        
        print("El precio final a pagar es de $ {}".format(precio_final))
    
    def vendedor(self):
        sueldo = float(input("Ingresa el sueldo: "))
        a = float(input("Ingrese la venta Nº1: "))
        b = float(input("Ingrese la venta Nº2: "))
        c = float(input("Ingrese la venta Nº3: "))
        
        comisión = (a+b+c) * 0.10
        
        print("El sueldo del trabajor es de: $ {}".format(sueldo))
        print("La comisión del mes por las tres ventas es de: {}".format(comisión))
        print("El sueldo total con la comisión es de: $ {}".format(sueldo+comisión))
        
    def calificaciones(self):
        cali = float(input("Ingrese el valor de la calificación: "))
        if cali>=7:
            print("Aprobado")
        else:
            print("Reprobado")    
    
    def incremento(self):
        sueldo = float(input("Ingrese el sueldo del trabajador: "))
        aumento = 600*0.10 
        if sueldo > 599:
           print("El aumento es de: {}".format(aumento))
           print("Su nuevo sueldo es de: {}".format(sueldo+aumento))
        else:
           print("Su sueldo es el mismo: {}".format(sueldo))  
                     
    def calcularJornada(self):
        ht, he, het=0,0,0
        ph, phe, pt, ph8=0,0,0,0
        ht = int(input("Ingrese horas trabajadas: "))
        ph = float(input("Ingrese valor de hora: "))
        if ht > 40:
            he = ht-40       
            if he > 8:
                het = he -8 
                ph8 = 8*ph*2
                phe = het*ph*3
            else:
               phe = 0
               ph8 = he*ph*2
            pt = 40*ph + ph8 + phe  
        else:
            pt = ht*ph
        print("Sobretiempo<8:{} Sobretiempo>8:{}, Jornada:{} ".format(ph8,phe,pt))                   
    
    def mayor(self):
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        n3 = int(input("Ingrese el tercer numero: "))
        if n1>=n2 and n1>=n3:
            print("El numero mayor es el primer: {}".format(n1))
        elif n2>=n1 and n2>=n3:
            print("El numero mayor es el segundo: {}".format(n2))
        elif n3>=n1 and n3>=n2:
            print("El numero mayor es el terero: {}".format(n3))       
    
    def variable(self):
        print("Menú: ")
        print("1.")
        print("2.")
        print("3.")
        print("4.")
        v = input("Ingrese el valor de v: ")
        num = input("Ingrese la opcion: ")
        if num == "1":
            print(100*v)
        elif num == "2":
            print(100^v)
        elif num == "3":
            print(v/100)
        else:
            print(0)    
                     
        
    def aspirantes(self):
        calificacion_de_C1 = float (input ('Ingresa el valor de calificacion de C1: '))
        calificacion_de_C2 = float (input ('Ingresa el valor de calificacion de C2: '))
        if calificacion_de_C1>80 and calificacion_de_C2>80:
             print ('Aceptado')
        else:
             print ('Rechazado')
                 
    def elementos(self):
        suma=0
        
        suma = suma
        print(suma)
     
    def numero(self):
       for num in range(1,100): 
        if num > 1:
            cont=0
            i=2
            while i<num and cont==0:
                resto=num%i
                #print("{} % {} = {}".format(num,i,resto))
                if resto ==0:
                    cont+=1
                i+=1
            if cont==0:
                print(num)     

    n=int(input("Ingrese un numero: "))          
    def es_primo(n):
        contador=0
        resultado=True
        for i in range(1, (n+1)):
            if (n%i==0):
                contador+=1
            if (contador>2):
                resultado=False
                break
        return resultado
    if (es_primo(n)==True):
        print("El numero es primo")
    else:
        print("El numero es impar")            
                                      
    
    def factorial(self):
        numero = int(input("Ingrese numero: "))
        acu=1
        for num in range(numero,1,-1):
            acu = acu*num
        print("numero={}, factorial={}".format(numero,acu))
            
               
tarea = Tarea()
# tarea.precio()
# tarea.vendedor()
# tarea.calificaciones()
# tarea.incremento()
# tarea.calcularJornada()
# tarea.mayor()
# tarea.variable() 
# tarea.aspirantes()
# tarea.elementos() 
# tarea.numero()
tarea.es_primo()
# tarea.factorial()