import random

from .constants import ALLOWED_OPERATORS, MAX_OPERAND, MIN_OPERAND, RULES_CALC

RULES = RULES_CALC 


def get_round_data():
    number_one = random.randint(MIN_OPERAND, MAX_OPERAND)
    number_two = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(ALLOWED_OPERATORS)

    question = f"{number_one} {operator} {number_two}"
    correct_answer = str(eval(question))

    return question, correct_answer
