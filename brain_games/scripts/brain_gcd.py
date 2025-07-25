#!/usr/bin/env python3

from brain_games.engine.engine import run_game
from brain_games.games import gcd_game


def main():
    run_game(gcd_game.generate_round, gcd_game.RULES)


if __name__ == '__main__':
    main()
