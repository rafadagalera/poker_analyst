value_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14 }

suits = {
    "S": 100,
    "H": 10,
    "C": 1,
    "D": 0.1
}

hand_ranks = {
    "Straight Flush": 1,
    "Four of a Kind": 2,
    "Full House": 3,
    "Flush": 4,
    "Straight": 5,
    "Three of a Kind": 6,
    "Two Pair": 7,
    "Pair": 8,
    "High Card": 9
}

deck = []

for value in value_dict:
    for suit in suits:
        deck.append(f"{value}{suit}")

# print(deck)    
    