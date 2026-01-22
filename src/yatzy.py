class Yatzy:
    def __init__(self, *dice):
        # Guardamos los dados en una lista para que el objeto tenga sus propios datos.
        # CODE SMELL: Mysterious Name (72) / Temporary Field (80).
        self.dice = list(dice)
        # REFACTORIZACIÓN:
        # Antes se usaban nombres como d1, d2... o _5. 
        # Ahora usamos una lista, que es más fácil de recorrer.

    @staticmethod
    def chance(*dice):
        return sum(dice)
        # REFACTORIZACIÓN: 
        # CODE SMELL: Long Parameter List (74).
        # Antes el código estaba "atado" a 5 argumentos. 
        # Con '*dice' aceptamos cualquier numero de dados.

    @staticmethod
    def yatzy(*dice):
        for pip in dice:
            if pip != dice[0]:
                return 0
        return 50
           

    # Sumas Simples: 
    # CODE SMELL: Long Parameter List (74). Eliminamos d1, d2, d3, d4, d5.
    # CODE SMELL: Duplicated Code (72). Antes cada función hacía lo mismo con lógica repetida
    # REFACTOR: Usamos un bucle 'for' básico, que es lo más fácil de entender

    @staticmethod
    def ones(*dice):
        points = 0
        for pip in dice:
            if pip == 1:
                points += 1
        return points

    @staticmethod
    def twos(*dice):
        points = 0
        for pip in dice:
            if pip == 2:
                points += 2
        return points

    @staticmethod
    def threes(*dice):
        points = 0
        for pip in dice:
            if pip == 3:
                points += 3
        return points


    def fours(self):
        points = 0
        for pip in self.dice:
            if pip == 4:
                points += 4
        return points

    def fives(self):

        points = 0
        for pip in self.dice:
            if pip == 5:
                points += 5
        return points

    def sixes(self):
        points = 0
        for pip in self.dice:
            if pip == 6:
                points += 6
        return points

    def pair(self, *dice):
        pair = 0

        for pip in dice:
            
            if dice.count(pip) >= 2 and pip > pair:
                pair = pip
        
        return pair * 2
        # Recorremos todos los dados recibidos como argumentos
        # Si el dado aparece al menos 2 veces y es mayor que el par guardado
        # Actualizamos el par más alto encontrado
        # Al final, devolvemos el puntaje del par más alto (valor del dado * 2)
        # Si no se encontró ningún par, pair sigue siendo 0 → devuelve 0
        # CODE SMELLS: Long Parameter List (74), Duplicated Code (72), MYSTERIOUS NAME (72), LOOPS (79).
        
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

    # REFACTORIZACIÓN Y CODE SMELLS:
    # Long Parameter List (74). Se cambió (d1, d2, d3, d4, d5) por '*dice' 
    # Duplicated Code (72). Se eliminó la asignación manual de cada dado a la lista 'counts'
    # Mysterious Name (72). Se cambiaron las variables 'n' por 'pairs_found'
    # Loops (79). Se simplificó el recorrido del array

    def four_of_a_kind(self):
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1
        
        for value in range(6, 0, -1):
            if counts[value - 1] >= 4:
                return value * 4
                
        return 0

    # REFACTORIZACIÓN Y CODE SMELLS:
    # Se usa un bucle 'for' para recorrer 'self.dice'. No importa si hay 5 dados o 10, el código funcionará igual sin repetir líneas.
    # Se cambiaron por 'counts' (conteo), 'die' (dado) y 'value' (valor del dado).
    # 'range(6, 0, -1)' permite ir directamente del valor 6 al 1.
    # Es mucho más intuitivo porque revisamos si tenemos cuatro "seises", luego cuatro "cincos", y así sucesivamente.
    # El 'return 0' al final es necesario para los casos donde no existan 4
    #CODE SMELL: Long Parameter List (74), Mysterious Name (72), Loops (79). Duplicated Code (72).

    def three_of_a_kind(self):
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1
            
        for value in range(6, 0, -1):
            if counts[value - 1] >= 3:
                return value * 3
        return 0

    # REFACTORIZACIÓN Y CODE SMELLS:
    # lo mismo que en four_of_a_kind, pero buscando tríos.
    #CODE SMELL: Long Parameter List (74), Mysterious Name (72), Loops (79). Duplicated Code (72).

    @staticmethod
    def small_straight(*dice):
        sorted_dice = sorted(dice)
        
        if sorted_dice == [1, 2, 3, 4, 5]:
            return 15
        
        return 0

    # REFACTORIZACIÓN Y CODE SMELLS:
    # CODE SMELL: Long Parameter List (Pág. 74)
    # CODE SMELL: Long Function / Complexity (Pág. 73)
    # Solo ordenamos la lista con 'sorted()' y comparamos.
    # CODE SMELL: Duplicated Code (Pág. 72)
    # Se eliminó toda la repetición de 'tallies[d1-1] += 1', 'tallies[d2-1] += 1'...
    # CODE SMELL: Mysterious Name (Pág. 72)
    # Cambiamos 'tallies' por 'sorted_dice'.

    @staticmethod
    def large_straight(*dice):
        sorted_dice = sorted(dice)
        
        if sorted_dice == [2, 3, 4, 5, 6]:
            return 20
        
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0