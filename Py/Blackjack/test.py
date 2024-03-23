#!/usr/bin python3

def status():
    from game import p_capital, c_capital, c_count, p_count, c_stake, p_stake, win_value, player, computer

    print(f"\nCurrent Status:\n{computer} :\t\t{c_capital}\n{player} :\t\t\t{p_capital}\n\n     Card Count: \n{computer}\t\t{c_count}\n{player} :\t\t\t{p_count}\n\n     Current Stake: \n{computer} :\t\t{c_stake}\n{player} :\t\t\t{p_stake}\n\nPossible win :\t\t{win_value}\n\n")
    print("=========================================\n")