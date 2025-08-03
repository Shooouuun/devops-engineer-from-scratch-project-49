import random
from .constants import (
    RULES_EVEN,
    MIN_EVEN_NUMBER,
    MAX_EVEN_NUMBER,
    EVEN_ANSWER_YES,
    EVEN_ANSWER_NO
)

RULES = RULES_EVEN 

def get_round_data():
    number = random.randint(MIN_EVEN_NUMBER, MAX_EVEN_NUMBER)
    correct_answer = EVEN_ANSWER_YES if number % 2 == 0 else EVEN_ANSWER_NO
    return str(number), correct_answer
