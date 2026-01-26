from enum import Enum, unique

@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())
    
    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - { pip.value }

    ###########

    @staticmethod
    def _sum_by_value(dice, value):
        points = 0
        for pip in dice:
            if pip == value:
                points += value
        return points
        
    @classmethod
    def get_counts(cls, dice):
        """Devuelve una lista con la frecuencia de cada cara (1-6)."""
        return [dice.count(face_value) for face_value in cls.values()]
    
    @classmethod
    def find_n_of_a_kind(cls, dice, n):
        """
        Busca el valor de dado más alto que aparece al menos 'n' veces.
        Retorna el valor del dado (1-6) o 0 si no se encuentra.
        """
        counts = cls.get_counts(dice)
        for value in cls.reversedValues():
            if counts[value - 1] >= n:
                return value
        return 0


if __name__ == "__main__":

    print(list(Pips))
    print(Pips(1))
    print(Pips['ONE'])
    print(Pips.ONE)
    print(Pips.ONE.name)
    print(Pips.ONE.value)
    for number in Pips.__members__.values():
        print(number._value_)
    
    print(Pips.values())
    print(Pips.reversedValues())
    print(Pips.minus(Pips.FIVE))

    # Se encarga de que el código dentro del bloque solo se ejecute 
    # cuando lanzas el archivo directamente (python pips.py). 
    # Si importas Pips desde otro archivo, este bloque se ignora.

    # Muestra la lista de todos los miembros del Enum Pips
    # print(list(Pips)) 
    
    # Busca y muestra el miembro que tiene el valor indicado
    # print(Pips(1)) 
    
    # Busca y muestra el miembro que tiene el nombre (key) indicado
    # print(Pips['ONE']) 
    
    # Acceso directo al indicado (1)
    # print(Pips.ONE) 
    
    # Imprime solo el nombre del INDICADO (1)
    # print(Pips.ONE.name) 
    
    # Imprime solo el valor numérico del indicado (1)
    # print(Pips.ONE.value) 
    
    # Recorre todos los miembros del Enum e imprime sus valores
    # for number in Pips.__members__.values():
    # print(number._value_)

    # Llama al método que devuelve una lista con solo los valores [1, 2, 3, 4, 5, 6]
    # print(Pips.values()) 
    
    # Llama al método que devuelve la lista pero al revés [6, 5, 4, 3, 2, 1]
    # print(Pips.reversedValues()) 
    
    # Llama al método que devuelve una lista con todos los valores menos el que indicas (5 en este caso)
    # print(Pips.minus(Pips.FIVE))