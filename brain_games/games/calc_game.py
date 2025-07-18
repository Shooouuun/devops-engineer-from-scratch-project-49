import random

RULES = 'What is the result of the expression?'

def get_round_data():
    number_one = random.randint(1, 20)
    number_two = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    question = f"{number_one} {operator} {number_two}"
    correct_answer = str(eval(question))

    return question, correct_answer
