import pytest
from enum import IntEnum
from src.yatzy import Yatzy


class Pip(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


@pytest.mark.chance
@pytest.mark.parametrize("dice, expected", [
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 15),
    ((Pip.ONE, Pip.ONE, Pip.THREE, Pip.THREE, Pip.SIX), 14),
    ((Pip.FOUR, Pip.FIVE, Pip.FIVE, Pip.SIX, Pip.ONE), 21),
])
def test_chance(dice, expected):
    assert expected == Yatzy.chance(*dice)


@pytest.mark.yatzy
@pytest.mark.parametrize("dice, expected", [
    ((Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE), 50),
    ((Pip.ONE, Pip.ONE, Pip.ONE, Pip.TWO, Pip.ONE), 0),
])
def test_yatzy(dice, expected):
    assert expected == Yatzy.yatzy(*dice)


@pytest.mark.parametrize("func,dice,expected", [
    (Yatzy.ones, (Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
    (Yatzy.ones, (Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE), 5),
    (Yatzy.twos, (Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
    (Yatzy.twos, (Pip.TWO, Pip.THREE, Pip.TWO, Pip.FIVE, Pip.ONE), 4),
    (Yatzy.threes, (Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE, Pip.ONE), 0),
    (Yatzy.threes, (Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FIVE), 9),
])
def test_number_categories(func, dice, expected):
    assert expected == func(*dice)


def test_static_interface():
    assert 5 == Yatzy.ones(*(Pip.ONE,)*5)
    assert 15 == Yatzy.chance(Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FIVE, Pip.FIVE), 0),
    ((Pip.FOUR, Pip.FOUR, Pip.ONE, Pip.TWO, Pip.THREE), 8),
    ((Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.FIVE, Pip.SIX), 12),
])
def test_fours(dice, expected):
    assert expected == Yatzy.fours(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.SIX), 0),
    ((Pip.FIVE, Pip.FIVE, Pip.ONE, Pip.TWO, Pip.THREE), 10),
    ((Pip.FIVE, Pip.FIVE, Pip.FIVE, Pip.FIVE, Pip.ONE), 20),
])
def test_fives(dice, expected):
    assert expected == Yatzy.fives(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
    ((Pip.SIX, Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR), 6),
    ((Pip.SIX, Pip.SIX, Pip.SIX, Pip.ONE, Pip.TWO), 18),
])
def test_sixes(dice, expected):
    assert expected == Yatzy.sixes(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FOUR), 8),
    ((Pip.ONE, Pip.ONE, Pip.SIX, Pip.TWO, Pip.SIX), 12),
    ((Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.ONE), 6),
    ((Pip.THREE, Pip.THREE, Pip.THREE, Pip.THREE, Pip.ONE), 6),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
])
def test_pair(dice, expected):
    assert expected == Yatzy.pair(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.ONE, Pip.TWO, Pip.THREE, Pip.THREE), 8),
    ((Pip.ONE, Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR), 0),
    ((Pip.ONE, Pip.ONE, Pip.TWO, Pip.TWO, Pip.TWO), 6),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
    ((Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.FIVE), 0),
])
def test_two_pairs(dice, expected):
    assert expected == Yatzy.two_pairs(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.THREE, Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FIVE), 9),
    ((Pip.THREE, Pip.THREE, Pip.FOUR, Pip.FIVE, Pip.SIX), 0),
    ((Pip.THREE, Pip.THREE, Pip.THREE, Pip.THREE, Pip.ONE), 9),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
])
def test_three_of_a_kind(dice, expected):
    assert expected == Yatzy.three_of_a_kind(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.TWO, Pip.TWO, Pip.TWO, Pip.TWO, Pip.FIVE), 8),
    ((Pip.TWO, Pip.TWO, Pip.TWO, Pip.FIVE, Pip.FIVE), 0),
    ((Pip.TWO, Pip.TWO, Pip.TWO, Pip.TWO, Pip.TWO), 8),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
])
def test_four_of_a_kind(dice, expected):
    assert expected == Yatzy.four_of_a_kind(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 15),
    ((Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE, Pip.SIX), 0),
    ((Pip.ONE, Pip.THREE, Pip.FOUR, Pip.FIVE, Pip.FIVE), 0),
    ((Pip.SIX, Pip.SIX, Pip.SIX, Pip.SIX, Pip.SIX), 0),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.SIX), 0),
])
def test_small_straight(dice, expected):
    assert expected == Yatzy.small_straight(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE, Pip.SIX), 20),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.FIVE), 0),
    ((Pip.ONE, Pip.THREE, Pip.FOUR, Pip.FIVE, Pip.FIVE), 0),
    ((Pip.SIX, Pip.SIX, Pip.SIX, Pip.SIX, Pip.SIX), 0),
    ((Pip.ONE, Pip.TWO, Pip.THREE, Pip.FOUR, Pip.SIX), 0),
])
def test_large_straight(dice, expected):
    assert expected == Yatzy.large_straight(*dice)


@pytest.mark.parametrize("dice,expected", [
    ((Pip.ONE, Pip.ONE, Pip.TWO, Pip.TWO, Pip.TWO), 8),
    ((Pip.TWO, Pip.TWO, Pip.THREE, Pip.THREE, Pip.FOUR), 0),
    ((Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.FOUR), 0),
    ((Pip.FOUR, Pip.FOUR, Pip.FOUR, Pip.ONE, Pip.TWO), 0),
])
def test_full_house(dice, expected):
    assert expected == Yatzy.full_house(*dice)
