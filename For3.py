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
        # print()    
                  
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
            print() 
        print()                               
bucle = For()
bucle.usoFor()
            