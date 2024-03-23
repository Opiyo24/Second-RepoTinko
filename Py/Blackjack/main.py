#!/usr/bin python3

import time
from game import Player


Computer = Player("COMPUTER", 1000, 0, 0)
player_name = str.upper(input("Enter your name: "))
Human = Player(player_name, 1000, 0, 0)

def winner():
    comp_result = Computer.current_result()
    human_result = Human.current_result()

    if comp_result == "BUSTED!!":
        print(f"{Human.name} WINS!!!")  # Player wins if computer busts
        return

    if human_result == "BUSTED!!":
        print(f"{Computer.name} WINS!!!")  # Computer wins if player busts
        return

    # Both players are not busted, compare scores
    winner = "Draw"  # Default winner (in case scores are equal)
    if human_result > comp_result:
        winner = Human.name
    elif human_result < comp_result:
        winner = Computer.name

    print(f"{winner} WINS!!!")


def main():
    print(Human)
    print(Computer)

    Human.play_stake()
    Computer.play_stake()
    print(f"\nPossible win:\t{Human.stake + Computer.stake}\n\n")

    Human.deal()
    print(f"Human card count: {Human.count}")
    time.sleep(2)
    Computer.deal()
    print(f"\nComputer card count: {Computer.count}")

    print("\n\n\tHIT or STAND\n")
    Human.question()

    print(f"Computer is thinking...")
    time.sleep(3)
    Computer.question()

    #Assuming everyone hits
    Computer.hit()
    Human.hit()

    print(Human)
    print(Computer)

    


main()