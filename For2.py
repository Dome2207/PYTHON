class For:
    def __init__(self):
        pass
    
    
    def usoFor(self):
        # ciclo repetivo de incrementos o decrementos se ejecuta por verdadero
        nombre = "Doménica"
        datos=["Doménica",19,True]
        # pos     0       1   2
        numeros=(2,5,6,4,1)
        docente = {"nombre": "Doménica", "edad": 19, "fac": "faci"}
        listaNotas = [(30,40),(20,40),(50,40)]
        listaAlumnos = [{"nombre":"Doménica","final":70},{"nombre":"Lady","final":60},{"nombre":"Natanael","final":50}]
        # range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial
        # se ejecuta desde inicio hasta el limite
        # for con range() o for con colecciones 
        # j=0
        # while j<5:
        #     print("while",j)
        #     j=j+1
        
        for i in range(5): # rango(0,1,2,3,4)
            print("for",i,end=" ")
        print()    
        for i in range(1,5): # rango(1,2,3,4)
            print("for",i,end=" ")
        print()     
        for i in range(2,10,2): # rango(2,4,6,8)
            print("for",i,end=" ") 
        print()      
        for i in range(12,3,-3): # rango(12,9,6)
            print("for",i,end=" ")  
        
        lon = len(datos)  
        for pos in range(lon):
            print(pos,datos[pos])
                 
bucle = For()
bucle.usoFor()
            