

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
names = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]
colors = ["Spades", "Clubs", "Hearts", "Diamonds"]
deck = {}

for i in range(len(numbers)):
    for color in colors:
        name = f"{names[i]} of {color}"
        deck[name] = numbers[i]
