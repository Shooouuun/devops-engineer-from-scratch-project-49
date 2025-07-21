#!/usr/bin/env python3
# brain_games/scripts/brain_games.py

from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    print(f"To start the game, run brain-even,\n"
        f"brain-calc, brain_gcd, brain_prime or brain_progression.")


if __name__ == '__main__':
    main()
