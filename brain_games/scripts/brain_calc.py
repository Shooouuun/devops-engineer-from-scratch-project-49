from brain_games.engine.engine import run_game
from brain_games.games import calc_game

def main():
    run_game(calc_game.get_round_data, calc_game.RULES)

if __name__ == '__main__':
    main()
