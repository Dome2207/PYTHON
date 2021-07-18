# class Cargo:
#    def __init__(self):
#        self.codigo=99
#        self.descripcion="Sin Cargo"
   
# cargo1 = Cargo()
# print(cargo1.codigo,cargo1.descripcion)
# cargo2 = Cargo()
# cargo2.codigo=1
# cargo2.descripcion="Ana"
# print(cargo2.codigo,cargo2.descripcion) 

   
# cargo1 = Cargo()
# print(cargo1.codigo,cargo1.descripcion)
# cargo2 = Cargo()
# cargo2.codigo=1
# cargo2.descripcion="Estudiante"
# print(cargo2.codigo,cargo2.descripcion)

# cargo1 = Cargo()
# print("cargo1",cargo1.codigo,cargo1.descripcion)
# cargo2 = Cargo()
# cargo2.codigo=1
# cargo2.descripcion="Estudiante"
# print("cargo2",cargo2.codigo,cargo2.descripcion)
# cargo3 = Cargo()
# cargo3.descripcion="Conserje"
# print("cargo3",cargo3.codigo,cargo3.descripcion)
  
#    def __init__(self,cod=99,des="Sin cargo"):
#        self.codigo=99
#        self.descripcion=des

class Cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des      
       
if __name__ == "__main__":
    cargo1 = Cargo()
    print("Ejecutando desde el archivo cargo.py")
    print("cargo1",cargo1.codigo,cargo1.descripcion)
    cargo2 = Cargo("Estudiante")
    print("cargo2",cargo2.codigo,cargo2.descripcion)
    cargo3 = Cargo()
    print("Cargo3",cargo3.codigo,cargo3.descripcion)
    print(Cargo.secuencia) 
        