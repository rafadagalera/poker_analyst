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
    1: "Straight Flush",
    2: "Four of a Kind",
    3: "Full House",
    4: "Flush",
    5: "Straight",
    6: "Three of a Kind",
    7: "Two Pair",
    8: "Pair",
    9: "High Card"
}

deck = []

for value in value_dict:
    for suit in suits:
        deck.append(f"{value}{suit}")

# print(deck)    
    