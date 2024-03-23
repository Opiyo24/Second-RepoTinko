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
        return f"PLAYER DETAILS:\nName:\t\t{self.name}\nCapitat:\t\t{self.capital}\nStake:\t\t{self.stake}\nCard Count:\t{self.count}\n"
    
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
        else:
            while True:
                try:
                    stake_amount = int(input(f"How much woukd you like to stake?"))
                    if stake_amount > 0 and stake_amount <= self.capital:
                        self.stake = stake_amount
                        break
                    else:
                        print('SORRY, You ran out of MUD!!!')
                except ValueError:
                    print('Stake amount must eb a number!!')
