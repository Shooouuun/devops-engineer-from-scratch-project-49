from brain_games.engine.engine import run_game
from brain_games.games import prime_game


def main():
    run_game(prime_game.get_round, prime_game.RULES)


if __name__ == '__main__':
    main()
