#!/usr/bin/env python3
# brain_games/scripts/brain_games.py

from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import play_even_game

def main():
    print("Welcome to the Brain Games!")
    play_even_game()


if __name__ == '__main__':
    main()