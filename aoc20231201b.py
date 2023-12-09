import inflect
from aoc20231201a import *


def aoc(data):
    return do(
        data,
        {
            **{str(x): x for x in range(10)},
            **{inflect.engine().number_to_words(x): x for x in range(10)},
        },
    )
