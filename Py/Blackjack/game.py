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
    
    # @property
    # def name(self):
    #     return self.name
    
    # @name.setter
    # def name(self, new_name):
    #     self.name = new_name
    #     return

    # @property
    # def capital(self):
    #     return self.capital
    
    # @capital.setter
    # def capital(self, new_capital=1000):
    #     self.capital = new_capital
    #     return

    def play_stake(self):
        if (self.name == "Computer"):
            seed = random.randint(1, 10)
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

