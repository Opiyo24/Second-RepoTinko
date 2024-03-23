#!/usr/bin python3

from game import Player

def main():
    Computer = Player("Computer", 1000, 0, 0)
    player_name = str.capitalize(input("Enter your name: "))
    Player(player_name, 1000, 0, 0)

    print(f"Copmuter.name: {Computer.name}")

main()