from brain_games.engine.engine import run_game
from brain_games.games import even_game


def main():
    run_game(even_game.get_round_data, even_game.RULES)


if __name__ == '__main__':
    main()
