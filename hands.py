import json, random

class Hands:
    def __init__(self):
        self.deck = []
        self.hand_types = ("Royal Flush", "Straight Flush", "Four-of-a-Kind", "Full House", "Flush", 
                           "Straight", "Three-of-a-Kind", "Two Pair", "One Pair", "High Card")
    
    def load_deck(self):
        try:
            with open('possible_cards.json') as file:
                self.deck = json.load(file)
        except FileNotFoundError:
            print("File not found.")
        return self.deck
    
    def draw_cards(self, origin, destination, amount):
        for i in range(amount):
            card = random.choice(origin)
            destination.append(card)
            origin.remove(card)
        return origin, destination
            
                