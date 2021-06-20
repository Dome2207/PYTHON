class Ciclo:
    
    def __init__(self, numero=5):
        self.numer=numero
        self.numero2=0


    def usoWhile(self):
        # ciclo repetitivo que se ejecuta mientras la condicion se cumpla (verdadero),
        # es decir sale por falso
        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in("a","e","i","o","u"):
            car = input("Ingrese vocal: ").lower()
        print("Felicitaciones su vocal es: {}".format(car))

ciclo1 = Ciclo()
ciclo1.usoWhile()
print("fin de uso ciclo")