import math
import random
from .constants import (
    RULES_GCD,
    MIN_GCD_NUMBER,
    MAX_GCD_NUMBER
)

def generate_round():
    number1 = random.randint(MIN_GCD_NUMBER, MAX_GCD_NUMBER)
    number2 = random.randint(MIN_GCD_NUMBER, MAX_GCD_NUMBER)
    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
