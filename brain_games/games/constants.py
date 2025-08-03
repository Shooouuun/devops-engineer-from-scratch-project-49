# games/constants.py

# Правила для игр
RULES_PROGRESSION = 'What number is missing in the progression?'

# Настройки арифметической прогрессии
PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 30
MIN_STEP = 1
MAX_STEP = 10

# Символ, скрывающий элемент прогрессии
HIDDEN_PLACEHOLDER = '..'
HIDDEN_INDEX_MIN = 0


# Calc game
RULES_CALC = 'What is the result of the expression?'

MIN_OPERAND = 1
MAX_OPERAND = 20
ALLOWED_OPERATORS = ['+', '-', '*']


# Even game
RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_EVEN_NUMBER = 1
MAX_EVEN_NUMBER = 100

EVEN_ANSWER_YES = 'yes'
EVEN_ANSWER_NO = 'no'


# GCD game
RULES_GCD = "Find the greatest common divisor of given numbers."

MIN_GCD_NUMBER = 1
MAX_GCD_NUMBER = 100


# Prime game
RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_PRIME_NUMBER = 1
MAX_PRIME_NUMBER = 100
MIN_PRIME_DIVISOR = 2

PRIME_ANSWER_YES = 'yes'
PRIME_ANSWER_NO = 'no'
