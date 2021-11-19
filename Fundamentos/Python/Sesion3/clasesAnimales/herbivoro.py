from animal import Animal
	
class Herbivoro(Animal):
        durmiendo: bool = False
        siendoCazado: bool = False
        comiendo: bool = False
        descansando: bool = True
 
        def __init__(self, nombre, edad, nPatas, 
                        raza, ruido, color):
                super(Animal, self).__init__(nombre, edad, nPatas, raza,
                                            ruido, color)

        
        def dormir(self, horas: int):
                self.durmiendo = True
                self.siendoCazado = False
                self.comiendo = False
                self.descansando = False
                print(f'El herbívoro está durmiendo {horas} horas')
    
        def huir(self, cazador: str):
                self.durmiendo = False
                self.siendoCazado = True
                self.comiendo = False
                self.descansando = False
                print(f'El herbívoro está huyendo de un/a {cazador}')
        
        def reposar(self):
                self.durmiendo = False
                self.siendoCazado = False
                self.comiendo = False
                self.descansando = True
                print(f'El herbívoro está en reposo')
        
        def comer(self, comida: str):
                self.durmiendo = False
                self.siendoCazado = False
                self.comiendo = True
                self.descansando = False
                print(f'El herbívoro está comiendo {comida} horas')
