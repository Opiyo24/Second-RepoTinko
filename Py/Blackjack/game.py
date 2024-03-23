#!/usr/bin python3

import time
import random


class Player:
    def __init__(self, name, capital=1000, stake=0, count=0):
        self.name = name
        self.capital = capital
        self.stake = stake
        self.count = count

    def __str__(self):
        return f"\n\nPLAYER DETAILS:\n\nName:\t\t{self.name}\nCapital:\t{self.capital}\nStake:\t\t{self.stake}\nCard Count:\t{self.count}\n"
    
    def __repr__(self):
        return f"Player({self.name}, {self.capital}, {self.stake}, {self.count})"

    def play_stake(self):
        if (self.name == "COMPUTER"):
            limit = self.capital / 100
            seed = random.randint(0, limit)
            self.stake = seed * 100
            self.capital -= self.stake
            print(f"Computer stake:\t\t{self.stake}")
        else:
            while True:
                try:
                    stake_amount = int(input(f"How much woukd you like to stake?  "))
                    if stake_amount > 0 and stake_amount <= self.capital:
                        self.stake = stake_amount
                        self.capital -= self.stake
                        print(f"Player stake:\t\t{self.stake}")
                        break
                    else:
                        print('SORRY, You ran out of MUD!!!')
                except ValueError:
                    print('Stake amount must eb a number!!')

    
    def deal(self):
        cards = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13}
        selection = random.randint(1, 13)
        self.count += cards[selection]
        return self.count
    

    def question(self):
        choices = {1: "Hit", 2: "Stand"}
        if self.name == "COMPUTER":
            choice = random.randint(1, 2)
            if choice == 1:
                print(f"{self.name} chose to Hit")
            else:
                print(f"{self.name} chose to Stand")
            return choices[choice]
        else:
            while True:
                try:
                    choice = int(input(f"Would you like to Hit or Stand? 1.Hit   2.Stand  "))
                    if choice == 1:
                        print(f"{self.name} chose to {choices[choice]}")
                    else:
                        print(f"{self.name} chose to {choices[choice]}")

                    if choice in choices.keys():
                        return choices[choice]
                    else:
                        print('Invalid choice!!')
                except ValueError:
                    print('Invalid choice!!')

    def hit(self):
        self.play_stake()
        self.deal()

    def current_result(self):
        if self.count > 21:
            return "BUSTED!!"
        elif self.count == 21:
            return "BLACKJACK!!"
        else:
            return 21 - self.count
            

