import random

from .constants import (
    HIDDEN_INDEX_MIN,
    HIDDEN_PLACEHOLDER,
    MAX_START,
    MAX_STEP,
    MIN_START,
    MIN_STEP,
    PROGRESSION_LENGTH,
    RULES_PROGRESSION,
)

RULES = RULES_PROGRESSION 


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = [str(start + i * step) for i in range(PROGRESSION_LENGTH)]

    hidden_index = random.randint(HIDDEN_INDEX_MIN, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = HIDDEN_PLACEHOLDER

    question = ' '.join(progression)
    return question, correct_answer
