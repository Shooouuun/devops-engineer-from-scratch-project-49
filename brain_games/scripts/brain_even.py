import prompt, random
from brain_games.cli import welcome_user

'''def play_even_game():
    random_num = random.randint(1, 100)
    correct_answer = 'yes' if random_num % 2 == 0 else 'no'

    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"Question: {random_num}")
    answer = prompt.string('Your answer: ').lower()

    if answer == correct_answer:
        print('Correct!')
        return True
    elif random_num % 2 != 0:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False'''



def is_even(number):
    return number % 2 == 0


def play_even_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    
    print(f"Question: {number}")
    user_answer = input("Your answer: ").lower().strip()
    
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


def play_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".\nYou need to give three correct answers')
    
    correct_answers = 0
    
    while correct_answers < 3:
        if play_even_round():
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")



def main():
    print("Welcome to the Brain Games!")
    play_even_game()

if __name__ == '__main__':
    main()