# Made by: https://https://github.com/brandonbondig
# This program shows the martingale system visually, with adjustable variables.
# Note that this simulation is only for educational purposes.

import matplotlib.pyplot as plt
import random

# Multiplies the bet after a loss
multiplier = float(input("Betting Multiplier: "))
# Start Capital
money = float(input("Start Capital: "))
# Amount to bet every round
bet = float(input("Wager: "))

betnum = 0

total_money = []
total_bets = []
total_bet = []

while True:
    betnum += 1
    roll = random.randint(0,100)

    print("Bet Number:",round(betnum,2))
    print("Wage:",round(bet,2))
    print("Money:",round(money,2))
    print("Dice:", roll)

    total_money.append(money)
    total_bets.append(betnum)
    total_bet.append(bet)

    if roll < 50:
        money += bet
        bet = 10

    if roll >= 50:
        money -= bet
        bet *= multiplier
    if bet > money:
        break

# input for x and y axis
plt.plot(total_bets, total_money)
plt.show()

maximum = ((max(total_money)/10000)-1)*100
minimum = ((min(total_money)/10000)-1)*100

print('------------------------')
print("Number of bets:", betnum)
print("Min:", round(min(total_money), 2),",", "Max:", round(max(total_money), 2))
print("Biggest Gain:", str(round(float(maximum), 2)) + "%")
print("Biggest Loss:", str(round(float(minimum), 2)) + "%")
print("Biggest wager:", round(float(max(total_bet)), 2))
print('------------------------')