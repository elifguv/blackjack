#In this game we're going to assume that each of the card in the list has equal chance of occuring
import os #to clear the terminal
import random
# from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #the ace is going to count as 11 until the user goes over to 21.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls') #This function clears the terminal 
    users_cards = []
    computers_cards = []
    # print(logo)
    for card_value in range(2):
        users_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))
    users_sum = sum(users_cards)
    computers_sum = sum(computers_cards)
    print(f"Your cards: {users_cards}, current score: {users_sum}")
    print(f"Computer's first card: {computers_cards[0]}")

    if computers_sum == 21:
        print(f"Your final hand: {users_cards}, final score: {users_sum}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_sum}")
        print("Lose, opponent has Blackjack :(")
    
    elif users_sum == 21 and computers_sum != 21:
        while computers_sum < 17:
            value = random.choice(cards)
            computers_cards.append(value)
            computers_sum += value
        print(f"Your final hand: {users_cards}, final score: {users_sum}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_sum}")
        print("Win with a blackjack :)")
        
    else: # greater than or smaller than 21
        if users_sum < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                value = random.choice(cards)
                dealers_value = random.choice(cards)
                users_cards.append(value)
                users_sum += value
                computers_cards.append(dealers_value)
                computers_sum += dealers_value
                
        else:
            if 11 in users_cards and users_sum != 21:
                index = users_cards.index(11)
                users_cards[index] = 1
                users_sum -= 10 #ace is now 1, not 11. the sum is decreased by 10 
            elif 11 in computers_cards and len(computers_cards) != 2:
                computers_cards.remove(11)
                computers_cards.append(1)
                computers_sum -= 10

        while computers_sum < 17:
            value = random.choice(cards)
            computers_cards.append(value)
            computers_sum += value
        print(f"Your cards: {users_cards}, current score: {users_sum}")
        print(f"Computer's first card: {computers_cards[0]}")
        if users_sum > 21:
            print(f"Your final hand: {users_cards}, final score: {users_sum}")
            print(f"Computer's final hand: {computers_cards}, final score: {computers_sum}")
            print("You lose")
        else:
            print(f"Your final hand: {users_cards}, final score: {users_sum}")
            print(f"Computer's final hand: {computers_cards}, final score: {computers_sum}")
            if users_sum == computers_sum:
                print("Draw")
            elif users_sum > computers_sum:
                print("You win")
            elif computers_sum > 21:
                print("Opponent went over. You win!")
            else:
                print("You lose")
