import random
from .constants import (
    RULES_PROGRESSION,
    PROGRESSION_LENGTH,
    MIN_START,
    MAX_START,
    MIN_STEP,
    MAX_STEP,
    HIDDEN_PLACEHOLDER,
    HIDDEN_INDEX_MIN
)

def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = [str(start + i * step) for i in range(PROGRESSION_LENGTH)]

    hidden_index = random.randint(HIDDEN_INDEX_MIN, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = HIDDEN_PLACEHOLDER

    question = ' '.join(progression)
    return question, correct_answer
