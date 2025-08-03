import random

from .constants import (
    EVEN_ANSWER_NO,
    EVEN_ANSWER_YES,
    MAX_EVEN_NUMBER,
    MIN_EVEN_NUMBER,
    RULES_EVEN,
)

RULES = RULES_EVEN 


def get_round_data():
    number = random.randint(MIN_EVEN_NUMBER, MAX_EVEN_NUMBER)
    correct_answer = EVEN_ANSWER_YES if number % 2 == 0 else EVEN_ANSWER_NO
    return str(number), correct_answer
