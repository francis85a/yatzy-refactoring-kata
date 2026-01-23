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
