class For:
    def __init__(self):
        pass
    
    
    def usoFor(self):
        # ciclo repetivo de incrementos o decrementos se ejecuta por verdadero
        nombre = "Doménica"
        datos=["Doménica",19,True]
        # pos     0       1   2
        numeros=(2,5.6,4,1)
        estudiantes = {"nombre": "Doménica", "edad": 19, "fac": "faci"}
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Doménica","final":70},{"nombre":"Lady","final":60},{"nombre":"Natanael","final":90}]
        # range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial
        # se ejecuta desde inicio hasta el limite
        # for con range() o for con colecciones 
        # j=0
        # while j<5:
        #     print("while",j)
        #     j=j+1
        
        # for i in range(5): # rango(0,1,2,3,4)
        #     print("for",i,end=" ")
        # print()    
        # for i in range(1,5): # rango(1,2,3,4)
        #     print("for",i,end=" ")
        # print()     
        # for i in range(2,10,2): # rango(2,4,6,8)
        #     print("for",i,end=" ") 
        # print()      
        # for i in range(12,3,-3): # rango(12,9,6)
        #     print("for",i,end=" ")  
        
        # lon = len(nombre)  
        # for pos in range(lon):
        #     if pos%2 == 0 and pos !=0:
        #         print(pos,nombre[pos])
           
        # vocal = ("a","e","i","o","u")
        # for elem in datos:
        #     print(elem,end=" ") 
        # for elem in nombre:
        #     print(elem,end=" ")  
        
        # lon = len(datos)  
        # for pos in range(lon):
        #     print(pos,datos[pos])   
         
        # for pos,valor in enumerate(datos):
        #     print(pos,valor)   
        
        # for clave,valor in estudiantes.items():
        #     print(clave,valor,end=" ")
        # print()     
        # print(listaNotas)
        # for notas in listaNotas:
        #     print("For externo",notas)
        #     for nota in notas:
        #         print(nota,end=" ")
        #     print("Saliendo del for interno")    
        # print()    
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     acum=0
        #     for nota in notas:
        #         acum=acum+nota
        #     print(acum/len(notas),end=" ")   
        # listaAlumnos = [{"nombre":"Doménica","final":70},{"nombre":"Lady","final":60},{"nombre":"Natanael","final":90}]          
        # print("\nDiccionario de alumnos")
        # print(listaAlumnos)
        # acum=0
        # for alumnos in listaAlumnos:
        #     print(alumnos)
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,type(valor),end=" ")
        #     if type(valor) == int:
        #         acum=acum+valor
        #     print()  
        # print("Promedio",acum/3)                              
        
        #   listaAlumnos =[{"nombre":"Jose","final":90},{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #   print("\nDiccionario de alumnos")
        #   print(listaAlumnos)
        #   acum=0
        #   for alumnos in listaAlumnos:
        #       print(alumnos,len(alumnos))
        #       for clave,valor in alumnos.items():
        #         print(clave,":",valor,end=" ")
        #       if clave == "final":
        #          acum=acum+valor  
        #       print()
        #   print("Promedio",acum/len(listaAlumnos))
        
        # listaNotas =[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        # acum=0
        # cont=0
        # for notas in listaNotas:
        #     print("Primer for",notas)
        #     for nota in notas:
        #         print("Segundo for",nota)
        #         acum=acum+nota
        #         cont=cont+1
        # print(acum/cont)  
        
        # listaNotas =[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        # acum=0
        # cont=0
        # for notas in listaNotas:
        #     print(notas)
        #     acumparcial=0
        #     contparcial=0
        #     for nota in notas:
        #         acumparcial +=nota
        #         contparcial +=1
        #         acum=acum+nota
        #         cont=cont+1
        #     print(acumparcial/contparcial)    
        # print(acum/cont)
        
        listaNotas =[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+len(notas)
            acum=acum+acumparcial    
            print("Totalparcial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas)))    
        print("TotalGeneral:{} PromGeneral:{}".format(acum,acum/cont))        
bucle = For()
bucle.usoFor()
            