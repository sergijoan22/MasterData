from carnivoro import Carnivoro
from herbivoro import Herbivoro

lobo: Carnivoro = Carnivoro('Lobo', 12, 4, 'Lobo', 'Auuuu', 'Gris')
print(f'{lobo.nombre} está durmiendo? {lobo.durmiendo}')
lobo.dormir(6)