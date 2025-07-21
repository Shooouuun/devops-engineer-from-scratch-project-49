import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_round():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer
