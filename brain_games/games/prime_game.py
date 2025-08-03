import random
from .constants import (
    RULES_PRIME,
    MIN_PRIME_NUMBER,
    MAX_PRIME_NUMBER,
    MIN_PRIME_DIVISOR,
    PRIME_ANSWER_YES,
    PRIME_ANSWER_NO
)


RULES = RULES_PRIME 


def is_prime(n):
    if n < MIN_PRIME_DIVISOR:
        return False
    for i in range(MIN_PRIME_DIVISOR, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_round():
    number = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    correct_answer = PRIME_ANSWER_YES if is_prime(number) else PRIME_ANSWER_NO
    return str(number), correct_answer
