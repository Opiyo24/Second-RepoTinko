#!/usr/bin python3

import time
from game import Player

def main():
    Computer = Player("Computer", 1000, 0, 0)
    player_name = str.upper(input("Enter your name: "))
    Human = Player(player_name, 1000, 0, 0)

    print(Human)
    print(Computer)

    Human.play_stake()
    Computer.play_stake()
    print(f"\nPossible win:\t{Human.stake + Computer.stake}\n\n")

    Human.deal()
    print(f"Human card count: {Human.count}")
    time.sleep(1)
    print(f"Computer is thinking...")
    time.sleep(2)
    Computer.deal()
    print(f"\nComputer card count: {Computer.count}")


main()