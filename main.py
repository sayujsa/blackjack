from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playAgain = True
clear()

while playAgain:
    clear()
    print(logo)
    playerCards = [random.choice(cards) for x in range(2)]
    compCards = [random.choice(cards) for x in range(1)]

    if 11 in playerCards and sum(playerCards) > 21:
        playerCards[playerCards.index(11)] = 1

    print(f"\tYour cards are {playerCards} which adds to {sum(playerCards)}")

    if sum(playerCards) != 21:
        print(f"\tComputer's cards are {compCards}")

    while sum(playerCards) < 21:
        draw = input("Enter 'h' to hit or 's' to stand : ")
        if draw == 'h':
            newCard = random.choice(cards)
            playerCards += [1 if newCard == 11 and sum(playerCards)+newCard < 22 else newCard for x in range(1)]
            if sum(playerCards) == 21:
                print(f"\tYour new card is {playerCards} which adds to {sum(playerCards)}\nYou have a blackjack!!")
            else:
                print(f"\tYour new card is {playerCards} which adds to {sum(playerCards)}")
        elif draw == 's':
            break

    while sum(compCards) < 17:
        newCard = random.choice(cards)
        compCards += [1 if newCard == 11 and sum(playerCards)+newCard < 22 else newCard for x in range(1)]

    print(f"\tComputer's cards are {compCards} which adds to {sum(compCards)}")

    if sum(playerCards) < 22 and sum(playerCards) == sum(compCards):
        print("ITS A DRAW!!")
    elif sum(compCards) > 21 and sum(playerCards) < 22:
        print("YOU WIN!!")
    elif 22 > sum(playerCards) > sum(compCards):
        print("YOU WIN!!")
    elif 22 > sum(compCards) > sum(playerCards):
        print("YOU LOSE!!")
    else:
        print("YOU LOSE!!")

    again = input("Would you like to play again? (Y/N) : ").lower()

    if again == "y":
        playAgain = True
    if again == "n":
        break
