# Score categories
# Change the values as you see fit
from enum import Enum, auto
from collections import Counter
from itertools import count, islice
from typing import List, Dict, Callable, Sequence, Iterable


class YachtCategory(Enum):
    YACHT = auto()
    ONES = auto()
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()


# export all categories as globals
cat: YachtCategory
for cat in YachtCategory:
    globals()[cat.name] = cat
del cat


def _same(dice: Sequence[int], val: int) -> int:
    """Return the score for ones, twos, etc.
    """
    return val * dice.count(val)


def _ones(dice: Sequence[int]) -> int:
    return _same(dice, 1)


def _twos(dice: Sequence[int]) -> int:
    return _same(dice, 2)


def _threes(dice: Sequence[int]) -> int:
    return _same(dice, 3)


def _fours(dice: Sequence[int]) -> int:
    return _same(dice, 4)


def _fives(dice: Sequence[int]) -> int:
    return _same(dice, 5)


def _sixes(dice: Sequence[int]) -> int:
    return _same(dice, 6)


def _full_house(dice: Sequence[int]) -> int:
    counts = Counter(dice)
    if not len(counts) == 2:
        return 0
    (_, hi_count), (_, lo_count) = counts.most_common()
    if hi_count != 3 or lo_count != 2:
        return 0

    return sum(dice)


def _four_of_a_kind(dice: Sequence[int]) -> int:
    counts = Counter(dice)
    [(val, cnt)] = counts.most_common(1)
    if cnt < 4:
        return 0
    return 4 * val


_LITTLE_LIST: List[int] = list(islice(count(1), 5))
_BIG_LIST: List[int] = list(islice(count(2), 5))


def _little_straight(dice: Sequence[int]) -> int:
    if _LITTLE_LIST != sorted(dice):
        return 0

    return 30


def _big_straight(dice: Sequence[int]) -> int:
    if _BIG_LIST != sorted(dice):
        return 0

    return 30


def _choice(dice: Sequence[int]) -> int:
    return sum(dice)


def _yacht(dice: Sequence[int]) -> int:
    counts = Counter(dice)
    [(_, cnt)] = counts.most_common(1)
    if cnt < 5:
        return 0
    return 50


_ScoreFunc = Callable[[Sequence[int]], int]

_SCORE_FUNCS: Dict[YachtCategory, _ScoreFunc] = {
    YachtCategory.YACHT: _yacht,
    YachtCategory.ONES: _ones,
    YachtCategory.TWOS: _twos,
    YachtCategory.THREES: _threes,
    YachtCategory.FOURS: _fours,
    YachtCategory.FIVES: _fives,
    YachtCategory.SIXES: _sixes,
    YachtCategory.FULL_HOUSE: _full_house,
    YachtCategory.FOUR_OF_A_KIND: _four_of_a_kind,
    YachtCategory.LITTLE_STRAIGHT: _little_straight,
    YachtCategory.BIG_STRAIGHT: _big_straight,
    YachtCategory.CHOICE: _choice,
}


def score(dice: List[int], category: YachtCategory) -> int:
    score_func = _SCORE_FUNCS[category]
    return score_func(dice)
