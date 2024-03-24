#!/usr/bin python3

import time
from game import Player


Computer = Player("COMPUTER", 1000, 0, 0)
player_name = str.upper(input("Enter your name: "))
Human = Player(player_name, 1000, 0, 0)

def winner():
    """
    Announces a winner
    """
    comp_result = Computer.current_result()
    human_result = Human.current_result()

    if comp_result == "BUSTED!!":
        print(f"{Human.name} WINS!!!")  # Player wins if computer busts
        return

    if human_result == "BUSTED!!":
        print(f"{Computer.name} WINS!!!")  # Computer wins if player busts
        return

    # Both players are not busted, compare scores
    jaloch = "Draw"  # Default winner (in case scores are equal)
    if human_result > comp_result:
        jaloch = Human.name
    elif human_result < comp_result:
        jaloch = Computer.name

    return jaloch

def cards():
    print(f"\n\n{Human.name} card count: \t{Human.count}\n")
    print(f"{Computer.name} card count: \t{Computer.count}\n")

    if Human.count == 21:
        print(f"BLACLJACK!!! {Human.name} WINS!!!")
        return
    elif Computer.count == 21:
        print(f"BLACKJACK!!! {Computer.name} WINS!!!")
        return
    elif Human.count > 21 and Computer.count < 21:
        print(f"{Human.name} BUSTED!!! {Computer.name} WINS!!!")
        return


def hs(player="Both Players"):
    print(f"\n\n\t{player}, HIT or STAND\n")

def h_decision():
    hs(Human.name)
    decision = Human.question()
    if decision == "Hit":
        Human.deal()
        cards()
        hs(Human.name)
    else:
        return
    
def c_decision():
    hs(Computer.name)
    print(f"Computer is thinking...")
    time.sleep(3)
    decision = Computer.question()
    if decision == "Hit":
        Computer.deal()
        cards()
        hs(Computer.name)
    else:
        return


def decision():
    hs()
    human_decision = Human.question()

    print(f"Computer is thinking...")
    time.sleep(3)
    computer_decision = Computer.question()

    if human_decision == "Hit" and computer_decision == "Hit":
        Human.deal()
        Computer.deal()
        cards()
        decision()
    elif human_decision == "Hit" and computer_decision == "Stand":
        Human.deal()
        cards()
        h_decision()
    elif human_decision == "Stand" and computer_decision == "Hit":
        Computer.deal()
        cards()
        c_decision()
    else:
        return


def winner_announcement(jaloch):
    print()
    print("=========================================")
    print("\t", end="")
    print("WE HAVE A WINNER!!!")
    print("=========================================")
    # print()
    # print("\tThe winner is:", end="")
    # # time.sleep(3)
    # # print(".", end="")
    # # time.sleep(3)
    # # print(".", end="")
    # time.sleep(3)
    # print(".", end="")
    print()
    print()
    print(f"\n    CONGRATULATIONS {jaloch} !!!\n\n")
    print()
    print("=========================================")
    print()

def main():
    """
        Entry point
    """
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

    decision()
    print(Human)
    print(Computer)

main()