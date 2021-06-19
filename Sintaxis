class Sintaxis:
    instancia=0 # atributo de clase
    frase="Llamando"
     #__init__Metodoconstructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     # e inicializar los atributos de la clase. Self es un obejto que se representa la clase creadas
    def __init__(self,dato="Llamando al constructor1"):
        self.frase=dato # atributo de instancia
        Sintaxis.instancia = Sintaxis.instancia+1

    def usoVariable(self):
        edad, _peso = 19, 50
        nombres = "Domenica Pineda"
        car = nombres[0]
        Tipo__sexo = "F"
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario = ("dbpa","2207","domebetsa@gmail.com")
        # usuario[0]="Betsa"
        #usu = usuario[2]
        # print(usuario[2], nombre[7])
        # listas = [] colecciones mutables
        materias = []
        materias = ["Matematica", "Lengua", "Educacion Fisica"]
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        # print(materias,aux, materias[1])
        # diccionario = {} colecciones de objetos clave:valor tipo json
        estudiante={}
        estudiante = {"nombre": "Domenica", "edad": 19, "activo": True}
        edad =estudiante["edad"]
        estudiante["edad"]=20
        estudiante["carrera"]="IS"
        # print(estudiante,edad,estudiante["edad"])
        print(usuario,usuario[0],usuario[0:2],usuario[-1])
        print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3],materias[::-1],materias[-2:])

        # presentacion con format
        # print("""Mi nombre es {}, tengo {} años""". format(nombres,edad))

# print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))
ejer1 = Sintaxis() # Instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
# ejer2 = Sintaxis("instancia2")
# print(ejer1.frase)
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
# print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
# print(ejer2.frase)

ejer1.usoVariable()
