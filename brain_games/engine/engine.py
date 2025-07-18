import prompt

def run_game(get_round_data, rules):
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    print(rules)

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        question, correct_answer = get_round_data()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
