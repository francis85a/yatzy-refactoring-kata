from src.pips import Pips

class Yatzy:
    FIFTY = 50
    ZERO = 0

    @staticmethod
    def chance(*dice):
        return sum(dice)

    # Long Parameter List (74): el código estaba "atado" a 5 argumentos
    # Con '*dice' aceptamos cualquier numero de dados.

    @staticmethod
    def yatzy(*dice):
        ONE = Pips.ONE.value
        if len(set(dice)) == ONE:
            return Yatzy.FIFTY
        return Yatzy.ZERO

           
    # Long Parameter List (74). Eliminamos d1, d2, d3, d4, d5.
    # Duplicated Code (72). Usamos un bucle 'for' básico para no repeitir código

    @classmethod
    def ones(cls, *dice):
        ONE = Pips.ONE.value
        return Pips._sum_by_value(dice, ONE)

    @classmethod
    def twos(cls, *dice):
        TWO = Pips.TWO.value
        return Pips._sum_by_value(dice, TWO)

    @classmethod
    def threes(cls, *dice):
        THREE = Pips.THREE.value
        return Pips._sum_by_value(dice, THREE)

    @classmethod
    def fours(cls, *dice):
        FOUR = Pips.FOUR.value
        return Pips._sum_by_value(dice, FOUR)

    @classmethod
    def fives(cls, *dice):
        FIVE = Pips.FIVE.value
        return Pips._sum_by_value(dice, FIVE)

    @classmethod
    def sixes(cls, *dice):
        SIX = Pips.SIX.value
        return Pips._sum_by_value(dice, SIX)

    # para todas las sumas:
    # Duplicated Code (72): La lógica de 'ones', 'twos', etc. era idéntica.
    # Long Parameter List (74): Eliminamos (d1..d5) y usamos self.dice.

    @classmethod
    def pair(cls, *dice):
        TWO = Pips.TWO.value
        value = Pips.find_n_of_a_kind(dice, TWO)
        return value * TWO

    # Long Parameter List (74).
    # Duplicated Code (72): El algoritmo de conteo se repetía 
    # Usamos un conteo de frecuencias y buscamos desde el 6 hacia abajo.
        
    
    @classmethod
    def two_pairs(cls, *dice):
        ONE = Pips.ONE.value
        TWO = Pips.TWO.value
        # Usamos el motor de la clase Pips para obtener las frecuencias
        counts = Pips.get_counts(dice)
        
        pairs_count = 0
        total_points = 0

        for value in Pips.reversedValues():
            if counts[value - ONE] >= TWO:
                pairs_count += ONE
                total_points += value
        
        return (total_points * TWO) if pairs_count == TWO else cls.ZERO

    # Long Parameter List (74): igual que siempre, cambiamos (d1, d2, d3, d4, d5) por '*dice' 
    # Duplicated Code (72): eliminamos la asignación manual de cada dado a la lista 'counts'
    # Mysterious Name (72): cambiamos las variables 'n' por 'pairs_found'
    # Loops (79): simplificamos el recorrido del array

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = Pips.THREE.value
        value = Pips.find_n_of_a_kind(dice, THREE)
        return value * THREE

    # lo mismo que en four_of_a_kind, pero buscando tríos.
    # Long Parameter List (74), Mysterious Name (72), Loops (79). Duplicated Code (72).

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = Pips.FOUR.value
        value = Pips.find_n_of_a_kind(dice, FOUR)
        return value * FOUR

        # Mysterious Name (72): argumentos como _1, _2 en la versión anterior.
        # Duplicated Code (72): el conteo de frecuencias se repetía.
        # Long Parameter List (74): usamos '*dice' para recibir los dados

    @staticmethod
    def small_straight(*dice):
        FIFTEN = 15

        if set(dice) == Pips.minus(Pips.SIX):
                return FIFTEN
        return Yatzy.ZERO

    # Long Parameter List (Pág. 74)
    # Long Function / Complexity (Pág. 73)
    # Solo ordenamos la lista con 'sorted()' y comparamos.
    # Duplicated Code (Pág. 72)
    # Se eliminó toda la repetición de 'tallies[d1-1] += 1', 'tallies[d2-1] += 1'...
    # Mysterious Name (Pág. 72)
    # Cambiamos 'tallies' por 'sorted_dice'.

    @staticmethod
    def large_straight(*dice):
        TWENTY = 20
        if set(dice) == Pips.minus(Pips.ONE):
            return TWENTY
        
        return Yatzy.ZERO

    @classmethod
    def full_house(cls, *dice):
        ONE = Pips.ONE.value
        TWO = Pips.TWO.value
        THREE = Pips.THREE.value

        counts = Pips.get_counts(dice)

        if TWO in counts and THREE in counts:
            pair_value = counts.index(TWO) + ONE
            three_value = counts.index(THREE) + ONE
            
            return (pair_value * TWO) + (three_value * THREE)
            
        return cls.ZERO
    
    # Mysterious Name (Pág. 72): cambiamos las variables por nombres mejores (floats).
    # Long Parameter List (Pág. 74): usamos '*dice' para recibir los dados
    # Duplicated Code (Pág. 72): había dos bucles 'for' idénticos para buscar el 2 y el 3: lo unimos en un solo bucle que comprueba ambas cosas
    # Dead Code / Speculative Generality (Pág. 80): tenía 'tallies = []' y luego 'tallies = [0]*6', el primero no se usa