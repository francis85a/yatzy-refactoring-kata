from src.pips import Pips

class Yatzy:
    FIFTY = 50
    ZERO = 0

    @staticmethod
    def chance(*dice):
        return sum(dice)


    @staticmethod
    def yatzy(*dice):
        ONE = Pips.ONE.value
        if len(set(dice)) == ONE:
            return Yatzy.FIFTY
        return Yatzy.ZERO

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

    @classmethod
    def pair(cls, *dice):
        TWO = Pips.TWO.value
        value = Pips.find_n_of_a_kind(dice, TWO)
        return value * TWO

    
    @classmethod
    def two_pairs(cls, *dice):
        ONE = Pips.ONE.value
        TWO = Pips.TWO.value
        counts = Pips.get_counts(dice)
        
        pairs_count = 0
        total_points = 0

        for value in Pips.reversedValues():
            if counts[value - ONE] >= TWO:
                pairs_count += ONE
                total_points += value
        
        return (total_points * TWO) if pairs_count == TWO else cls.ZERO

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = Pips.THREE.value
        value = Pips.find_n_of_a_kind(dice, THREE)
        return value * THREE

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = Pips.FOUR.value
        value = Pips.find_n_of_a_kind(dice, FOUR)
        return value * FOUR

    @staticmethod
    def small_straight(*dice):
        FIFTEN = 15

        if set(dice) == Pips.minus(Pips.SIX):
                return FIFTEN
        return Yatzy.ZERO

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