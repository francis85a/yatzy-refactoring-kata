class Yatzy:
    def __init__(self, *dice):

    # Guardamos los dados en una lista para que el objeto tenga sus propios datos.
    # CODE SMELL: Mysterious Name (72) / Temporary Field (80).
        self.dice = list(dice)

    # Antes se usaban nombres como d1, d2... o _5. 
    # Ahora usamos una lista, que es más fácil de recorrer.



    @staticmethod
    def chance(*dice):
        return sum(dice)

    # Long Parameter List (74): el código estaba "atado" a 5 argumentos
    # Con '*dice' aceptamos cualquier numero de dados.

    @staticmethod
    def yatzy(*dice):
        for pip in dice:
            if pip != dice[0]:
                return 0
        return 50
           
    # Long Parameter List (74). Eliminamos d1, d2, d3, d4, d5.
    # Duplicated Code (72). Usamos un bucle 'for' básico para no repeitir código

    @staticmethod
    def _sum_by_value(dice, value):
        points = 0
        for pip in dice:
            if pip == value:
                points += value
        return points


    @staticmethod
    def ones(*dice):
        return Yatzy._sum_by_value(dice, 1)
    
    @staticmethod
    def twos(*dice):
        return Yatzy._sum_by_value(dice, 2)

    @staticmethod
    def threes(*dice):
        return Yatzy._sum_by_value(dice, 3)

    @staticmethod
    def fours(*dice):
        return Yatzy._sum_by_value(dice, 4)

    @staticmethod
    def fives(*dice):
        return Yatzy._sum_by_value(dice, 5)

    @staticmethod
    def sixes(*dice):
        return Yatzy._sum_by_value(dice, 6)

    # para todas las sumas:
    # Duplicated Code (72): La lógica de 'ones', 'twos', etc. era idéntica.
    # Long Parameter List (74): Eliminamos (d1..d5) y usamos self.dice.

    def pair(*dice):
        pair = 0
        for pip in dice:
            if dice.count(pip) >= 2 and pip > pair:
                pair = pip
        return pair * 2

    # Long Parameter List (74).
    # Duplicated Code (72): El algoritmo de conteo se repetía 
    # Usamos un conteo de frecuencias y buscamos desde el 6 hacia abajo.
        
    @staticmethod
    def two_pairs(*dice):
        counts = [0] * 6
        for pip in dice:
            counts[pip - 1] += 1
        
        pairs_count = 0
        total_points = 0
        
        for value in range(6, 0, -1):
            if counts[value - 1] >= 2:
                pairs_count += 1
                total_points += value
        
        if pairs_count == 2:
            return total_points * 2
        return 0

    # Long Parameter List (74): igual que siempre, cambiamos (d1, d2, d3, d4, d5) por '*dice' 
    # Duplicated Code (72): eliminamos la asignación manual de cada dado a la lista 'counts'
    # Mysterious Name (72): cambiamos las variables 'n' por 'pairs_found'
    # Loops (79): simplificamos el recorrido del array

    def four_of_a_kind(self):
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1
        
        for value in range(6, 0, -1):
            if counts[value - 1] >= 4:
                return value * 4
                
        return 0

        # Mysterious Name (72): argumentos como _1, _2 en la versión anterior.
        # Duplicated Code (72): el conteo de frecuencias se repetía.
        # Long Parameter List (74): usamos '*dice' para recibir los dados

    def three_of_a_kind(self):
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1
            
        for value in range(6, 0, -1):
            if counts[value - 1] >= 3:
                return value * 3
        return 0

    # lo mismo que en four_of_a_kind, pero buscando tríos.
    # Long Parameter List (74), Mysterious Name (72), Loops (79). Duplicated Code (72).

    @staticmethod
    def small_straight(*dice):
        sorted_dice = sorted(dice)
        
        if sorted_dice == [1, 2, 3, 4, 5]:
            return 15
        
        return 0

    # Long Parameter List (Pág. 74)
    # Long Function / Complexity (Pág. 73)
    # Solo ordenamos la lista con 'sorted()' y comparamos.
    # Duplicated Code (Pág. 72)
    # Se eliminó toda la repetición de 'tallies[d1-1] += 1', 'tallies[d2-1] += 1'...
    # Mysterious Name (Pág. 72)
    # Cambiamos 'tallies' por 'sorted_dice'.

    @staticmethod
    def large_straight(*dice):
        sorted_dice = sorted(dice)
        
        if sorted_dice == [2, 3, 4, 5, 6]:
            return 20
        
        return 0

    @staticmethod
    def full_house(*dice):
        counts = [0] * 6
        for die in dice:
            counts[die - 1] += 1
            
        has_pair = False
        has_three = False
        pair_value = 0
        three_value = 0

        for value in range(1, 7):
            if counts[value -1] == 2:
                has_pair = True
                pair_value = value
            elif counts[value -1] == 3:
                has_three = True
                three_value = value

        if has_pair and has_three:
            return pair_value * 2 + three_value * 3
        return 0
    
    # Mysterious Name (Pág. 72): cambiamos las variables por nombres mejores (floats).
    # Long Parameter List (Pág. 74): usamos '*dice' para recibir los dados
    # Duplicated Code (Pág. 72): había dos bucles 'for' idénticos para buscar el 2 y el 3: lo unimos en un solo bucle que comprueba ambas cosas
    # Dead Code / Speculative Generality (Pág. 80): tenía 'tallies = []' y luego 'tallies = [0]*6', el primero no se usa