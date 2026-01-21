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

#_________________________

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
        # CODE SMELL: Long Parameter List (74), Duplicated Code (72), MYSTERIOUS NAME (72), LOOPS (79).
        
    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
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