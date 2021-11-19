from animal import Animal
	
class Carnivoro(Animal):
        durmiendo: bool = False
        cazando: bool = False
        comiendo: bool = False
        descansando: bool = True
 
        def __init__(self,  ):
                super(Carnivoro, self).__init__(nombre, edad, nPatas, raza, ruido, color)
        
        def dormir(self, horas: int):
                self.durmiendo = True
                self.cazando = False
                self.comiendo = False
                self.descansando = False
                print(f'El carnívoro está durmiendo {horas} horas')
    
        def cazar(self, presa: str):
                self.durmiendo = False
                self.cazando = True
                self.comiendo = False
                self.descansando = False
                print(f'El carnívoro está cazando un/a {presa}')
        
        def reposar(self):
                self.durmiendo = False
                self.cazando = False
                self.comiendo = False
                self.descansando = True
                print(f'El carnívoro está en reposo')
        
        def comer(self, comida: str):
                self.durmiendo = False
                self.cazando = False
                self.comiendo = True
                self.descansando = False
                print(f'El carnívoro está comiendo {comida} horas')
