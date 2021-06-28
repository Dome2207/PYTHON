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
   
                   
    def aspirantes(self):
        calificacion_de_C1 = float (input ('Ingresa el valor de calificacion de C1: '))
        calificacion_de_C2 = float (input ('Ingresa el valor de calificacion de C2: '))
        if calificacion_de_C1>80 and calificacion_de_C2>80:
             print ('Aceptado')
        else:
             print ('Rechazado')
     
    def generar_numeros(self):
        total = 0
        num = 4
        for i in range(0, num+1):
            total = total + i * i
        print("El resultado 0 a {} es: {}".format(num,total))   
                 
    def numero(self):
          i = 1
          while i <= 100:
              print(i)
              i = i + 1
    
    def producto(self):
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        suma = num1+num2
        producto = num1*num2
        print("La respuesta de la suma es: {}".format(suma))
        print("La respuesta del producto es: {}".format(producto)) 
              
                
    def primo(n):
        n=int(input("Ingrese un número: "))
        if n <= 0:
            print("El número debe ser mayor que cero")
        else:
            cant_divisores = 0
            i = 1
            while (i <= n):
                if n % i == 0:
                    cant_divisores+=1
                i+=1
            if cant_divisores==2:
                print("El número es primo")
            else:
                print("El número no es primo") 
    
    def serie(self):
        comprobar = True
        while comprobar == True:
            numero = int(input("Ingrese un número: "))
            if numero > 0:
                comprobar = False
                resultado = 0 
                for i in range(1,numero+1):
                    resultado +=(1/i)
                print("El resultado de la serie es: {}".format(resultado))
            else:
                print("El número ingresado no es correcto. Inténtelo nuevamente.")        
                                        
            
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
# tarea.aspirantes()
# tarea.numero()
# tarea.producto()
# tarea.primo()
# tarea.generar_numeros()
# tarea.serie()
# tarea.factorial()