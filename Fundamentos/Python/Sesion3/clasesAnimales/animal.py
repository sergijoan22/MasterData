	
class Animal:
    nombre: str
    edad: int
    nPatas: int
    raza: str
    ruido: str
    color: str
    
    def __init__(self, nombre, edad, nPatas, raza, ruido, color):
        self.nombre = nombre
        self.edad = edad
        self.nPatas = nPatas
        self.raza = raza
        self.ruido = ruido
        self.color = color
    
    def hacerRuido(self):
        print(self.ruido)
    
    def comer(self):
        print(f'El animal va a comer')