from deck import deck
import random as r


def initialize_hand(hand):
    sum_of_hand = 0
    for i in range(2):
        card_name, card_value = r.choice(list(deck.items()))
        sum_of_hand += card_value
        hand.append(card_name)
    return sum_of_hand


def draw_another_card(choice, hand):
    if choice == "hit":
        card_name, card_value = r.choice(list(deck.items()))
        hand.append(card_name)
        return card_value
    else:
        return 0


def fill_computer_hand():
    while computer_sum <= 16:
        draw_another_card("hit", computer)


def compare_players():
    if player_sum == computer_sum:
        return "Draw!"
    elif player_sum > computer_sum:
        return "You win!"
    else:
        return "Computer wins!"


def check_sum(hand, sum_of_person):
    if sum_of_person > 21:
        index_of_aces = check_ace(hand)
        if not index_of_aces:  # list is empty
            return True
        else:


def check_ace(hand):
    possibilities = ["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds"]
    indexes_of_aces = []
    for card in hand:
        if card in possibilities:
            indexes_of_aces.append(hand.index(card))
    return indexes_of_aces


print(deck)
player = []
computer = []

player_sum = initialize_hand(player)
computer_sum = initialize_hand(computer)


print("Your cards:", player)
print("Your sum:", player_sum)

print("Computers first Card:", computer[0])
print("Sum of Computer:", computer_sum)

if player_sum == 21 or computer_sum == 21:
    print("BlackJack")
else:
    game_is_on = True
    while game_is_on:
        input_choice = input("You want to Hit or Stand? ").lower()
        player_sum += draw_another_card(input_choice, player)
        print("Your cards:", player)
        print("Your sum:", player_sum)
        if player_sum > 21:
            print("You loose, Value > 21")
            break
        if input_choice != "hit":
            fill_computer_hand()
            print(compare_players())
            break

