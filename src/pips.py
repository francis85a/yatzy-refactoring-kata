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
    # Está aquí para probar que los enum y los métodos funcionan

    # print(list(Pips))
    # → [<Pips.ONE: 1>, <Pips.TWO: 2>, <Pips.THREE: 3>, <Pips.FOUR: 4>, <Pips.FIVE: 5>, <Pips.SIX: 6>]
    # Lista de todos los miembros del enum, en orden de definición.
    # Cada elemento es una instancia de Pips (no un int ni un str).

    # print(Pips(1))
    # → Pips.ONE
    # Accede al miembro cuyo valor asociado (value) es 1.

    # print(Pips['ONE'])
    # → Pips.ONE
    # Accede al miembro por su nombre (clave del enum), usando string.

    # print(Pips.ONE)
    # → Pips.ONE
    # Accede directamente al miembro definido en la clase.

    # print(Pips.ONE.name)
    # → 'ONE'
    # Devuelve el nombre textual del miembro.

    # print(Pips.ONE.value)
    # → 1
    # Devuelve el valor numérico asociado al miembro.

    # for number in Pips.__members__.values():
    # print(number._value_)
    # → 1  2  3  4  5  6
    # __members__ es un diccionario {nombre: miembro}.
    # Se itera por sus valores y se imprime el atributo interno _value_ (igual que .value).

    # print(Pips.values())
    # → [1, 2, 3, 4, 5, 6]
    # Devuelve los valores numéricos de cada cara del dado.

    # print(Pips.reversedValues())
    # → [6, 5, 4, 3, 2, 1]
    # Igual que el anterior, pero inverso.

    # print(Pips.minus(Pips.FIVE))
    # → 1  (si 6 - 5 = 1)
    # Devuelve todas las caras excepto la que indicas.
