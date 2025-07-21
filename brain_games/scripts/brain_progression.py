from brain_games.engine.engine import run_game
from brain_games.games import progression_game


def main():
    run_game(progression_game.generate_round, progression_game.RULES)


if __name__ == '__main__':
    main()
