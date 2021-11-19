from carnivoro import Carnivoro
from herbivoro import Herbivoro


class Omnivoro(Carnivoro, Herbivoro):

    def __init__(self, )



class JefeCuadrilla(Supervisor, Destreza):
    """Clase la cual representa al Jefe de Cuadrilla"""

    def __init__(self, cedula, nombre, apellido, sexo, 
        rol, area, herramienta, experiencia, cuadrilla):
        """Constructor de clase Jefe de Cuadrilla"""

        # Invoca al constructor de clase Supervisor
        Supervisor.__init__(self, cedula, nombre, apellido, sexo, 
            rol)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)

        # Nuevos atributos
        self.cuadrilla = cuadrilla

    def __str__(self):
        """Devuelve cadena representativa al Jefe de Cuadrilla"""
        jq = "{0}: {1} {2}, rol '{3}', tareas {4}, cuadrilla: {5}"
        return jq.format(
            self.__doc__[28:46], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas(), self.cuadrilla)